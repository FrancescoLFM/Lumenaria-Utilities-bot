from telegram import ParseMode
import json
from commands.Variables import c, pvt_text
import html


def add(update, context):
    try:
        if update.message.chat.id == c:
            user = update.message.from_user
            txt = update.message.text.split(" ", 1)
            txt.remove("/newcit")
            
            if len(txt) == 3:
                for i in range(len(txt)):
                    if len(txt[i]) <= 30:
                        exe = True
                    else:
                        raise ValueError
            else:
                raise ValueError
            
            # Issue from LoZack solved
            
            if exe:
                temp = " ".join(txt)
                print(txt)
                with open("File.json", "r+") as file:
                    a = json.load(file)
                    a.append(html.escape(temp))
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
    except ValueError:
        context.bot.send_message(chat_id=c, text="""Nome troppo lungo! Assicurati di aver inserito massimo 30 caratteri""")
