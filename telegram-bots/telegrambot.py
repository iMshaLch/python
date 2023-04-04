# from telegram import Update
# from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


# async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text(f'Hello {update.effective_user.first_name}')

# token = "5920446143:AAE4pV6XS738rYAmTMH4zoVZdMVfdKd0B04"
# app = ApplicationBuilder().token(token).build()

# app.add_handler(CommandHandler("hello", hello))

# app.run_polling()

# while i == req.text.find("update_id"):
#     print("New massage : ", req.text.find("first_name"), req.text.find("text"))
#     i += 1

import requests 
import time 

d = {}
while True:
    # req = requests.get("https://api.telegram.org/bot5920446143:AAE4pV6XS738rYAmTMH4zoVZdMVfdKd0B04/getUpdates").json()
    
    # for i in req["result"]: 
    #     if i["update_id"] not in d:
    #         print("New massage :", i["message"]["from"]["first_name"], i["message"]["text"])
    #         d[i["update_id"]] = i
    req = ()
    print(rew)

    time.sleep(0.5)

