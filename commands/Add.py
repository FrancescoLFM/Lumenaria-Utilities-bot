from telegram import ParseMode
import json
from commands.Variables import c, pvt_text
from commands.Newlist import genlist
import html


def add_print(update, context, filename):
    user = update.message.from_user
    add(update, context, filename)
    context.bot.send_message(chat_id=c, text="""Cittadino aggiunto con successo!\n\nRichiesto da: @"""
                                             + user['username'])


def add(update, context, filename):
    exe = False
    try:
        if update.effective_chat.id == c:
            txt = update.message.text.split(" ")
            txt.remove("/newcit")
            print(len(txt))
            if len(txt) <= 3:
                for i in range(len(txt)):
                    if len(txt[i]) <= 30:
                        exe = True
                    else:
                        raise ValueError
            else:
                raise ValueError
            if exe:
                temp = " ".join(txt)
                print(txt)
                with open(filename, "r+") as file:
                    a = json.load(file)
                    a.append(html.escape(temp))
                    file.close()
                with open(filename, "w") as file:
                    json.dump(a, file)
                    file.close()
        else:
            context.bot.send_message(chat_id=update.message.chat.id,
                                     text=pvt_text,
                                     parse_mode=ParseMode.HTML)
    except IndexError:
        context.bot.send_message(chat_id=c, text="""Sintassi erata, inserire parametri dopo /newcit
                                                 \nEsempio: /newcit Giorgio Stramaroni @GiorgioStramaroni""")
    except ValueError:
        try:
            temp = "temp.json"
            genlist(temp)
            add(update, context, temp)
            file = "File.json"
            genlist(file)
            add_print(update, context, file)
        except ValueError:
            context.bot.send_message(chat_id=c, text="""Nome troppo lungo! Assicurati di aver
                                                        inserito massimo 30 caratteri""")
