import random

from time import sleep
from threading import Thread

from config import config
from app.utils import Keyboards
from app.database import CaptchaController


dev_config = config.get("development")
db = CaptchaController()
kb = Keyboards()


class CaptchaHandler:
    def new_chat_member(self, message, bot):
        user_id = message.new_chat_members[0].id
        name = message.new_chat_members[0].first_name
        group = message.chat.id

        if not all(db.get_group_params(group)):
            db.set_default_settings(group)

        lang = db.select_lang(group)

        if db.select_status(group) == 'on':

            if not db.get_user(user_id):
                db.new_user_captcha(user_id)

            bot.restrict_chat_member(group, user_id, can_send_messages=False)

            bot.send_message(
                group, 
                dev_config.settings[lang][9].format(
                    name, random.choice(kb.captcha_kb()[1])
                ), 
                reply_markup=kb.captcha_kb()[0]
            )

            Thread(target=self.check_captcha, args=[user_id, bot, name, group, message, lang], daemon=True).start()

    def check_captcha(self, user_id, bot, name, group, message, lang):
        sleep(15)

        if db.get_user(user_id):
            bot.delete_message(chat_id=group, message_id=message.message_id)
            bot.send_message(group, dev_config.settings[lang][8].format(name))

            db.delete_user_captcha(user_id)
            bot.ban_chat_member(group, user_id)