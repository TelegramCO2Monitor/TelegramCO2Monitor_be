from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters


class TelegramBot:
    def __init__(self, token: str):
        self.token = token
        self.application = Application.builder().token(self.token).build()
        self.application.add_handler(CommandHandler("start", self.start))
        self.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_message_text))

    @staticmethod
    async def start(update: Update) -> None:
        await update.message.reply_text(f"Ciao dal nostro bellissimo bot, {update.message.from_user.first_name}")

    @staticmethod
    def co2_text_message_calculator(message):
        co2_emissions_per_byte = 2.1
        return len(message) * co2_emissions_per_byte

    async def handle_message_text(self, update: Update) -> None:
        total_emissions = 0
        message = update.message.text
        total_emissions += self.co2_text_message_calculator(message)

        metadata_emissions = self.co2_text_message_calculator(update.message.to_json())

        total_emissions += metadata_emissions
        message = (f'Your only message emits {total_emissions}ng of Co2 for group member\n\nFull metadata message emits'
                   f' {metadata_emissions}ng of Co2 for group member')

        await update.message.reply_text(message)
