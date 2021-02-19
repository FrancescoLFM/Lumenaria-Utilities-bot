import json
from telegram import ParseMode
from commands.Variables import c, pvt_text


def delete(update, context):
    if update.message.chat.id == c:
        try:
            user = update.message.from_user
            txt = update.message.text.split(" ", 1)
            txt.remove("/delcit")
            with open("File.json", "r+") as file:
                a = json.load(file)
                n = a[int(txt[0])-1]
                if (int(txt[0])) > 0:
                    a.remove(n)
                else:
                    raise IndexError
                file.close()
            with open("File.json", "w") as file:
                json.dump(a, file)
                file.close()
            context.bot.send_message(chat_id=c, text="""Cittadino rimosso con successo!\n
                                                     \n Richiesto da: @%s""" % user['username'])
        except IndexError:
            context.bot.send_message(chat_id=c, text="Attenzione! Devi inserire un numero interno alla lista!")
        except ValueError:
            context.bot.send_message(chat_id=c, text="""Sintassi errata! Inserisci un numero dopo il comando.
                                                     \nVedi a quale numero corrisponde il cittadino che vuoi eliminare
                                                     con\n/cittadini""")
    else:
        context.bot.send_message(chat_id=update.message.chat.id,
                                 text=pvt_text,
                                 parse_mode=ParseMode.HTML)
