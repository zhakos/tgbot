from aiogram import types

buttons_ru = ["📚Предметы📚", "💰Оплата💰", "❓Задать вопрос❓", "📋Внутренние гранты и скидки📋",
              "🏢Колледж ЕНТ Специальности🏢", "👨🏻‍🎓Специальности Магистратуры👨🏻‍🎓", "👨‍🔬Специальности Докторантуры👨‍🔬"]
buttons_kz = ["📚Менің таңдау пәндерім📚", "💰2021 жылғы оқу ақысы💰", "❓Сұрағыңыз бар ма?❓",
              "📋Ішкі гранттар мен жеңілдіктер📋", "🏢Колледж - ҰБТ - Мамандықтары🏢", "👨🏻‍🎓Магистратура мамандықтары👨🏻‍🎓",
              "👨‍🔬Докторантура мамандықтары👨‍🔬"]

subject_short_ru = ['физ', 'мат', 'хим', 'гео', 'био', 'истор', 'англ', 'русс', 'казах', 'человек', 'чоп', 'твор',
                    'тарих', 'шет', 'орыс', 'қазақ', 'адам', 'аққ', 'шығарма']

subject_keys = ['phys_math', 'phys_chem', 'math_geo', 'bio_geo', 'chem_bio', 'geo_hist', 'geo_eng', 'hist_hsl', 'rulang_rulit',
        'kzlang_kzlit', 'eng_hist', 'crea_exam']

subject_values_ru = ['Математика-Физика', 'Химия-Физика', 'Математика-География', 'Биология-География', 'Химия-Биология',
          'География-Всемирная история', 'География-Английский язык', 'Всемирная история-Человек.Общество.Право',
          'Русский язык-русская литература', 'Казахский язык-Казахская литература', 'Английский язык-Всемирная история',
          'Творческий экзамен']

subject_values_kz = ['Математика-Физика', 'Химия-Физика', 'Математика-География', 'Биология-География', 'Химия-Биология',
          'География-Дүниежүзі тарихы', 'География-Шет тілі', 'Дүниежүзі тарихы-Адам.Қоғам.Құқық',
          'Орыс тілі-Орыс әдебиеті', 'Қазақ тілі-Қазақ әдебиеті', 'Шет тілі-Дүниежүзі тарихы',
          'Шығармашылық емтихан']

subject_price_ru = ['Математика-Физика', 'Химия-Физика', 'Математика-География', 'Биология-География', 'Химия-Биология',
          'География-Всемирная история', 'Всемирная история-Человек.Общество.Право',
          'Русский язык-русская литература', 'Казахский язык-Казахская литература', 'Английский язык-Всемирная история',
          'Творческий экзамен']

subject_price_kz = ['Математика-Физика', 'Химия-Физика', 'Математика-География', 'Биология-География', 'Химия-Биология',
          'География-Дүниежүзі тарихы', 'Дүниежүзі тарихы-Адам.Қоғам.Құқық',
          'Орыс тілі-Орыс әдебиеті', 'Қазақ тілі-Қазақ әдебиеті', 'Шет тілі-Дүниежүзі тарихы',
          'Шығармашылық емтихан']

magistracy_buttons_kz = ['Педагогикалық ғылымдар', 'Өнер және гуманитарлық ғылымдар', 'Бизнес, басқару және құқық',
                         'Жаратылыстану ғылымдары', 'математика и статистика', 'Ақпараттық-коммуникациялық технологиялар',
                         'Инженерлік', 'өңдеу және құрылыс салалары', 'Ауылшаруашылығы және биоресурстар',
                         'Қызмет көрсету']

magistracy_buttons_ru = ['Педагогические науки', 'Искусство и гуманитарные науки', 'Бизнес, управление и право',
                         'Естественные науки, математика и статистика', 'Информационно-коммуникационные технологии',
                         'Инженерные, обрабатывающие и строительные отрасли', 'Сельское хозяйство и биоресурсы',
                         'Услуги']

doctoranture_buttons_kz = ['Педагогикалық ғылымдар', 'Бизнес, басқару және құқық',
                           'Инженерлік, өңдеу және құрылыс салалары', 'Ауылшаруашылығы және биоресурстар']

doctoranture_buttons_ru = ['Педагогические науки', 'Бизнес, управление и право',
                           'Инженерные, обрабатывающие и строительные отрасли', 'Сельское хозяйство и биоресурсы']

college_buttons_kz = ['Педагогикалық ғылымдар', 'Өнер және гуманитарлық ғылымдар',
                      'Әлеуметтік ғылымдар, журналистика және ақпарат', 'Бизнес, басқару және құқық',
                      'Жаратылыстану ғылымдары, математика және статистика', 'Ақпараттық-коммуникациялық технологиялар',
                      'Инженерлік, өңдеу және құрылыс салалары', 'Ауыл шаруашылығы және биоресурстар', 'Қызмет көрсету']

college_buttons_ru = ['Педагогические науки', 'Искусство и гуманитарные науки',
                      'Социальные науки, журналистика и информация', 'Бизнес, управление и право',
                      'Естественные науки, математика и статистика', 'Информационно-коммуникационные технологии',
                      'Инженерные, обрабатывающие и строительные отрасли', 'Сельское хозяйство и биоресурсы', 'Услуги']

buttons_for_discount = [
        types.InlineKeyboardButton(text="100%", callback_data='100%'),
        types.InlineKeyboardButton(text="50%", callback_data='50%'),
        types.InlineKeyboardButton(text="25%", callback_data='25%'),
        types.InlineKeyboardButton(text="20%", callback_data='20%'),
        types.InlineKeyboardButton(text="10%", callback_data='10%'),
    ]


short_subject_with_inline_button = [
    ['физ', [types.InlineKeyboardButton(text="Математика-Физика", callback_data='phys_math'),
             types.InlineKeyboardButton(text="Физика-Химия", callback_data='phys_chem')]],

    ['мат', [types.InlineKeyboardButton(text="Математика-Физика", callback_data='phys_math'),
             types.InlineKeyboardButton(text="Математика-География", callback_data='math_geo')]],

    ['хим', [types.InlineKeyboardButton(text="Физика-Химия", callback_data='phys_chem'),
             types.InlineKeyboardButton(text="Химия-Биология", callback_data='chem_bio')]],

    ['гео', [types.InlineKeyboardButton(text="Биология-География", callback_data='bio_geo'),
             types.InlineKeyboardButton(text="География-Всемирная история", callback_data='geo_hist'),
             types.InlineKeyboardButton(text="География-Английский", callback_data='geo_eng'),
             types.InlineKeyboardButton(text="Математика-География", callback_data='math_geo')]],

    ['биоло', [types.InlineKeyboardButton(text="Биология-География", callback_data='bio_geo'),
             types.InlineKeyboardButton(text="Химия-Биология", callback_data='chem_bio')]],

    ['истор', [types.InlineKeyboardButton(text="География-Всемирная история", callback_data='geo_hist'),
               types.InlineKeyboardButton(text="Всемирная история-Человек.Общество.Право", callback_data='hist_hsl'),
               types.InlineKeyboardButton(text="Английский язык-Всемирная история", callback_data='eng_hist')]],

    ['англ', [types.InlineKeyboardButton(text="Английский язык-Всемирная история", callback_data='eng_hist'),
              types.InlineKeyboardButton(text="География-Английский", callback_data='geo_eng')]],

    ['русс', [types.InlineKeyboardButton(text="Русский язык-русская литература", callback_data='rulang_rulit')]],

    ['казах', [types.InlineKeyboardButton(text="Казахский язык-Казахская литература", callback_data='kzlang_kzlit')]],

    ['человек чоп',
     [types.InlineKeyboardButton(text="Всемирная история-Человек.Общество.Право", callback_data='hist_hsl')]],

    ['твор', [types.InlineKeyboardButton(text="Творческий экзамен", callback_data='crea_exam')]],

    ['тарих', [types.InlineKeyboardButton(text="География-Дүниежүзі тарихы", callback_data='geo_hist'),
               types.InlineKeyboardButton(text="Дүниежүзі тарихы-Адам.Қоғам.Құқық", callback_data='hist_hsl'),
               types.InlineKeyboardButton(text="Шет тілі-Дүниежүзі тарихы", callback_data='eng_hist')]],

    ['шет', [types.InlineKeyboardButton(text="Шет тілі-Дүниежүзі тарихы", callback_data='eng_hist'),
             types.InlineKeyboardButton(text="География-Шет тілі", callback_data='geo_eng')]],

    ['орыс', [types.InlineKeyboardButton(text="Орыс тілі-Орыс әдебиеті", callback_data='rulang_rulit')]],

    ['қазақ', [types.InlineKeyboardButton(text="Қазақ тілі-Қазақ әдебиеті", callback_data='kzlang_kzlit')]],

    ['адам аққ', [types.InlineKeyboardButton(text="Дүниежүзі тарихы-Адам.Қоғам.Құқық",
                                             callback_data='hist_hsl')]],

    ['шығарма', [types.InlineKeyboardButton(text="Шығармашылық емтихан", callback_data='crea_exam')]]]


def button_from_short_subject(message):
    for pair in short_subject_with_inline_button:
        if pair[0] in message.lower():
            return pair[1]
