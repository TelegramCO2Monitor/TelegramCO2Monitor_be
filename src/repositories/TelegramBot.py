from datetime import datetime

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from fastapi import Depends
from sqlalchemy.orm import Session
from src.app.depends import get_db
from src.models.Message import Message
import logging


class TelegramBot:
    def __init__(self, token: str):
        self.token = token
        self.application = Application.builder().token(self.token).build()
        self.application.add_handler(CommandHandler("start", self.start))
        self.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_message_text))
        self.application.add_handler(CommandHandler("info", self.info))

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

        logging.info('dovrebbe salvare messaggio')
        self.save_message_to_db(update.message, total_emissions)
        logging.info('ha salvato il messaggio')

        reply_message = (f'Your message emits {total_emissions}ng of CO2\nFull metadata emits {metadata_emissions}ng of CO2')
        await update.message.reply_text(reply_message)

    async def initialize(self):
        await self.application.initialize()

    async def start(self):
        await self.application.start()
        await self.application.updater.start_polling()

    async def stop(self):
        await self.application.stop()

    def save_message_to_db(self, message: Message, total_emissions: int, db: Session = Depends(get_db)):
        logging.info('dentro funione salva')
        new_message = Message(
            type=message.content_type,
            weight=total_emissions,
            date=datetime.fromtimestamp(message.date),
            user_id=1
        )
        db.add(new_message)
        db.commit()
