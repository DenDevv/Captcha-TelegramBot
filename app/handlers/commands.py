from app.database import db
from app.models import texts
from app.models import keyboards

from config import bot, group


def bot_settings(message):
    try:
        db.insert_default_status()
        db.insert_default_lang()

        if db.select_lang()[0] == 'ua':
            bot.send_message(group, texts.text_settings_menu_home_ua, reply_markup=keyboards.bot_settings_ua)
        
        if db.select_lang()[0] == 'en':
            bot.send_message(group, texts.text_settings_menu_home_en, reply_markup=keyboards.bot_settings_en)
    except:
        pass