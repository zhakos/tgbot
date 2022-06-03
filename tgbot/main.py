from cgitb import text
import logging
from operator import contains
from re import IGNORECASE
from tracemalloc import stop
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from os import getenv
from sys import exit
import db_request as db
import datetime
import inline_short_subject_ru as sisb

# Объект бота
bot_token = "5322427961:AAElTOBaFWlfxonWpzYRIO7TZK-JhtNuU0s"
#if not bot_token:
#    exit("Error: no token provided")
bot = Bot(token=bot_token)
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропуститinь важные сообщения
logging.basicConfig(level=logging.INFO)

subject_short_ru = {'физ','мат','хим','гео','био','истор','англ','русс','казах','человек','чоп'}

@dp.message_handler(lambda message: bool(set(message.text.split()) & subject_short_ru))
async def cmd_all(message: types.message):
    buttons = sisb.button_from_short_subject(message.text)
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.answer("Выберите один профильный предмет", reply_markup=keyboard)

# Payment
@dp.message_handler(Text(contains="плата", ignore_case=True))
async def cmd_menu_items(message: types.Message):
    await message.answer('<b>Биология-География</b>\n "Педагогика и Психология" - 443.400 тг в год\n "',
                         parse_mode='html')


# Magistracy
@dp.message_handler(Text(contains="магистр", ignore_case=True))
async def cmd_menu_items(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    buttons = ["first", "second", "third", "chetvertyii",
               "pyatyi", "shestoi", "🔄Назад🔄"]
    keyboard.add(*buttons)
    await message.answer("👨🏻‍🎓Выберите специальность магистратуры👨🏻‍🎓", reply_markup=keyboard)


# Doctoral
@dp.message_handler(Text(contains="доктор", ignore_case=True))
async def cmd_menu_items(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    buttons = ["first1", "second2", "third3", "chetvertyii4",
               "pyatyi5", "shestoi6", "🔄Назад🔄"]
    keyboard.add(*buttons)
    await message.answer("👨‍🔬Выберите специальность докторантуры👨‍🔬", reply_markup=keyboard)


# GrantsAndDiscount
@dp.message_handler(Text(contains="Внутренние гранты и скидки", ignore_case=True))
async def cmd_menu_items(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="100%", callback_data='100'),
        types.InlineKeyboardButton(text="50%", callback_data='50'),
        types.InlineKeyboardButton(text="25%", callback_data='25'),
        types.InlineKeyboardButton(text="20%", callback_data='20'),
        types.InlineKeyboardButton(text="10%", callback_data='10'),
    ]
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*buttons)
    await message.answer("Выберите скидку", reply_markup=keyboard)


@dp.message_handler(commands="menu")
async def cmd_menu(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    buttons = ["📚Предметы📚", "💰Оплата💰", "❓Задать вопрос❓", "📋Внутренние гранты и скидки📋",
               "🏢Колледж ЕНТ Специальности🏢", "👨🏻‍🎓Специальности Магистратуры👨🏻‍🎓",
               "👨‍🔬Специальности Докторантуры👨‍🔬"]
    keyboard.add(*buttons)
    await message.answer("Здравствуйте, Коркыт Ата бот приветствует вас🙋‍♂️\nВыберите действие",
                         reply_markup=keyboard)


# Ask a Question
@dp.message_handler(Text(contains="вопрос", ignore_case=True))
async def cmd_ask_ques(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="Напишите нам на WhatsApp", callback_data='100',
                                   url='http://wa.me/+77029224458'),
    ]
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*buttons)
    await message.answer("<a href='http://wa.me/+77029224458'><b>Напишите нам на WhatsApp</b></a>", parse_mode='html',
                         reply_markup=keyboard)


@dp.message_handler(Text(contains="предметы", ignore_case=True))
async def cmd_menu_items(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, )
    buttons = ["Биология-География", "География-Всемирная История", "География-Английский Язык",
               "Всемирная История-Человек.Общество.Право", "Казахский Язык-Казахская Литература", "Математика-Физика",
               "Математика-География", "Русский Язык-Русская Литература", "Химия-Биология",
               "Химия-Физика", "Английский Язык-Всемирная История", "Творческий экзамен", "🔄Назад🔄"]
    keyboard.add(*buttons)
    await message.answer("Выберите свои предметы", reply_markup=keyboard)


@dp.message_handler(Text(contains="назад", ignore_case=True))
async def cmd_back(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    buttons = ["📚Предметы📚", "💰Оплата💰", "❓Задать вопрос❓", "📋Внутренние гранты и скидки📋",
               "🏢Колледж ЕНТ Специальности🏢", "👨🏻‍🎓Специальности Магистратуры👨🏻‍🎓",
               "👨‍🔬Специальности Докторантуры👨‍🔬"]
    keyboard.add(*buttons)
    await message.answer("Здравствуйте, Коркыт Ата бот приветствует вас🙋‍♂️\nВыберите действие",
                         reply_markup=keyboard)


@dp.callback_query_handler(lambda call: call.data.split()[0] in ["phys_math","phys_chem","math_geo","bio_geo","chem_bio","geo_hist","geo_eng",
"hist_hsl","rulang_rulit","kzlang_kzlit","eng_hist"])
@dp.message_handler(lambda message: message.text in ["Биология-География", "География-Всемирная История", "География-Английский Язык",
               "Всемирная История-Человек.Общество.Право", "Казахский Язык-Казахская Литература", "Математика-Физика",
               "Математика-География", "Русский Язык-Русская Литература", "Химия-Биология",
               "Химия-Физика", "Английский Язык-Всемирная История", "Творческий экзамен"])
async def subject_balls(user_press):                                                    #subject : Если message то string, если callback то callback_data в англ версии ; year : int
    keys = ['phys_math', 'phys_chem', 'math_geo', 'bio_geo', 'chem_bio', 'geo_hist', 'geo_eng', 'hist_hsl', 'rulang_rulit', 'kzlang_kzlit', 'eng_hist']
    values = ['Математика-Физика', 'Химия-Физика', 'Математика-География', 'Биология-География', 'Химия-Биология', 'География-Всемирная История', 
    'География-Английский Язык', 'Всемирная История-Человек.Общество.Право', 'Русский Язык-Русская Литература', 'Казахский Язык-Казахская Литература','Английский Язык-Всемирная История']

    match(str(type(user_press))):
        case "<class 'aiogram.types.message.Message'>":
            subject_and_year = user_press.text.split()
            otvet = user_press.answer
        case "<class 'aiogram.types.callback_query.CallbackQuery'>":
            subject_and_year = user_press.data.split()
            subject_and_year[0] = values[keys.index(subject_and_year[0])]
            otvet = user_press.message.answer

    try: subject_and_year[1]                                            #Ставить этот год
    except IndexError:
        now = datetime.datetime.now()
        subject_and_year.insert(1, now.year - 1)

    data = db.subject_ball_from_bd(subject_and_year[0], int(subject_and_year[1]))           #Запрос на бд

    keyboard = types.InlineKeyboardMarkup(row_width=1)
    buttons = []
    for list_year in data[1]:
        buttons.append(types.InlineKeyboardButton(text=f"{str(list_year[0])[5:]} год", callback_data= keys[values.index(subject_and_year[0])] + ' ' + str(list_year[0])[5:]))
    keyboard.add(*buttons)
    await otvet(data[0],reply_markup=keyboard)

if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)