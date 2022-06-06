from aiogram import types

short_subject_with_inline_button = [
    ['физ', [types.InlineKeyboardButton(text="Математика-Физика", callback_data='phys_math'),
             types.InlineKeyboardButton(text="Физика-Химия", callback_data='phys_chem')]],

    ['мат', [types.InlineKeyboardButton(text="Математика-Физика", callback_data='phys_math'),
             types.InlineKeyboardButton(text="Математика-География", callback_data='math_geo')]],

    ['хим', [types.InlineKeyboardButton(text="Физика-Химия", callback_data='phys_chem'),
             types.InlineKeyboardButton(text="Химия-Биология", callback_data='chem_bio')]],

    ['гео', [types.InlineKeyboardButton(text="Биология-География", callback_data='bio_geo'),
             types.InlineKeyboardButton(text="География-Всемирная История", callback_data='geo_hist'),
             types.InlineKeyboardButton(text="География-Английский", callback_data='geo_eng'),
             types.InlineKeyboardButton(text="Математика-География", callback_data='math_geo')]],

    ['био', [types.InlineKeyboardButton(text="Биология-География", callback_data='bio_geo'),
             types.InlineKeyboardButton(text="Химия-Биология", callback_data='chem_bio')]],

    ['истор', [types.InlineKeyboardButton(text="География-Всемирная История", callback_data='geo_hist'),
               types.InlineKeyboardButton(text="Всемирная История-Человек.Общество.Право", callback_data='hist_hsl')]],

    ['англ', [types.InlineKeyboardButton(text="Английский Язык-Всемирная История", callback_data='eng_hist'),
              types.InlineKeyboardButton(text="География-Английский", callback_data='geo_eng')]],

    ['русс', [types.InlineKeyboardButton(text="Русский Язык-Русская Литература", callback_data='rulang_rulit')]],

    ['казах', [types.InlineKeyboardButton(text="Казахский Язык-Казахская Литература", callback_data='kzlang_kzlit')]],

    ['человек чоп',
     [types.InlineKeyboardButton(text="Всемирная История-Человек.Общество.Право", callback_data='hist_hsl')]]]

def button_from_short_subject(message):
    for pair in short_subject_with_inline_button:
        if message in pair[0]:
            return pair[1]