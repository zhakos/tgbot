from cgitb import text
import logging
from operator import contains
from re import IGNORECASE
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text


# Объект бота
bot = Bot(token="5332706447:AAH-GxB4NtiKUnW-6vKOBWVwfzBqhnPhctU")
# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

#////////////////////////Physic/////////////////////
@dp.message_handler(lambda message: 'физ' in message.text.lower())
async def cmd_phys_mat(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="Физика-Математика",callback_data='Физика-Математика'),
        types.InlineKeyboardButton(text="Физика-Химия",callback_data='Физика-Химия'),
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.reply("Выбери", reply_markup=keyboard)

#////////////////////////Math/////////////////////
@dp.message_handler(lambda message: 'мат' in message.text.lower())
async def cmd_phys_mat(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="Физика-Математика",callback_data='Физика-Математика'),
        types.InlineKeyboardButton(text="Математика-География",callback_data='Математика-География'),
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.reply("Выбери", reply_markup=keyboard)

#////////////////////////Biology/////////////////////
@dp.message_handler(lambda message: 'био' in message.text.lower())
async def cmd_phys_mat(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="Биология-География",callback_data='Биология-География'),
        types.InlineKeyboardButton(text="Химия-Биология",callback_data='Химия-Биология'),
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.reply("Выбери", reply_markup=keyboard)

#////////////////////////Chemistry/////////////////////
@dp.message_handler(lambda message: 'хим' in message.text.lower())
async def cmd_phys_mat(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="Химия-Физика",callback_data='Химия-Физика'),
        types.InlineKeyboardButton(text="Химия-Биология",callback_data='Химия-Биология'),
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.reply("Выбери", reply_markup=keyboard)

#////////////////////////Geography/////////////////////
@dp.message_handler(lambda message: 'гео' in message.text.lower())
async def cmd_phys_mat(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="Биология-География",callback_data='Биология-География'),
        types.InlineKeyboardButton(text="География-Всемирная история",callback_data='География-История мира'),
        types.InlineKeyboardButton(text="География-Английский",callback_data='География-Английский'),
        types.InlineKeyboardButton(text="Математика-География",callback_data='Математика-География'),
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.reply("Выбери", reply_markup=keyboard)

#////////////////////////History/////////////////////
@dp.message_handler(lambda message: 'ист' in message.text.lower()  or 'тар' in message.text.lower())
async def cmd_phys_mat(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="География-Всемирная история",callback_data='География-Всемирная история'),
        types.InlineKeyboardButton(text="Всемирная история-Человек.Общество.Право",callback_data='Всемирная история-Человек.Общество.Право')
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.reply("Выбери", reply_markup=keyboard)
    
#/////////////////Payment//////////////////
@dp.message_handler(contains="плата", ignore_case=True)
async def cmd_payment(message: types.Message):
    await message.answer('<b>Биология-География</b>\n "Педагогика и Психология" - 443.400 тг в год\n "."') 



@dp.message_handler(Text(startswith="прив", ignore_case=True))
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Физика-Математика", "География-Английский"]
    keyboard.add(*buttons)
    await message.answer("Выберите предметы", reply_markup=keyboard)









if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)