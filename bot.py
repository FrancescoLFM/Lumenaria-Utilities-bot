# Code by FrancescoLFM 2021
# No licences, free to use this code
import commands
from commands import TOKEN, filename
from telegram.ext import CommandHandler, Updater, CallbackContext
import telegram
import functools


def main():
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', commands.Start.start))
    dispatcher.add_handler(CommandHandler('newlist', commands.Newlist.newlist))
    dispatcher.add_handler(CommandHandler('cittadini', commands.Load.load))
    dispatcher.add_handler(CommandHandler('newcit', commands.Add.add(update=telegram.Update, context=CallbackContext,
                                                                     filename=filename)))
    dispatcher.add_handler(CommandHandler('delcit', commands.Del.delete))
    dispatcher.add_handler(CommandHandler('getlista', commands.Getlist.getlist))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()

