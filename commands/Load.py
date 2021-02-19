import json
from commands.Variables import c, pvt_text
from telegram import ParseMode


def load(update, context):
    try:
        if update.message.chat.id == c:
            with open("File.json") as file:
                a = json.load(file)
            for i in range(1, len(a)+1):
                a[i-1] = '%s) ' % i + a[i-1]
            context.bot.send_message(chat_id=c,
                                     text="<b>Lista degli attuali cittadini</b>:\n"+('\n'.join(a)),
                                     parse_mode=ParseMode.HTML)
        else:
            context.bot.send_message(chat_id=update.message.chat.id,
                                     text=pvt_text,
                                     parse_mode=ParseMode.HTML)
    except UnicodeDecodeError:
        context.bot.send_message(chat_id=c, text="Errore fatale! Assicurati che il file sia in formato JSON")
    except TypeError:
        context.bot.send_message(chat_id=c,
                                 text="""Non inserire numeri nel file!\n
                                      (Se vuoi inserirli devi mettere le virgolette)""")
