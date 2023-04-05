#  --telegram bot with buttons
import time
import requests
from datetime import datetime
import logging
from telegram.ext import (
    Application, 
    CommandHandler, 
    ContextTypes, 
    ConversationHandler,
    MessageHandler, 
    filters, 
    ApplicationBuilder
)
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from bs4 import BeautifulSoup

buttons = ReplyKeyboardMarkup([["Dollar kursi"], ["Hozirgi vaqt"]], 
    resize_keyboard=True, input_field_placeholder="Nima kerak")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # reply_keyboard = [["Dollar kursi", "Hozirgi vaqt"]]

    # await update.message.reply_text(
    #     f"Salom {update.effective_user.first_name} !\n\n"
    #     "Pastdagi buyruqlardan birini tanlang",
    #     reply_markup=ReplyKeyboardMarkup(
    #         reply_keyboard, one_time_keyboard=True, resize_keyboard=True, input_field_placeholder="Nima kerak"
    #     ),
    # )
    await update.message.reply_text(f'Hello {update.effective_user.first_name}', 
        reply_markup=buttons)

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Qanday yordam bera olaman ?')

async def hayr(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hayr {update.effective_user.first_name}')

async def date(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hozirgi vaqt   {datetime.now().strftime("%H:%M:%S")}')

async def kurs(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hozirgi kurs   '
    f'{(requests.get("https://api.exchangerate.host/latest?base=USD").json())["rates"]["UZS"]:.2f}'
    )

async def weather(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    site = requests.get('https://obhavo.uz/')
    soup = BeautifulSoup(site.text, 'html.parser')
    temp = soup.find(class_ = "current-forecast").text.strip()
    vaziyat = soup.find(class_ = "current-forecast-desc").text.strip()

    a, b = temp.splitlines()

    txt = f"Shahar : Toshkent \nHavo : {vaziyat} \nKunduzi : {a} \nKechasi : {b}"
    await update.message.reply_text(txt)

async def weather_city(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # site = 'https://obhavo.uz/'
    # sms += str(update.message.text)[9:]
    # site = requests.get(site)
    site = requests.get('https://obhavo.uz/Nukus/')
    soup = BeautifulSoup(site.text, 'html.parser')
    temp = soup.find(class_ = "current-forecast").text.strip()
    vaziyat = soup.find(class_ = "current-forecast-desc").text.strip()
    
    a, b = temp.splitlines()

    txt = f"Shahar : Nukus \nHavo : {vaziyat} \nKunduzi : {a} \nKechasi : {b}"
    await update.message.reply_text(txt)

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(update.message.text.title())





TOKEN = "5920446143:AAE4pV6XS738rYAmTMH4zoVZdMVfdKd0B04"
def main() -> None:
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    app.add_handler(CommandHandler("help", help))
    
    app.add_handler(CommandHandler("weather", weather))

    app.add_handler(MessageHandler(filters.Regex("/weather_Nukus"), weather_city))

    app.add_handler(MessageHandler(filters.Regex("hayr"), hayr))

    app.add_handler(MessageHandler(filters.Regex("Hozirgi vaqt"), date))

    app.add_handler(MessageHandler(filters.Regex("Dollar kursi"), kurs))

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    app.run_polling()

if __name__ == "__main__":
    main()
