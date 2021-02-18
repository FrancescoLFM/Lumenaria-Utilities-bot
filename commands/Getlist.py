def getlist(update, context):
    with open("File.json", 'rb') as file:
        context.bot.send_document(chat_id=update.message.chat_id,
                                  document=file, filename="File.json",
                                  caption="Ecco la lista più recente salvata")