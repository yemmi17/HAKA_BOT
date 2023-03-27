from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_m_b():
    kb = ReplyKeyboardMarkup(
        resize_keyboard=True
    )
    b1 = KeyboardButton(
        text='Запуск'
    )
    b3 = KeyboardButton(
        text='Помощь'
    )
    kb.add(b1,b3)
    return kb



def get_curs():
    kb_curs = InlineKeyboardMarkup(
        row_width=2
    )
    kb_c1 = InlineKeyboardButton(
        text='Английский',
        callback_data='Engl'
    )
    kb_c3 = InlineKeyboardButton(
        text='Программирование',
        callback_data='Cod'
    )
    kb_c2 = InlineKeyboardButton(
    text='Робототехника',
    callback_data='Analitik'
    )
    kb_curs.add(kb_c2, kb_c1).add(kb_c3)
    return kb_curs


def get_level():
    kb_info = InlineKeyboardMarkup(
        row_width=2
    )
    kb_i_ur1 = InlineKeyboardButton(
        text='Начинающий',
        callback_data='New'
    )
    kb_i_ur2 = InlineKeyboardButton(
        text='Уже что-то знаю',
        callback_data='Mi'
    )
    kb_i_ur3 = InlineKeyboardButton(
        text='Профи',
        callback_data='Pro'
    )
    kb_info.add(kb_i_ur1).add(kb_i_ur2).add(kb_i_ur3)
    return kb_info
def get_anket():
    ib_inf = InlineKeyboardMarkup(
        row_width=2
    )
    ib_1 = InlineKeyboardButton(
        text='Заполнить анкету!',
        callback_data='Анкета'
    )

    ib_inf.add(ib_1)
    return ib_inf

def get_anket_2():
    ib = InlineKeyboardMarkup(
        row_width=2
    )
    ib_b = InlineKeyboardButton(
        text='Начинаем',
        callback_data='GO'
    )
    ib.add(ib_b)
    return ib

def quests_1():
    kb = ReplyKeyboardMarkup(
        resize_keyboard=True
    )
    kb_1 = KeyboardButton(
        text='Александров'
    )
    kb_2 = KeyboardButton(
        text='Владимир'
    )
    kb_3 = KeyboardButton(
        text='Вязники'
    )
    kb_4 = KeyboardButton(
        text='Гороховец'
    )
    kb_5 = KeyboardButton(
        text='Ковров'
    )

    kb_6 = KeyboardButton(
        text='Суздаль'
    )
    kb.add(kb_1).add(kb_2).add(kb_3).add(kb_4).add(kb_5).add(kb_6)
    return kb

def question_2():
    kb = ReplyKeyboardMarkup(
        resize_keyboard=True
    )
    k_1 = KeyboardButton(
        text='Очная'
    )
    k_2 = KeyboardButton(
        text='Заочная'
    )
    kb.add(k_1,k_2)
    return kb

def questions_3():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    k1=KeyboardButton("Январь")
    k2=KeyboardButton("Февраль")
    k3=KeyboardButton("Март")
    k4=KeyboardButton("Апрель")
    k5=KeyboardButton("Май")
    k6=KeyboardButton("Июнь")
    k7=KeyboardButton("Июль")
    k8=KeyboardButton("Август")
    k9=KeyboardButton("Сентябрь")
    k10=KeyboardButton("Октябрь")
    k11=KeyboardButton("Ноябрь")
    k12=KeyboardButton("Декабрь")
    kb.add(k1,k2).add(k3,k4).add(k5,k6).add(k7,k8).add(k9,k10).add(k11,k12)
    return kb


def gc():
    kb = ReplyKeyboardMarkup(
        resize_keyboard=True
    )
    k1= KeyboardButton(
        text='Получить курс'
    )
    kb.add(k1)
    return kb