# Code by FrancescoLFM 2021
# No licences, free to use this code
import os
import json
from time import process_time
# from pydrive.auth import GoogleAuth
# from pydrive.drive import GoogleDrive
import logging
from telegram import ParseMode
from telegram.ext import Updater
from telegram.ext import CommandHandler
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
pvt_text="Attenzione! Funziono solo nella piazza di <a href='t.me/RepubblicaLumenaria'>Lumenaria</a>"
# Google Drive
# gauth = GoogleAuth()
# gauth.LocalWebserverAuth()
# drive = GoogleDrive(gauth)
# Hosting
PORT = int(os.environ.get('PORT', 5000))
# Bot
TOKEN="1535282631:AAFX7bS6oYsCHMAIFs5itBNvyDrDdkQflHU"
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher
c = -466724082
def start(update, context):
    user = update.message.from_user
    admin = context.bot.get_chat_member(chat_id=c, user_id=user['id'])
    if update.message.chat.id==c:
        if admin['status'] == 'member':
            context.bot.send_message(chat_id=c,
                                    text="Grazie per avermi attivato, @%s " %(user['username']))
        if admin['status'] == 'administrator':
            context.bot.send_message(chat_id=c,
                                    text="Grazie per avermi attivato admin, @%s " %(user['username']))
        if admin['status'] == 'creator':
            context.bot.send_message(chat_id=c,
                                    text="Messaggio personalizzato solo per il creatore, @%s " %(user['username']))
    else:
        context.bot.send_message(chat_id=update.message.chat.id,
                                    text=pvt_text,
                                    parse_mode=ParseMode.HTML)
def newlist(update, context):
    t1_start = process_time()
    user = update.message.from_user
    admin = context.bot.get_chat_member(chat_id=c, user_id=user['id'])
    if update.message.chat.id == c:
        try:
            if admin['status'] == 'administrator' or 'creator':
                user = update.message.from_user
                with open("file.json", "wb") as file:
                    context.bot.get_file(update.message.reply_to_message.document.file_id).download(out=file)
                t1_stop = process_time()
                process_time_ms = (t1_stop-t1_start)*1000
                context.bot.send_message(chat_id=c,
                                        text="File caricato con successo in {} ms\nrichiesto da @{}". format(round(process_time_ms, 0), user['username']))
            else:
                context.bot.send_message(chat_id=c, text="Mi dispiace, per eseguire questa azione devi essere admin.")
        except AttributeError:
            context.bot.send_message(chat_id=c,
                                    text="Devi rispondere al messaggio del file!")
    else:
        context.bot.send_message(chat_id=update.message.chat.id,
                                 text=pvt_text,
                                    parse_mode=ParseMode.HTML)
def load(update, context):
        try:
            if update.message.chat.id == c:
                with open("file.json") as file:
                    a = json.load(file)
                for i in range(1, len(a)+1):
                    a[i-1] = '%s) '%i + a[i-1]
                context.bot.send_message(chat_id=c,
                                        text="<b>Lista degli attuali cittadini</b>:\n"+('\n'.join(a)),
                                        parse_mode = ParseMode.HTML)
            else:
                context.bot.send_message(chat_id=update.message.chat.id,
                                        text=pvt_text,
                                        parse_mode=ParseMode.HTML)
        except UnicodeDecodeError:
            context.bot.send_message(chat_id=c, text="Errore fatale! Assicurati che il file sia in formato JSON")
        except TypeError:
            context.bot.send_message(chat_id=c,
                                     text="Non inserire numeri nel file!\n(Se vuoi inserirli devi mettere le virgolette)")

def add(update, context):
    try:
        if update.message.chat.id == c:
            user = update.message.from_user
            txt = (update.message.text).split(" ", 1)
            txt.remove("/newcit")
            with open("file.json", "r+") as file:
                a = json.load(file)
                a.append(txt[0])
                file.close()
            with open("file.json", "w") as file:
                json.dump(a, file)
                file.close()
            context.bot.send_message(chat_id=c, text="Cittadino aggiunto con successo!\n\nRichiesto da: @"+user['username'])
        else:
            context.bot.send_message(chat_id=update.message.chat.id,
                                     text=pvt_text,
                                     parse_mode=ParseMode.HTML)
    except IndexError:
        context.bot.send_message(chat_id=c, text="Sintassi erata, inserire parametri dopo /newcit\nEsempio: /newcit Giorgio Stramaroni @GiorgioStramaroni")

def delete(update, context):
    if update.message.chat.id == c:
        try:
            user = update.message.from_user
            txt = (update.message.text).split(" ", 1)
            txt.remove("/delcit")
            with open("file.json", "r+") as file:
                a = json.load(file)
                n = a[int(txt[0])-1]
                if (int(txt[0]))>0:
                    a.remove(n)
                else:
                    raise IndexError
                file.close()
            with open("file.json", "w") as file:
                json.dump(a, file)
                file.close()
            context.bot.send_message(chat_id=c, text="Cittadino rimosso con successo!\n\nRichiesto da: @%s"%user['username'])
        except IndexError:
            context.bot.send_message(chat_id=c, text="Attenzione! Devi inserire un numero interno alla lista!")
        except ValueError:
            context.bot.send_message(chat_id=c, text="Sintassi errata! Inserisci un numero dopo il comando. \nVedi a quale numero corrisponde il cittadino che vuoi eliminare con\n/cittadini")
    else:
        context.bot.send_message(chat_id=update.message.chat.id,
                                text=pvt_text,
                                parse_mode=ParseMode.HTML)
# Command Handlers
start_handler= CommandHandler('start', start)
newlist_handler = CommandHandler('newlist', newlist)
load_handler = CommandHandler('cittadini', load)
add_handler = CommandHandler('newcit', add)
delete_handler = CommandHandler('delcit', delete)
handler_array = [start_handler, newlist_handler, load_handler, add_handler, delete_handler]
#Adding Handlers
for i in range(len(handler_array)):
    dispatcher.add_handler(handler_array[i])
# updater loop
# updater.start_webhook(listen="0.0.0.0", port=int(PORT), url_path=TOKEN)
# updater.bot.setWebhook('https://boiling-plains-37671.herokuapp.com/' + TOKEN)
updater.start_polling()
updater.idle()