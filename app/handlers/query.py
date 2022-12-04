from config import config
from app.database import CaptchaController
from app.utils import Keyboards


dev_config = config.get("development")
db = CaptchaController()
kb = Keyboards()


class CaptchaQueryHadnler:
    def query(self, call, bot):
        user_id = call.from_user.id
        name = call.from_user.first_name
        group = call.message.chat.id
        lang = db.select_lang(group)
        s_callbacks = ['off_on', 'on', 'off', 'lang', 'close', 'back', 'ua', 'en']

        if call.data not in s_callbacks:
            emoji = call.message.text.split("\n\n")[1][-1]
            if call.data == emoji:
                if db.get_user(user_id):
                    bot.restrict_chat_member(
                        group, 
                        user_id, 
                        can_send_messages=True, 
                        can_add_web_page_previews=True, 
                        can_invite_users=True, 
                        can_send_media_messages=True, 
                        can_send_other_messages=True, 
                        can_send_polls=True, 
                        can_change_info=False, 
                        can_pin_messages=False
                    )

                    bot.edit_message_text(
                        chat_id=group, 
                        message_id=call.message.message_id, 
                        text=dev_config.settings[lang][10]
                    )

                    db.delete_user_captcha(user_id)
                else:
                    bot.answer_callback_query(
                        callback_query_id=call.id, 
                        show_alert=True, 
                        text=dev_config.settings[lang][11].format(name)
                    )
                return

            else:
                if db.get_user(user_id):
                    bot.edit_message_text(
                        chat_id=group, 
                        message_id=call.message.message_id, 
                        text=dev_config.settings[lang][8].format(name)
                    )

                    db.delete_user_captcha(user_id)
                    bot.ban_chat_member(group, user_id)

                else:
                    bot.answer_callback_query(
                        callback_query_id=call.id, 
                        show_alert=True, 
                        text=dev_config.settings[lang][11]
                    )

        if call.data == 'off_on':
            bot.edit_message_text(
                chat_id=group, 
                message_id=call.message.message_id, 
                text=dev_config.settings[lang][2].format(db.select_status(group)),
                reply_markup=kb.off_on_kb(lang)
            )
            return

        if call.data in ['on', 'off']:
            db.set_status(call.data, group)

            bot.edit_message_text(
                chat_id=group, 
                message_id=call.message.message_id, 
                text=dev_config.settings[lang][2].format(db.select_status(group)),
                reply_markup=kb.off_on_kb(lang)
            )
            return

        if call.data == 'lang':
            bot.edit_message_text(
                chat_id=group, 
                message_id=call.message.message_id, 
                text=dev_config.settings[lang][1],
                reply_markup=kb.languages_kb(lang)
            )
            return

        if call.data == 'close':
            bot.delete_message(
                chat_id=group, 
                message_id=call.message.message_id
            )
            return

        if call.data == 'back':
            bot.edit_message_text(
                chat_id=group, 
                message_id=call.message.message_id, 
                text=dev_config.settings[lang][0],
                reply_markup=kb.bot_settings_kb(lang)
            )
            return

        if call.data in ['ua', 'en']:
            db.set_lang(call.data, group)

            try:
                bot.edit_message_text(
                    chat_id=group, 
                    message_id=call.message.message_id, 
                    text=dev_config.settings[call.data][1],
                    reply_markup=kb.languages_kb(call.data)
                )
            except:
                pass

            return