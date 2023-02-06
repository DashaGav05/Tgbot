import random
import telebot
from telebot import types
from Token import TOKEN

# Токен для подключения к телеграмм боту
TOKEN = TOKEN

bot = telebot.TeleBot(TOKEN)

# Составляем словарь с предметами и учителями
diction_lesson = {
    "Выполнение работ по одной или нескольким профессиям рабочих, "
    "должностям служащих": 'Крылова Александра Анатольевна',
    'МДК': "Крылова Александра Анатольевна",
    'Защита информации в информационно-телекоммуникационных системах и сетях с использованием программных и '
    'Программно-аппаратных средств защиты': 'Родичкин Павел Филиппович',
    'Английский язык': 'Фомичева Валерия Юрьевна',
    'Информатика': 'Никонова Дарья Николаевна',
    'Компьютерный сети': 'Костромитинова Александра Максимовна',
    'Право': 'Сергеева Лариса Сергеевна',
    'Основы алгоритмизации и программирования': 'Костромитинова Александра Максимовна',
    'Физика': 'Черников Вячеслав Васильевич ',
    'Физическая культура': 'Трубицин Антон Юрьевич',
    'Электроника и схемотехника': 'Стетюха Любовь Геннадьевна'
}

# Функция приветствия через команду /start
@bot.message_handler(commands=['start'])
def start_message(message):
    hello_list = ['Привет', 'Здраствуй', 'Hi']
    hello_txt = f'<b>{random.choice(hello_list)}, {message.from_user.first_name}</b> 👋'
    bot.send_message(message.chat.id, hello_txt, parse_mode='html')
    bot.send_message(message.chat.id, 'Введите команду <b>/help</b>', parse_mode='html')

# Реализуем команду /help и выводим кнопки для дальнейших действий
@bot.message_handler(commands=['help'])
def help_user(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    item1 = types.KeyboardButton('📌Мое расписание📌')
    item2 = types.KeyboardButton('📌Список предметов и учителей📌')
    item3 = types.KeyboardButton('📌Журнал успеваемости📌')
    item4 = types.KeyboardButton('📌Автор бота📌')
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, 'Выберите что вам нужно', reply_markup=markup)


# Реализуем обработчик текста поступающего от пользователя
@bot.message_handler(content_types=['text'])
def message_reply(message):
    # Отправляем ссылку на расписание
    if message.text == '📌Мое расписание📌' or message.text == 'Мое расписание':
        markup = types.InlineKeyboardMarkup()
        url_timetable = types.InlineKeyboardButton('Ссылка на расписание', url='https://ies.unitech-mo.ru/schedule?d=16.01.2023')
        markup.add(url_timetable)
        bot.send_message(message.chat.id, 'Перейди по ссылки', reply_markup=markup)

    elif message.text == '📌Список предметов и учителей📌' or message.text == 'Список предметов и учителей':
        # Реализуем распаковку словаря с помощью цикла в текст сообщения
        for key in diction_lesson:
            txt = f'<b>{key}</b>: {diction_lesson[key]}'
            bot.send_message(message.chat.id, txt, parse_mode='html')
    # Отправляем ссылку на журнал
    elif message.text == '📌Журнал успеваемости📌' or message.text == 'Журнал успаваемости':
        markup = types.InlineKeyboardMarkup()
        url_journal = types.InlineKeyboardButton('Ссылка на журнал', url='https://ies.unitech-mo.ru/studentplan?sem=4')
        markup.add(url_journal)
        bot.send_message(message.chat.id, 'Перейди по ссылки', reply_markup=markup)
    # Отправляем ссылку на вк пользователю
    elif message.text == '📌Автор бота📌' or message.text == 'Автор бота':
        markup = types.InlineKeyboardMarkup()
        author = types.InlineKeyboardButton('Ссылка на автора', url='https://vk.com/dogs_my_dogs')
        markup.add(author)
        bot.send_message(message.chat.id, 'Пиши свои пожелание по боту', reply_markup=markup)
    # Пишем обработчик для сообщений не внесенных в условия
    else:
        bot.send_message(message.chat.id,
                         'Я вас не понимаю. Напишите команду /help , чтобы узнать о моих возможностях.')


bot.infinity_polling()
