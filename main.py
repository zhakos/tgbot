from cgitb import text
import logging
from operator import contains
from re import IGNORECASE
from tracemalloc import stop
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
import sqlite3
conn = sqlite3.connect('databases/subjects.db')
cur = conn.cursor()

# Объект бота
bot = Bot(token="5322427961:AAElTOBaFWlfxonWpzYRIO7TZK-JhtNuU0s")
# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)


# ////////////////////////Physic/////////////////////
@dp.message_handler(lambda message: 'физ' in message.text.lower() and '-' not in message.text.lower())
async def cmd_phys(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="Физика-Математика", callback_data='Физика-Математика'),
        types.InlineKeyboardButton(text="Физика-Химия", callback_data='Физика-Химия'),
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.reply("Выбери", reply_markup=keyboard)


# ////////////////////////Math/////////////////////
@dp.message_handler(lambda message: 'мат' in message.text.lower() and '-' not in message.text.lower())
async def cmd_math(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="Физика-Математика", callback_data='Физика-Математика'),
        types.InlineKeyboardButton(text="Математика-География", callback_data='Математика-География'),
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.reply("Выбери", reply_markup=keyboard)


# ////////////////////////Biology/////////////////////
@dp.message_handler(lambda message: 'био' in message.text.lower())
async def cmd_bio(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="Биология-География", callback_data='Биология-География'),
        types.InlineKeyboardButton(text="Химия-Биология", callback_data='Химия-Биология'),
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.reply("Выбери", reply_markup=keyboard)


# ////////////////////////Chemistry/////////////////////
@dp.message_handler(lambda message: 'хим' in message.text.lower())
async def cmd_chem(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="Химия-Физика", callback_data='Химия-Физика'),
        types.InlineKeyboardButton(text="Химия-Биология", callback_data='Химия-Биология'),
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.reply("Выбери", reply_markup=keyboard)


# ////////////////////////Geography/////////////////////
@dp.message_handler(lambda message: 'гео' in message.text.lower() and '-' not in message.text.lower())
async def cmd_geo(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="Биология-География", callback_data='Биология-География'),
        types.InlineKeyboardButton(text="География-Всемирная история", callback_data='География-История мира'),
        types.InlineKeyboardButton(text="География-Английский", callback_data='География-Английский'),
        types.InlineKeyboardButton(text="Математика-География", callback_data='Математика-География'),
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.reply("Выбери", reply_markup=keyboard)


# ////////////////////////History/////////////////////
@dp.message_handler(lambda message: 'ист' in message.text.lower() or 'тар' in message.text.lower())
async def cmd_hist(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="География-Всемирная история", callback_data='География-Всемирная история'),
        types.InlineKeyboardButton(text="Всемирная история-Человек.Общество.Право",
                                   callback_data='Всемирная история-Человек.Общество.Право')
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.reply("Выбери", reply_markup=keyboard)

#Добавь еще предметов а именно:English,CH.O.P,KAZlanguage,KAZliterature,RUSlanguage,RUSliterature,creativeexam

# /////////////////Payment//////////////////
@dp.message_handler(Text(contains="плата", ignore_case=True))
async def cmd_payment(message: types.Message):
    await message.answer('<b>Биология-География</b>\n "Педагогика и Психология" - 443.400 тг в год\n "',
                         parse_mode='html')


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    buttons = ["📚Предметы📚", "💰Оплата💰", "❓Задать вопрос❓", "📋Внутренние гранты и скидки📋",
               "🏢Колледж ЕНТ Специальности🏢", "👨🏻‍🎓Специальности Магистратуры👨🏻‍🎓"]
    keyboard.add(*buttons)
    await message.answer("Здравствуйте", reply_markup=keyboard)


@dp.message_handler(Text(contains="предметы", ignore_case=True))
async def cmd_items(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2,)
    buttons = ["Биология-География", "География-Всемирная История", "География-Английский",
               "Всемирная История-Человек.Общество.Право", "Казахский Язык-Казахская Литература", "Математика-Физика",
               "Математика-География", "Русский Язык-Русская Литература", "Химия-Биология",
               "Химия-Физика", "Английский Язык-Всемирная История", "Творческий экзамен", "🔄Назад🔄"]
    keyboard.add(*buttons)
    await message.answer("Выберите свои предметы", reply_markup=keyboard)

@dp.message_handler(Text(contains="назад", ignore_case=True))
async def cmd_back(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    buttons = ["📚Предметы📚", "💰Оплата💰", "❓Задать вопрос❓", "📋Внутренние гранты и скидки📋",
               "🏢Колледж ЕНТ Специальности🏢", "👨🏻‍🎓Специальности Магистратуры👨🏻‍🎓"]
    keyboard.add(*buttons)
    await message.answer("Здравствуйте", reply_markup=keyboard)


def request(message, year):
    cur.execute(f"SELECT groups.nomer, groups.name, year_{year}.grant, year_{year}.jk, year_{year}.ak FROM groups JOIN year_{year} ON groups.nomer = year_{year}.group_nomer WHERE groups.subject = '{message}' ORDER BY groups.nomer ASC;")
    data_groups = cur.fetchall()
    cur.execute(f"SELECT spec.group_nomer, spec.name FROM spec JOIN groups ON groups.nomer = spec.group_nomer WHERE subject = '{message}' ORDER BY spec.group_nomer ASC;")
    data_spec = cur.fetchall()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name > 'year_';")
    tables = cur.fetchall()
    text = ''
    for group in data_groups:
        group = list(group)
        text = text + f"<{group[1]}>\n"
        for spec in data_spec:
            spec = list(spec)
            if spec[0] == group[0]:
                text = text + "-" + spec[1] + "-\n"  #подумай
        text = text + f"Бакалавриатқа бөлінген грант саны:{group[2]}\nЖалпы конкурс бойынша грантқа түскен минималды балл:{group[3]}\nАуылдық квотамен грантқа түскен минималды балл:{group[4]}\n\n"
    return text,tables

@dp.callback_query_handler()
@dp.message_handler(lambda message: message.text in ["Биология-География", "География-Всемирная История", "География-Английский",
               "Всемирная История-Человек.Общество.Право", "Казахский Язык-Казахская Литература", "Математика-Физика",
               "Математика-География", "Русский Язык-Русская Литература", "Химия-Биология",
               "Химия-Физика", "Английский Язык-Всемирная История", "Творческий экзамен"])
async def from_bd_balls(subject: types.message, year = None):
    if not year:
        year = int(str(subject.date)[:4]) - 1
    data = request(subject.text, year)
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    buttons = []
    for year in data[1]:
        buttons.append(types.InlineKeyboardButton(text=f"{str(year[0])[5:]} год", callback_data=subject.text + ' ' + year[0]))
    keyboard.add(*buttons)
    await subject.answer(data[0],reply_markup=keyboard)

@dp.callback_query_handler(Text(contains='year_'))
async def year(call: types.CallbackQuery):
    data = call.data.split(' ')
    data[1] = int(str(data[1])[5:])
    await from_bd_balls(data[0],data[1])

if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)









#{"id":"4680207043138230388","from":{"id":1089695618,"is_bot":false,"first_name":"Zhako","language_code":"en"},"message":{"message_id":307,"from":{"id":5322427961,"is_bot":true,"first_name":"Idk","username":"Korkyt_assintant_bot"},"chat":{"id":1089695618,"first_name":"Zhako","type":"private"},"date":1654155682,"text":"tyu","reply_markup":{"inline_keyboard":[[{"text":"2020 год","callback_data":"hi"}],[{"text":"2021 год","callback_data":"hi"}]]}},"chat_instance":"-8721534746082330406","data":"hi"}