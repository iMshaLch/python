import time
import requests
from datetime import datetime

d = {}
req = requests.get("https://api.telegram.org/bot5920446143:AAE4pV6XS738rYAmTMH4zoVZdMVfdKd0B04/getUpdates").json()
for i in req["result"]:
    d[i['update_id']] = i

while True:
    req = requests.get("https://api.telegram.org/bot5920446143:AAE4pV6XS738rYAmTMH4zoVZdMVfdKd0B04/getUpdates").json()
    
    for i in req["result"]: 
        name = i["message"]["from"]["first_name"]
        sms = i["message"]["text"]
        chat_id = i["message"]["chat"]["id"]
        
        if i["update_id"] not in d:
            if sms.lower() == "salom":
                ss = "https://api.telegram.org/bot5920446143:AAE4pV6XS738rYAmTMH4zoVZdMVfdKd0B04/sendMessage?chat_id="
                ss = ss + str(chat_id) + "&text=" + "Salom " + name + " !"
                # print(ss)
                requests.get(ss)              
            elif sms.lower() == "/time":
                mssg = datetime.now().strftime("%H:%M:%S")
                ss = "https://api.telegram.org/bot5920446143:AAE4pV6XS738rYAmTMH4zoVZdMVfdKd0B04/sendMessage?chat_id="
                ss = ss + str(chat_id) + "&text=" + str(mssg)
                requests.get(ss)
            elif sms.lower() == '/usd':
                mssg = requests.get("https://api.exchangerate.host/latest?base=USD").json()
                mssg = mssg['rates']['UZS']
                ss = "https://api.telegram.org/bot5920446143:AAE4pV6XS738rYAmTMH4zoVZdMVfdKd0B04/sendMessage?chat_id="
                ss = ss + str(chat_id) + "&text=" + str(mssg)
                requests.get(ss)
            elif sms[0] == "/":
                sms = sms[1:4].upper()
                mssg = requests.get("https://api.exchangerate.host/latest?base=USD").json()
                mssg = mssg['rates'][sms]
                ss = "https://api.telegram.org/bot5920446143:AAE4pV6XS738rYAmTMH4zoVZdMVfdKd0B04/sendMessage?chat_id="
                ss = ss + str(chat_id) + "&text=" + str(mssg)
                requests.get(ss)    
            else:
                ss = "https://api.telegram.org/bot5920446143:AAE4pV6XS738rYAmTMH4zoVZdMVfdKd0B04/sendMessage?chat_id="
                ss = ss + str(chat_id) + "&text=Siz xato formatda buyruq kiritdingiz !"
            d[i["update_id"]] = i
    
    # time.sleep(1)
            
            



