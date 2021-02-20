from commands.Variables import c, pvt_text
from time import process_time
from telegram import ParseMode

def newlist(update, context):
    t1_start = process_time()
    user = update.message.from_user
    admin = context.bot.get_chat_member(chat_id=c, user_id=user['id'])
    if update.message.chat.id == c:
        try:
            if admin['status'] == 'administrator' or 'creator':
                user = update.message.from_user
                with open("File.json", "wb") as file:
                    context.bot.get_file(update.message.reply_to_message.document.file_id).download(out=file)
                t1_stop = process_time()
                process_time_ms = (t1_stop-t1_start)*1000
                context.bot.send_message(chat_id=c,
                                         text="File caricato con successo in {} ms\nrichiesto da @{}".
                                         format(round(process_time_ms, 0), user['username']))
            else:
                context.bot.send_message(chat_id=c, text="Mi dispiace, per eseguire questa azione devi essere admin.")
        except AttributeError:
            with  file as open("File.json", "w"):
                file.write("[]")
             context.bot.send_message(chat_id=c,
                                      text="Nuova lista vuota generata.")
    else:
        context.bot.send_message(chat_id=update.message.chat.id,
                                 text=pvt_text,
                                 parse_mode=ParseMode.HTML)

