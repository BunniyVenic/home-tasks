import telebot
import time

token='My_token'
bot=telebot.TeleBot(token)



users = {}


@bot.message_handler(func=lambda message: True)
def check_messages(message):
    user_id = message.from_user.id

    if user_id not in users:
        users[user_id] = {
            'message_count': 0,
            'last_message_time': time.time()
        }

    current_time = time.time()
    user = users[user_id]
    user['message_count'] += 1
    if current_time - user['last_message_time'] > 10:
        user['message_count'] = 1
        user['last_message_time'] = current_time

    if user['message_count'] > 3:
        bot.delete_message(message.chat.id, message.message_id)

    user['last_message_time'] = current_time


bot.polling()
