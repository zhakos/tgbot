import logging
import sqlite3

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
import db_request as db
import datetime
import all_buttons as bt
from subjects import register_handlers_subjects
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from aiogram.types import BotCommand
import config as conf

logger = logging.getLogger(__name__)


all_button = {'bkz': bt.subject_values_kz, 'bru': bt.subject_values_ru, 'mkz': bt.magistracy_buttons_kz,
              'mru': bt.magistracy_buttons_ru, 'dkz': bt.doctoranture_buttons_kz, 'dru': bt.doctoranture_buttons_ru,
              'ckz': bt.college_buttons_kz, 'cru': bt.college_buttons_ru, 'pkz': bt.subject_price_kz,
              'pru': bt.subject_price_ru}
lang = db.get_lang


# register_handlers_subjects(dp)

async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/kz", description="казак тилине кошу"),
        BotCommand(command="/ru", description="Изменить язык на русский"),
        BotCommand(command="/menu", description="Меню")
    ]
    await bot.set_my_commands(commands)


async def main():
    # Настройка логирования в stdout
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
    logger.error("Starting bot")

    # Парсинг файла конфигурации
    config = conf.load_config("bot.ini")

    # Объявление и инициализация объектов бота и диспетчера
    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher(bot, storage=MemoryStorage())
    register_handlers_subjects(dp)
    await set_commands(bot)
    await dp.start_polling()


# # GrantsAndDiscount
# @dp.callback_query_handler((lambda call: call.data in ['100%', '50%', '25%', '20%', '10%']))
# @dp.message_handler(lambda message: any(map(message.text.lower().__contains__, ['скидки', 'жеңілдік'])))
# async def cmd_menu_items(call):
#     buttons = bt.buttons_for_discount
#     keyboard = types.InlineKeyboardMarkup()
#     keyboard.add(*buttons)
#
#     match (str(type(call))):
#         case "<class 'aiogram.types.message.Message'>":
#             data = db.discount_drom_bd('100%', lang(call.from_user.id))
#             await call.answer(text=data, reply_markup=keyboard)
#         case "<class 'aiogram.types.callback_query.CallbackQuery'>":  # Если предыдущий текст равен тексту на замену ОШИБКА
#             data = db.discount_drom_bd(call.data, lang(call.from_user.id))
#             await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=data,
#                                         reply_markup=keyboard)
#             await bot.answer_callback_query(callback_query_id=call.id)


# Ask a Question
# @dp.message_handler(Text(contains="вопрос", ignore_case=True))
# async def cmd_ask_ques(message: types.Message):
#     buttons = [
#         types.InlineKeyboardButton(text="Напишите нам на WhatsApp", callback_data='100',
#                                    url='http://wa.me/+77029224458'),
#     ]
#     keyboard = types.InlineKeyboardMarkup()
#     keyboard.add(*buttons)
#     await message.answer("<a href='http://wa.me/+77029224458'><b>Напишите нам на WhatsApp</b></a>", parse_mode='html',
#                          reply_markup=keyboard)


# @dp.message_handler(lambda message: any(map(message.text.lower().__contains__, bt.subject_short_ru)) and not any(
#     map(message.text.lower().__contains__, ['-', 'экзамен', 'емтихан'])))
# async def cmd_all(message: types.message):
#     buttons = bt.button_from_short_subject(message.text)
#     keyboard = types.InlineKeyboardMarkup(row_width=1)
#     keyboard.add(*buttons)
#     match lang(message.from_user.id):
#         case "kz":
#             await message.answer("Бейіндік пәндерді таңдаңыз", reply_markup=keyboard)
#         case "ru":
#             await message.answer("Выберите один профильный предмет", reply_markup=keyboard)


if __name__ == "__main__":
    asyncio.run(main())
