# Code by FrancescoLFM 2021
# No licences, free to use this code
import commands
from commands import TOKEN
from telegram.ext import CommandHandler

while 1:
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', Start.start))
    dispatcher.add_handler(CommandHandler('newlist', Newlist.newlist))
    dispatcher.add_handler(CommandHandler('cittadini', Load.load))
    dispatcher.add_handler(CommandHandler('newcit', Add.add))
    dispatcher.add_handler(CommandHandler('delcit', Del.delete))
    dispatcher.add_handler(CommandHandler('getlista', Getlist.getlist))
    dispatcher.add_handler(CommandHandler('genlista', Genlist.genlist))


    updater.start_polling()
    updater.idle()
    continue
