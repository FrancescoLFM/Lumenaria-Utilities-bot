from commands.Variables import c, pvt_text
from telegram import ParseMode


def start(update, context):
    user = update.message.from_user
    admin = context.bot.get_chat_member(chat_id=c, user_id=user['id'])
    if update.message.chat.id == c:
        if admin['status'] == 'member':
            context.bot.send_message(chat_id=c,
                                     text="Grazie per avermi attivato, @%s " % (user['username']))
        if admin['status'] == 'administrator':
            context.bot.send_message(chat_id=c,
                                     text="Grazie per avermi attivato admin, @%s " % (user['username']))
        if admin['status'] == 'creator':
            context.bot.send_message(chat_id=c,
                                     text="Messaggio personalizzato solo per il creatore, @%s " % (user['username']))
    else:
        context.bot.send_message(chat_id=update.message.chat.id,
                                 text=pvt_text,
                                 parse_mode=ParseMode.HTML)
