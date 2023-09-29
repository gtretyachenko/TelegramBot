# -*- coding: utf-8 -*-

import telebot
from telebot import types
import config

bot = telebot.TeleBot('6504913495:AAF53ujq-R8GLGfMzmy01VPKMW1Ueyge3y8')


@bot.message_handler(commands=['go', 'start'])  # Обработка команды для старта
def welcome(message):
    sti = open('welcome_start_sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    item1 = types.KeyboardButton("🌎 Участки")
    item2 = types.KeyboardButton("🏠 Дома")
    item3 = types.KeyboardButton('💰 Инвестиции')
    item4 = types.KeyboardButton('⛳ Карта поселков')
    item5 = types.KeyboardButton('☎ Связь с менеджером')
    item6 = types.KeyboardButton('📑 Ипотека')
    item7 = types.KeyboardButton('📑 Мы в соц сетях')

    markup.add(item1, item2, item3, item4, item5, item6, item7)

    bot.send_message(message.chat.id,
                     "Добро пожаловать {0.first_name}!\n\nКоманда - <b>{1.first_name}</b>, "
                     "приветствует Вас. "
                     "\n\nВыбирете нужный вам раздел меню."                     
                     "".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


# @bot.message_handler(content_types=['text'])
# def start(message):
#     if message.text == '/reg':
#         bot.send_message(message.from_user.id, "Как тебя зовут?")
#         bot.register_next_step_handler(message, get_name)  # следующий шаг – функция get_name
#     else:
#         bot.send_message(message.from_user.id, 'Напиши /reg')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '⛳ Карта поселков':
        bot.send_message(chat_id = message.from_user.id,
                         text= "<a href='https://yandex.ru/maps/21642/elektrougli/?from=mapframe&ll="
                               "38.224372%2C55.734000&mode=usermaps&source=mapframe&um="
                               "constructor%3A5f501a4ae56987d7e085e172cf1e6692aec63af8a0087fc300e4a422304d5e6a&"
                               "utm_source=mapframe&z=8'>Google</a>", parse_mode="html")

    elif message.text == '☎ Связь с менеджером':
        bot.send_message(chat_id=message.from_user.id, text='Лилия Толмачова +7 (926) 201-01-12'
                                                            '\n\nЦырен Лудупов +7 (999) 099-92-15'
                                                            '\n\nАдминистратор +7 (929) 604-58-46', parse_mode='html')
    elif message.text == '📑 Ипотека':
        keyboard = types.InlineKeyboardMarkup()  # наша клавиатура
        key_transh = types.InlineKeyboardButton(text='Траншевая ипотека на строительство дома', callback_data='transh')  # кнопка «Да»
        keyboard.add(key_transh)  # добавляем кнопку в клавиатуру
        key_family = types.InlineKeyboardButton(text='Семейная ипотека, ставка от 6%', callback_data='family')
        keyboard.add(key_family) # добавляем кнопку в клавиатуру
        key_government = types.InlineKeyboardButton(text='С господдержкой от 8%', callback_data='government')
        keyboard.add(key_government) # добавляем кнопку в клавиатуру
        key_it = types.InlineKeyboardButton(text='IT ипотека 5%', callback_data='it')
        keyboard.add(key_it) # добавляем кнопку в клавиатуру
        key_ground = types.InlineKeyboardButton(text='Ипотека на покупку земельного участка от 14 %', callback_data='ground')
        keyboard.add(key_ground) # добавляем кнопку в клавиатуру
        bot.send_message(message.from_user.id, text="Выберите тип ипотечного кредитования:", reply_markup=keyboard)


def get_name(message):  # получаем фамилию
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
    bot.register_next_step_handler(message, get_surname)


def get_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, 'Сколько тебе лет?')
    bot.register_next_step_handler(message, get_age)


def get_age(message):
    global age
    while age == 0:  # проверяем что возраст изменился
        try:
            age = int(message.text)  # проверяем, что возраст введен корректно
        except Exception:
            bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')

    keyboard = types.InlineKeyboardMarkup()  # наша клавиатура
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')  # кнопка «Да»
    keyboard.add(key_yes)  # добавляем кнопку в клавиатуру
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
    keyboard.add(key_no)
    question = 'Тебе ' + str(age) + ' лет, тебя зовут ' + name + ' ' + surname + '?'
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "transh":  # call.data это callback_data, которую мы указали при объявлении кнопки
        bot.send_message(call.message.chat.id, text='''
        Текст для трашевой ипотеки.   
        ''', parse_mode="html")
    elif call.data == "family":
        bot.send_message(call.message.chat.id, text='''
        Текст для семейной ипотеки.   
        ''', parse_mode="html")
    elif call.data == "government":
        bot.send_message(call.message.chat.id, text='''
        Текст для ипотеки с гос. поддержкой.   
        ''', parse_mode="html")
    elif call.data == "it":
        bot.send_message(call.message.chat.id, text='''
        Текст для IT ипотеки   
        ''', parse_mode="html")
    elif call.data == "ground":
        bot.send_message(call.message.chat.id, text='''
        Текст для ипотеки на земельный участок   
        ''', parse_mode="html")


@bot.message_handler(commands=['stop'])  # Обработка команды для выхода
def bye(message):
    #bye_Sti = open('byeMorty.tgs', 'rb')

    hideBoard = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id,
                     "Досвидания, {0.first_name}!\nМы, команда <b>{1.first_name}</b>, надеемся, что ты хорошо провел(а) время \n\n"
                     "Присоединяйся к нашей команде в <a href='<https://office_compressor.ru'>web</a>\n"
                     "Наш <a href='<https://instagram.com/office_compressor>'>inst</a>\n\n"
                     "Напиши Координатору проектов (<a href='<https://office_compressor.ru/admin>'>Админ</a>) и задай интересующие тебя вопросы по <i>проектной деятельности</i>\n\n"
                     "Надеемся, что тебе ответят очень скоро \n\n"
                     "<u>Don't be ill and have a nice day</u> \n\n\n"
                     "P.S.: Если есть какие-то пожелания или вопросы по боту, то напиши <a href='<https://office_compressor.ru/setmyaddresspls>'>мне</a>".format(
                         message.from_user, bot.get_me()), parse_mode='html', reply_markup=hideBoard)
    #exit()


name = ''
surname = ''
age = 0
bot.polling(none_stop=True, interval=0)
