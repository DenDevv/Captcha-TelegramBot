from telebot import types


key = types.InlineKeyboardMarkup(row_width=2)
key.row(types.InlineKeyboardButton('🌝', callback_data='1_1'),
         types.InlineKeyboardButton('👡', callback_data='1_2'),
         types.InlineKeyboardButton('💙', callback_data='1_3'))
key.row(types.InlineKeyboardButton('📲', callback_data='1_4'),
         types.InlineKeyboardButton('🏸', callback_data='1_5'),
         types.InlineKeyboardButton('😛', callback_data='1_6'))



bot_settings_ua = types.InlineKeyboardMarkup(row_width=2)
bot_settings_ua.row(types.InlineKeyboardButton('Вимк./Увімк. 🤖', callback_data='off_on'),
                types.InlineKeyboardButton('Мова 🌏', callback_data='lang'))
bot_settings_ua.add(types.InlineKeyboardButton('Закрити ❌', callback_data='close'))

off_on_ua = types.InlineKeyboardMarkup(row_width=2)
off_on_ua.row(types.InlineKeyboardButton('Увімк.🟢', callback_data='on'),
        types.InlineKeyboardButton('Вимк.🔴', callback_data='off'))
off_on_ua.add(types.InlineKeyboardButton('Назад', callback_data='back1'))

languages_ua = types.InlineKeyboardMarkup(row_width=2)
languages_ua.row(types.InlineKeyboardButton('Українська 🇺🇦', callback_data='ua'),
        types.InlineKeyboardButton('Русский 🇷🇺', callback_data='ru'),
        types.InlineKeyboardButton('English 🇬🇧', callback_data='en'))
languages_ua.add(types.InlineKeyboardButton('Назад', callback_data='back2'))


bot_settings_en = types.InlineKeyboardMarkup(row_width=2)
bot_settings_en.row(types.InlineKeyboardButton('Off/On 🤖', callback_data='off_on'),
                types.InlineKeyboardButton('Language 🌏', callback_data='lang'))
bot_settings_en.add(types.InlineKeyboardButton('Close ❌', callback_data='close'))

off_on_en = types.InlineKeyboardMarkup(row_width=2)
off_on_en.row(types.InlineKeyboardButton('On🟢', callback_data='on'),
        types.InlineKeyboardButton('Off🔴', callback_data='off'))
off_on_en.add(types.InlineKeyboardButton('Back', callback_data='back1'))

languages_en = types.InlineKeyboardMarkup(row_width=2)
languages_en.row(types.InlineKeyboardButton('Українська 🇺🇦', callback_data='ua'),
        types.InlineKeyboardButton('Русский 🇷🇺', callback_data='ru'),
        types.InlineKeyboardButton('English 🇬🇧', callback_data='en'))
languages_en.add(types.InlineKeyboardButton('Back', callback_data='back2'))