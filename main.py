from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters import Text
from config import *
from Keyboards import *
from baza import *

PROGRAMM = ''

async def on_startup(_):
    print("Bot connect")


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)
Kval = ''


@dp.message_handler(commands=['start'])
async def start_programm(message: types.Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        text='Мы приветствуем вас в нашем телеграмм боте!Напишите кодовое слово: "Запуск". И мы взлетаем'
    )

    await bot.send_sticker(
        chat_id=message.from_user.id,
        sticker='CAACAgIAAxkBAAEIVV9kIIcrfTEeIMxsC_rLDTCCsdvkcwAC2A8AAkjyYEsV-8TaeHRrmC8E'
    )
    """
    await bot.send_message(
        chat_id=message.from_user.id,
        text='Предлагаем быстро и удобно подобрать курс по вашим интересам!',
        reply_markup=ikb
    )"""
    await message.delete()

@dp.message_handler(commands=['help'])
async def help_commands(message: types.Message):
    await message.answer('Если вам нужна помощь!',
                         reply_markup=get_m_b())


@dp.message_handler(Text(equals=['Запуск']))
async def zapusk_pr(message: types.Message):
    await bot.send_sticker(
        chat_id=message.from_user.id,
        sticker='CAACAgEAAxkBAAEIVXBkIIljOInx9qxDIMgawcFqzg9t0gACSgMAAm_XGETUUhY0_9qHgy8E'
    )
    await bot.send_message(
        chat_id=message.from_user.id,
        text='Выберите одно из направлений предложенных ниже',
        reply_markup=get_curs()
    )
    await message.delete()


@dp.message_handler(Text(equals=['Помощь']))
async def help_fas(message: types.Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        text='https://t.me/Yemmi17'
    )


@dp.callback_query_handler()
async def cod_comomands(callback: types.CallbackQuery):
    global PROGRAMM
    global Kval
    if callback.data == 'Cod':
        Kval = '1'
        await bot.send_message(
            chat_id=callback.from_user.id,
            text='Хей! Прекрасный выбор!'
            # Написать еще про програмистов факт
        )
        await bot.send_sticker(
            chat_id=callback.from_user.id,
            sticker='CAACAgIAAxkBAAEIVXRkIInFvUUyzG_JeKLziWAoO_LaVAACBQEAAvcCyA_R5XS3RiWkoS8E'  # Стикер програмиста
        )
        await bot.send_message(
            chat_id=callback.from_user.id,
            text='Выберите ваш уровень!',
            reply_markup=get_level()
        )
    elif callback.data == 'Engl':
        Kval = '2'
        await bot.send_message(
            chat_id=callback.from_user.id,
            text='Хей! Прекрасный выбор!'

        )
            # Написать еще про изучение английского факт
        await bot.send_message(
            chat_id=callback.from_user.id,
            text='Выберите ваш уровень!',
            reply_markup=get_level()
        )
        await bot.send_sticker(
            chat_id=callback.from_user.id,
            sticker='CAACAgEAAxkBAAEIVXZkIIoJJKu4P-QKilOethAs4lswdAACNAMAAk39MEQ6NQ7Fr4Wdqy8E'  # Стикер
        )
    elif callback.data == 'Analitik:':
        Kval = '3'
        await bot.send_message(
            chat_id=callback.from_user.id,
            text='Хей! Прекрасный выбор!'
        )
        await bot.send_message(
            chat_id=callback.from_user.id,
            text='Выберите ваш уровень!',
            reply_markup=get_level()
        )
        # Написать еще про аналитику
        await bot.send_sticker(
            chat_id=callback.from_user.id,
            sticker='CAACAgIAAxkBAAEIVXhkIIpYvv2k3o4l4xjI6n4iq6AGhQACPwAD29t-AAH05pw4AeSqaS8E'  # Стикер заменить
        )
    elif callback.data == 'New':
        await bot.send_message(
            chat_id=callback.from_user.id,
            text=TEXT_NEW,
            reply_markup=get_anket()
        )
    elif callback.data == 'Mi':
        await bot.send_message(
            chat_id=callback.from_user.id,
            text=TEXT_MIDLE,
            reply_markup=get_anket()
        )
    elif callback.data == 'Pro':
        await bot.send_message(
            chat_id=callback.from_user.id,
            text=TEXT_PRO,
            reply_markup=get_anket()
        )
    elif callback.data == 'GO':
        await bot.send_message(
            chat_id=callback.from_user.id,
            text=Vopros1,
            reply_markup=quests_1()
        )
    elif callback.data == 'Анкета':
        await bot.send_message(
            chat_id=callback.from_user.id,
            text=ANKETA,
            reply_markup=get_anket_2()
        )
        await bot.send_sticker(
            chat_id=callback.from_user.id,
            sticker='CAACAgIAAxkBAAEIVzxkIUNdqDIpTgusAf7s_cdrysHgeQACESEAAnLDQEhgZeBxMNdpAi8E'  # Добавить стикер
        )


@dp.message_handler(Text(equals=['Владимир']))
async def city_1(message: types.Message):
    await bot.send_sticker(
        chat_id=message.from_user.id,
        sticker='CAACAgIAAxkBAAEIV0BkIVH2quD0J9HDyZPYDTZ0IoAABPsKAAJvNKFLLGrsXU0btXgvBA'  # Добавить стик
    )
    await bot.send_message(
        chat_id=message.from_user.id,
        text='Выберите форму обучения.',
        reply_markup=question_2()

    )
@dp.message_handler(Text(equals=['Александров']))
async def city_2(message: types.Message):
    await bot.send_sticker(
        chat_id=message.from_user.id,
        sticker='CAACAgIAAxkBAAEIV0BkIVH2quD0J9HDyZPYDTZ0IoAABPsKAAJvNKFLLGrsXU0btXgvBA'  # Добавить стик
    )
    await bot.send_message(
        chat_id=message.from_user.id,
        text='Выберите форму обучения.',
        reply_markup=question_2()

    )


@dp.message_handler(Text(equals=['Вязники']))
async def city_3(message: types.Message):
    await bot.send_sticker(
        chat_id=message.from_user.id,
        sticker='CAACAgIAAxkBAAEIV0BkIVH2quD0J9HDyZPYDTZ0IoAABPsKAAJvNKFLLGrsXU0btXgvBA'  # Добавить стик
    )
    await bot.send_message(
        chat_id=message.from_user.id,
        text='Выберите форму обучения.',
        reply_markup=question_2()

    )


@dp.message_handler(Text(equals=['Гороховец']))
async def city_4(message: types.Message):
    await bot.send_sticker(
        chat_id=message.from_user.id,
        sticker='CAACAgIAAxkBAAEIV0BkIVH2quD0J9HDyZPYDTZ0IoAABPsKAAJvNKFLLGrsXU0btXgvBA'  # Добавить стик
    )
    await bot.send_message(
        chat_id=message.from_user.id,
        text='Выберите форму обучения.',
        reply_markup=question_2()

    )


@dp.message_handler(Text(equals=['Ковров']))
async def city_5(message: types.Message):
    await bot.send_sticker(
        chat_id=message.from_user.id,
        sticker='CAACAgIAAxkBAAEIV0BkIVH2quD0J9HDyZPYDTZ0IoAABPsKAAJvNKFLLGrsXU0btXgvBA'  # Добавить стик
    )
    await bot.send_message(
        chat_id=message.from_user.id,
        text='Выберите форму обучения.',
        reply_markup=question_2()
    )


@dp.message_handler(Text(equals=['Суздаль']))
async def city_6(message: types.Message):
    await bot.send_sticker(
        chat_id=message.from_user.id,
        sticker='CAACAgIAAxkBAAEIV0BkIVH2quD0J9HDyZPYDTZ0IoAABPsKAAJvNKFLLGrsXU0btXgvBA'  # Добавить стик
    )
    await bot.send_message(
        chat_id=message.from_user.id,
        text='Выберите форму обучения.',
        reply_markup=question_2()
    )


@dp.message_handler(Text(equals=['Очная']))
async def form_study(message: types.Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        text='Выберите месяц начала',
        reply_markup=questions_3()
    )


@dp.message_handler(Text(equals=['Заочная']))
async def form_study(message: types.Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        text='Отлично!Выберите месяц начала',
        reply_markup=questions_3()
    )


@dp.message_handler(Text(equals=['Январь']))
async def month1(message: types.Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        text='Супер!',
        reply_markup=gc()
    )


@dp.message_handler(Text(equals=['Февраль']))
async def month1(message: types.Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        text='Супер!',
        reply_markup=gc()
    )


@dp.message_handler(Text(equals=['Март']))
async def month1(message: types.Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        text='Супер!',
        reply_markup=gc()
    )


@dp.message_handler(Text(equals=['Апрель']))
async def month1(message: types.Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        text='Супер!',
        reply_markup=gc()
    )


@dp.message_handler(Text(equals=['Май']))
async def month1(message: types.Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        text='Супер!',
        reply_markup=gc()
    )


@dp.message_handler(Text(equals=['Июнь']))
async def month1(message: types.Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        text='Супер!',
        reply_markup=gc()
    )


@dp.message_handler(Text(equals=['Июль']))
async def month1(message: types.Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        text='Супер!',
        reply_markup=gc()
    )


@dp.message_handler(Text(equals=['Август']))
async def month1(message: types.Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        text='Супер!',
        reply_markup=gc()
    )
@dp.message_handler(Text(equals=['Сентябрь']))
async def month1(message: types.Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        text='Супер!',
        reply_markup=gc()
    )
@dp.message_handler(Text(equals=['Октябрь']))
async def month1(message: types.Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        text='Супер!',
        reply_markup=gc()
    )
@dp.message_handler(Text(equals=['Ноябрь']))
async def month1(message: types.Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        text='Супер!',
        reply_markup=gc()
    )
@dp.message_handler(Text(equals=['Декабрь']))
async def month1(message: types.Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        text='Супер!',
        reply_markup=gc()
    )
@dp.message_handler(Text(equals=['Получить курс']))
async def get_curses(message: types.Message):
    global Kval
    if Kval =='1':
        await bot.send_message(
            chat_id=message.from_user.id,
            text= s
        )
    elif Kval =='3':
        await bot.send_message(
            chat_id=message.from_user.id,
            text= k
        )
    elif Kval == '2':
        await bot.send_message(
            chat_id=message.from_user.id,
            text= n #Допилить
        )



@dp.message_handler()
async def message_otv(message: types.Message):
    await bot.send_message(
            chat_id=message.from_user.id,
            text='Я еще не умею отвечать на все ваши сообщения. Но скоро обязательно научусь. Но если у вас возникли проблемы с использованием бота нажмите - /help'


        )
if __name__ == "__main__":
    executor.start_polling(
        dp,
        skip_updates=True,
        on_startup=on_startup
    )