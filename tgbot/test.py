from aiogram import types
text = 'физ'
checklist = {'физ', 'мат', 'хим', 'гео', 'био', 'истор', 'англ', 'русс', 'казах', 'человек', 'чоп'}
abd = [['физ',[types.InlineKeyboardButton(text="Математика-Физика", callback_data='phys_math'), types.InlineKeyboardButton(text="Физика-Химия", callback_data='phys_chem'),]],[],[]]
common_words = set(text.split()) & checklist


print(bool(common_words))
