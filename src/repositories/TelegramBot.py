from datetime import datetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from src.models.Message import Message
from src.models.User import User
from src.repositories.PostgreSQL import PostgreSQL


class TelegramBot:
    def __init__(self, token: str, db_instance: PostgreSQL):
        self.token = token
        self.application = Application.builder().token(self.token).build()
        self.application.add_handler(CommandHandler("start", self.start))
        self.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_message_text))
        self.application.add_handler(CommandHandler("info", self.info))
        self.db_instance = db_instance

    @staticmethod
    async def start(update: Update) -> None:
        await update.message.reply_text(f"Ciao dal nostro bellissimo bot, {update.message.from_user.first_name}")

    @staticmethod
    async def info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        keyboard = [[InlineKeyboardButton("Option 1", callback_data='1'),
                     InlineKeyboardButton("Option 2", callback_data='2')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text('Please choose:', reply_markup=reply_markup)

    @staticmethod
    def co2_text_message_calculator(message):
        co2_emissions_per_byte = 2.1
        return len(message) * co2_emissions_per_byte

    async def handle_message_text(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        total_emissions = 0
        message = update.message.text
        total_emissions += self.co2_text_message_calculator(message)
        metadata_emissions = self.co2_text_message_calculator(update.message.to_json())
        total_emissions += metadata_emissions

        telegram_id = update.message.from_user.id
        user_name = update.message.from_user.username or update.message.from_user.first_name

        with self.db_instance.LocalSession() as db:
            try:
                user = db.query(User).filter_by(telegram_id=telegram_id).first()
                if not user:
                    user = self.save_user(db, telegram_id, user_name)

                message_type = self.check_message_type(update)

                self.save_message(db, message_type, total_emissions, update, user)

                user.total_messages_weight += total_emissions
                db.commit()
            except Exception:
                db.rollback()

        reply_message = (f'Your message emits {total_emissions}ng of CO2\nFull metadata emits '
                         f'{metadata_emissions}ng of CO2')
        await update.message.reply_text(reply_message)

    async def initialize(self):
        await self.application.initialize()

    async def start(self):
        await self.application.start()
        await self.application.updater.start_polling()

    async def stop(self):
        await self.application.stop()

    @staticmethod
    def save_message(db, message_type, total_emissions, update, user):
        new_message = Message(
            type=message_type,
            weight=total_emissions,
            date=datetime.fromtimestamp(update.message.date.timestamp()),
            user_id=user.id
        )
        db.add(new_message)

    @staticmethod
    def check_message_type(update):
        if update.message.text:
            message_type = 'text'
        elif update.message.photo:
            message_type = 'photo'
        elif update.message.video:
            message_type = 'video'
        else:
            message_type = 'unknown'
        return message_type

    @staticmethod
    def save_user(db, telegram_id, user_name):
        user = User(
            telegram_id=telegram_id,
            name=user_name,
            registration_date=datetime.utcnow(),
            admin=False,
            active=True,
            phone=None,
            total_messages_weight=0,
            email=None
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
