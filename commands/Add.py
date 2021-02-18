from telegram import ParseMode
import json
from Variables import c, pvt_text


def add(update, context):
    try:
        if update.message.chat.id == c:
            user = update.message.from_user
            txt = update.message.text.split(" ", 1)
            txt.remove("/newcit")
            with open("File.json", "r+") as file:
                a = json.load(file)
                a.append(txt[0])
                file.close()
            with open("File.json", "w") as file:
                json.dump(a, file)
                file.close()
            context.bot.send_message(chat_id=c, text="""Cittadino aggiunto con successo!\n\nRichiesto da: @"""
                                                     + user['username'])
        else:
            context.bot.send_message(chat_id=update.message.chat.id,
                                     text=pvt_text,
                                     parse_mode=ParseMode.HTML)
    except IndexError:
        context.bot.send_message(chat_id=c, text="""Sintassi erata, inserire parametri dopo /newcit
                                                 \nEsempio: /newcit Giorgio Stramaroni @GiorgioStramaroni""")
