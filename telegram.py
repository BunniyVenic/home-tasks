import telebot


token='7664862192:AAE7OgDL7dsxCNHohrO7iOkAVVYsONDeMVk'
bot=telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,"https://www.youtube.com/watch?v=xvFZjo5PgG0")
    bot.send_message(message.chat.id,"Здравствуйте! Перед началом работы, посмотрите наш туториал, отправленный выше. ")
    bot.send_message(message.chat.id,"Для сортировки чисел, отправьте сообщением набор чисел разделенных точкой с запятой")

@bot.message_handler(content_types=['document'])
def handle_docs_photo(message):

    chat_id = message.chat.id
    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    src = 'C:/Users/inna_/OneDrive/Рабочий стол/Веремеев Иван/pythonProject1/bots/files' + message.document.file_name;
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)
        bot.reply_to(message, "Пожалуй, я сохраню это")

    bot.polling()
