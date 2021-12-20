import telebot
bot = telebot.TeleBot('1743447427:AAFJpp7HC_H9SMiOLZmEkyTk93-ZXqz1mOU')
import random
from random import choice
from telebot import types

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id,"Привет-привет! Этот чат-бот поможет с выбором будущей специальности. Пожалуйста, ознакомься с функционалом!  \
/start - меню с основными функциями; /meet - здесь я рассказываю о себе; /recomendation - здесь собрана вся полезная информация для тебя, а именно сами тесты; \
/opros - это последний шаг к результату")

@bot.message_handler(commands=['meet'])
def start_command(message):
    bot.send_message(message.chat.id, "Здравствуй, дорогой друг! 👋     \
Меня зовут Соня, и я являюсь создателем этого чат-бота, который, надеюсь, поможет тебе сделать правильный выбор твоей будущей профессии! 🙃 ")

@bot.message_handler(commands=['recomendation'])
def get_user_info(message):
    bot.send_message(message.from_user.id, "Я предлагаю тебе пройти тесты, которые помогут определить направления, \
    которое тебе больше всего подходит ﻿😜﻿. После прохождения тестов я буду ждать от тебя результатов, \
    на основании которых мы сможем выбрать саму профессию, а не только её область. ")
    markup_inline = types.InlineKeyboardMarkup()
    item_1 = types.InlineKeyboardButton(text='Конечно, да ﻿👌﻿', callback_data='YES')
    markup_inline.add(item_1)
    bot.send_message(message.chat.id, 'Договорились? ﻿👌﻿', reply_markup=markup_inline)

@bot.message_handler(commands=['opros'])
def start(message):
        markup_reply = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Практическая деятельность')
        btn2 = types.KeyboardButton('Интеллектуально-исследовательская деятельность')
        btn3 = types.KeyboardButton('Работа с людьми')
        btn4 = types.KeyboardButton('Планово-экономические виды деятельности')
        btn5 = types.KeyboardButton('Эстетические виды деятельности')
        btn6 = types.KeyboardButton('Экстремальные виды деятельности')
        btn7 = types.KeyboardButton('Следущий шаг - /opros2')
        markup_reply.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        send_mess = f"{message.from_user.first_name} , тебе сейчас нужно выбрать один из предложенных вариантов. 👇"
        bot.send_message(message.chat.id, send_mess, reply_markup=markup_reply)

@bot.message_handler(commands=['opros2'])
def start(message):
        markup_reply = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Человек-человек')
        btn2 = types.KeyboardButton('Человек-природа')
        btn3 = types.KeyboardButton('Человек-техника')
        btn4 = types.KeyboardButton('Человек-знаковая система')
        btn5 = types.KeyboardButton('Человек-художественный образ')
        btn6 = types.KeyboardButton('Последний шаг - /opros3')
        markup_reply.add(btn1, btn2, btn3, btn4, btn5, btn6)
        send_mess = f"{message.from_user.first_name} , тебе сейчас нужно выбрать один из предложенных вариантов. 👇"
        bot.send_message(message.chat.id, send_mess, reply_markup=markup_reply)

@bot.message_handler(commands=['opros3'])
def start(message):
        markup_reply = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('INTJ')
        btn2 = types.KeyboardButton('INTP')
        btn3 = types.KeyboardButton('ENTJ')
        btn4 = types.KeyboardButton('ENTP')
        btn5 = types.KeyboardButton('INFJ')
        btn6 = types.KeyboardButton('INFP')
        btn7 = types.KeyboardButton('ENFJ')
        btn8 = types.KeyboardButton('ENFP')
        btn9 = types.KeyboardButton('ISTJ')
        btn10 = types.KeyboardButton('ISTP')
        btn11 = types.KeyboardButton('ISFJ')
        btn12 = types.KeyboardButton('ISFP')
        btn13 = types.KeyboardButton('ESTJ')
        btn14 = types.KeyboardButton('ESTP')
        btn15 = types.KeyboardButton('ESFJ')
        btn16 = types.KeyboardButton('ESFP')
        btn17 = types.KeyboardButton('Результат 🔮 - /resylt')
        markup_reply.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn14, btn15, btn16, btn17)
        send_mess = f"{message.from_user.first_name} , тебе сейчас нужно выбрать один из предложенных вариантов. 👇"
        bot.send_message(message.chat.id, send_mess, reply_markup=markup_reply)

@bot.message_handler(commands=['resylt'])
def start_command(message):
    first = [f"Воу, {message.from_user.first_name} - ты просто красавчик! 💕 Ты дошел до конца в поисках своей профессии, поэтому держи: Учитель, Врач, Работник СМИ, Писатель. ", \
        f"Поздравляю, {message.from_user.first_name}, ты преодолел этот путь к выбору своего будущего! 🎉 Держи список подходящих профессий: Ученый, Композитор, Бухгалтер, Социальный работник. ", \
        f"Вот я встретила тебя, {message.from_user.first_name}! 👏 Ты очень крут, ведь ты не только задумался о своем будущем, но и сделал достаточно серьезный шаг - узнал много нового о себе. Но чтобы расширить твои знания держи список профессйи для тебя: Программист, Менеджер, Журналист, Фермер.", \
        f"Поздравляю, {message.from_user.first_name}! 🎉 Ты на шаг приблизился к своему будущему, которое выбираешь только ты! Но вот, лови список подходящих для тебя профессий: Медсестра/медбрат, Юрист, Ученый, Руководитель компании."]
    bot.send_message(message.chat.id, random.choice(first) + ' Потом обязательно нажми /bye.')

@bot.message_handler(commands=['bye'])
def start_command(message):
    bot.send_message(message.chat.id, 'Спасибо, что ты доверяешь мне и моему боту в таком серьезном выборе! 🥰 Я очень ценю это, поэтому стараюсь совершенствоать бот. Как ты мог заметить, тебе выпало всего лишь 4 професии, но поверь, в ближайшее время их количество увеличится, а также в НЕСКОЛЬКО раз ВОЗРАСТЕТ КАЧЕСТВО обработки результатов. До скорых встреч! 😘')

@bot.callback_query_handler(func = lambda call: True)
def answer(call):
    if call.data == 'YES':
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item_11 = types.KeyboardButton('Тест №1')
        item_12 = types.KeyboardButton('Тест №2')
        item_13 = types.KeyboardButton('Тест №3')
        item_14 = types.KeyboardButton('Я прошел(ла)')
        markup_reply.add(item_11, item_12, item_13, item_14)
        bot.send_message(call.message.chat.id, text='Отлично! Все тесты, которые я скинула выше, предлагаю тебе пройти ﻿🤓﻿. Я не случайно выбрала 3 разных теста,\
                                                    но имеющие одну тематику. Это было сделано для того, чтобы результаты были более точными. \
                                                    Итак, когда пройдешь каждый из них, уведоми меня об этом. \
                                                    Ладно? ﻿😉﻿ Я надеюсь, что ДА)', reply_markup=markup_reply)

@bot.message_handler(content_types=['text'])
def get_text(message):
    if message.text == 'Тест №1':
        bot.send_message(message.chat.id, '1. Тест по методике от Л.Йовайши. Тест направлен на определение профессиональных склонностей. \
Вот ссылочка: ﻿👇﻿https://careertest.ru/tests/opredelenie-professionalnyh-sklonnostej/')
    elif message.text == 'Тест №2':
        bot.send_message(message.chat.id, '2. Тест по методике Е.А. Климова. Этот тест поможет тебе определиться с направлением, которое \
больше всего тебе подходит. Лови ссылку на тест с актуальными профессиями:\
 ﻿🙌﻿ https://testometrika.com/business/test-to-determine-career/')
    elif message.text == 'Тест №3':
        bot.send_message(message.chat.id, '3. Мой «тестовый фаворит» - тест «Ключи персонального мастерства». Это самый полный тест,\
 показывающий не только область будущей специальности, но и частично определяет черты характера. Держи ссылочку ﻿😜﻿ : https://kpmi.ru/about')
    elif message.text == 'Я прошел(ла)':
        bot.send_message(message.chat.id, 'Супер! Ты уже на финишной прямой, один шаг отделяет тебя от результатов. Тебе необходимо нажать на /opros и ответить на вопросы.')



bot.polling(none_stop= True, interval = 0) 