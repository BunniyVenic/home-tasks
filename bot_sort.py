import telebot
token='7664862192:AAE7OgDL7dsxCNHohrO7iOkAVVYsONDeMVk'
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,"https://www.youtube.com/watch?v=xvFZjo5PgG0")
    bot.send_message(message.chat.id,"Здравствуйте! Перед началом работы, посмотрите наш туториал, отправленный выше. ")
    bot.send_message(message.chat.id,"Для сортировки чисел, отправьте сообщением набор чисел разделенных точкой с запятой")


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text
    numbers = list(map(int, (num.strip() for num in text.split(';'))))
    def counting_sort(arr, exp):
        n = len(arr)
        output = [0] * n
        count = [0] * 10

        for i in range(n):
            index = (arr[i] // exp) % 10
            count[index] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        for i in range(n - 1, -1, -1):
            index = (arr[i] // exp) % 10
            output[count[index] - 1] = arr[i]
            count[index] -= 1

        for i in range(n):
            arr[i] = output[i]

    def radix_sort(arr):
        max_num = max(arr)
        exp = 1
        while max_num // exp > 0:
            counting_sort(arr, exp)
            exp *= 10
    bot.send_message(message.chat.id.join(map(str, numbers)))
    radix_sort(numbers)


bot.infinity_polling()
