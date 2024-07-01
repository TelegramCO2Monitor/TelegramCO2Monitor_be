from dotenv import load_dotenv
from fastapi import FastAPI
from src.app.api.api import router as api_router
from src.app.depends import init_db
import os
import logging
from telegram import Update
from telegram.ext import Application ,CommandHandler,ContextTypes,MessageHandler,filters


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

load_dotenv()

app = FastAPI(
    title='TeleCO2gram',
    docs_url='/docs'
)
app.include_router(api_router, prefix="/api")


@app.on_event("startup")
def on_startup():
    init_db()


def conversionLenChar_co2(len_text):
    # Estimate CO2 emissions (1 byte or 1 char of data ≈ 2.1 ng of CO2)
    co2_emissions_per_byte = 2.1
    # Calculate CO2 emissions
    co2_emissions = len_text * co2_emissions_per_byte
    return co2_emissions


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"Ciao dal nostro bellissimo bot, {update.message.from_user.first_name}")

async def hanle_message_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # eleborate when every write message in group why contains your bot
    # await update.message.reply_text(f"grazie per avermi scritto un messaggio")
    emission_text_message = str(conversionLenChar_co2(len(update.message.text)))
    emission_metadata_message = str(conversionLenChar_co2(len(update.message.to_json())))
    message = f'Your only message emits {emission_text_message}ng of Co2 for group member\n\nFull metadata message emits {emission_metadata_message}ng of Co2 for group member'
    await update.message.reply_text(message)

if __name__ == "__main__":
    import uvicorn

    Application = Application.builder().token(os.getenv('BOT_TOKEN')).build()

    Application.add_handler(CommandHandler('start', start))
    Application.add_handler(MessageHandler(None, hanle_message_text))
    Application.add_handler(MessageHandler(None, hanle_message_text))
    Application.run_polling()

    uvicorn.run(app, port=8000)
