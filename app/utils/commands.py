from app.database import CaptchaController
from app.utils import Keyboards

from config import config


dev_config = config.get("development")
db = CaptchaController()
kb = Keyboards()


class SettingsCommand:
    def __init__(self, bot) -> None:
        def bot_settings(message):
            group = message.chat.id

            if not db.get_group_params(group):
                db.set_default_settings(group)

            lang = db.select_lang(group)

            bot.send_message(
                group, 
                dev_config.settings[lang][0], 
                reply_markup=kb.bot_settings_kb(lang)
            )
        
        bot.register_message_handler(
            bot_settings,
            commands=['settings']
        )