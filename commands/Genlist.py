def genfile(update, context):
  with  file as open("File.json", "w"):
    file.write("[]")
  context.bot.send_message(chat_id=c,
                           text="Nuova lista vuota generata.")
