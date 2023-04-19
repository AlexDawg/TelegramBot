import telebot
from nums import TOKEN, keys
from extensions import APIException, Converter

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def function_name(message: telebot.types.Message):
    bot.send_message(message.chat.id, f"Привет, {message.chat.username}, для того чтобы вычислить курс валюты нужно указывать всё через пробел:\n <Имя валюты> <В какую валюту будем переводить> <Количество валюты>")

@bot.message_handler(commands=['values'])
def print_values(message: telebot.types.Message):
    text = "Доступные валюты:"
    for key in keys.keys():
        text = '\n'.join((text, key,))
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['help'])
def print_help(message: telebot.types.Message):
    bot.send_message(message.chat.id, f"Чтобы вывести список доступных валют введите команду /values\nЗапустить бота введите /start\n")

@bot.message_handler(content_types=['text'])
def get_price(message: telebot.types.Message):
     try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise APIException('Слишком много параметров.')

        val1, val2, amount = values
        total = Converter.convert(val1, val2, amount)
     except APIException as e:
        bot.send_message(message.chat.id, f'Ошибка пользователя.\n{e}')
     except Exception as e:
        bot.send_message(message.chat.id, f'Не удалось обработать команду.\n{e}')
     else:
        text = f'Цена {amount} {val1} в {val2} - {total}'
        bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)