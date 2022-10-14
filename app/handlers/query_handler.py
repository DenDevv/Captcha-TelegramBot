from config import bot, group
from app.database import db
from app.models import keyboards
from app.models.texts import (text_settings_change_lang_ua, 
                             text_settings_change_lang_en, 
                             text_settings_ua_lang, 
                             text_settings_en_lang, 
                             text_settings_menu_home_ua, 
                             text_settings_menu_home_en)


def query(call):
    user_id = call.from_user.id
    name = call.from_user.first_name

    try:
        if call.data == '1_2':
            if db.select_user(user_id):
                if db.select_lang()[0] == 'ua':
                    bot.restrict_chat_member(group, user_id, can_send_messages=True, can_add_web_page_previews=True, can_invite_users=True, can_send_media_messages=True, can_send_other_messages=True, can_send_polls=True, can_change_info=False, can_pin_messages=False)
                    bot.edit_message_text(chat_id=group, message_id=call.message.message_id, text=f'<b>{name}</b> пройшов капчу, ласкаво просимо до нашої групи!\n\nВисновок: <b>Людина</b> 👶🏻', parse_mode='html')
                    db.delete_user_into_table(user_id)

                if db.select_lang()[0] == 'en':
                    bot.restrict_chat_member(group, user_id, can_send_messages=True, can_add_web_page_previews=True, can_invite_users=True, can_send_media_messages=True, can_send_other_messages=True, can_send_polls=True, can_change_info=False, can_pin_messages=False)
                    bot.edit_message_text(chat_id=group, message_id=call.message.message_id, text=f'<b>{name}</b> passed captcha, welcome to our group!\n\nConclusion: <b>Human</b> 👶🏻', parse_mode='html')
                    db.delete_user_into_table(user_id) 
            
            else:
                if db.select_lang()[0] == 'ua':
                    bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text='⛔️ Це не ваша капча! ⛔️')

                if db.select_lang()[0] == 'en':
                    bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text='⛔️ This is not your captcha! ⛔️')

        elif call.data == 'off_on':
            if db.select_lang()[0] == 'ua':
                bot.edit_message_text(chat_id=group, message_id=call.message.message_id, text=f'{text_settings_change_lang_ua}{db.select_status()[0]}', reply_markup=keyboards.off_on_ua)

            if db.select_lang()[0] == 'en':
                bot.edit_message_text(chat_id=group, message_id=call.message.message_id, text=f'{text_settings_change_lang_en}{db.select_status()[0]}', reply_markup=keyboards.off_on_en)

        elif call.data == 'on':
            db.status_on()
            if db.select_lang()[0] == 'ua':
                bot.edit_message_text(chat_id=group, message_id=call.message.message_id, text=f'{text_settings_change_lang_ua}{db.select_status()[0]}', reply_markup=keyboards.off_on_ua)

            if db.select_lang()[0] == 'en':
                bot.edit_message_text(chat_id=group, message_id=call.message.message_id, text=f'{text_settings_change_lang_en}{db.select_status()[0]}', reply_markup=keyboards.off_on_en)

        elif call.data == 'off':
            db.status_off()
            if db.select_lang()[0] == 'ua':
                bot.edit_message_text(chat_id=group, message_id=call.message.message_id, text=f'{text_settings_change_lang_ua}{db.select_status()[0]}', reply_markup=keyboards.off_on_ua)

            if db.select_lang()[0] == 'en':
                bot.edit_message_text(chat_id=group, message_id=call.message.message_id, text=f'{text_settings_change_lang_en}{db.select_status()[0]}', reply_markup=keyboards.off_on_en)

        elif call.data == 'lang':
            if db.select_lang()[0] == 'ua':
                bot.edit_message_text(chat_id=group, message_id=call.message.message_id, text=f'{text_settings_ua_lang}', reply_markup=keyboards.languages_ua)

            if db.select_lang()[0] == 'en':
                bot.edit_message_text(chat_id=group, message_id=call.message.message_id, text=f'{text_settings_en_lang}', reply_markup=keyboards.languages_en)

        elif call.data == 'close':
            bot.delete_message(chat_id=group, message_id=call.message.message_id)
        
        elif call.data == 'back2':
            if db.select_lang()[0] == 'ua':
                bot.edit_message_text(chat_id=group, message_id=call.message.message_id, text=f'{text_settings_menu_home_ua}', reply_markup=keyboards.bot_settings_ua)

            if db.select_lang()[0] == 'en':
                bot.edit_message_text(chat_id=group, message_id=call.message.message_id, text=f'{text_settings_menu_home_en}', reply_markup=keyboards.bot_settings_en)

        elif call.data == 'back1':
            if db.select_lang()[0] == 'ua':
                bot.edit_message_text(chat_id=group, message_id=call.message.message_id, text=f'{text_settings_menu_home_ua}', reply_markup=keyboards.bot_settings_ua)

            if db.select_lang()[0] == 'en':
                bot.edit_message_text(chat_id=group, message_id=call.message.message_id, text=f'{text_settings_menu_home_en}', reply_markup=keyboards.bot_settings_en)

        elif call.data == 'ua':
            db.lang_ua()
            bot.edit_message_text(chat_id=group, message_id=call.message.message_id, text=f'{text_settings_ua_lang}', reply_markup=keyboards.languages_ua)

        elif call.data == 'en':
            db.lang_en()
            bot.edit_message_text(chat_id=group, message_id=call.message.message_id, text=f'{text_settings_en_lang}', reply_markup=keyboards.languages_en)

        else:
            if db.select_user(user_id):
                if db.select_lang()[0] == 'ua':
                    bot.edit_message_text(chat_id=group, message_id=call.message.message_id, text=f'🚷 <b>{name}</b> був забанений.\n\n❓ Причина: <b>Не пройшов капчу</b>\n\nВисновок: <b>БОТ</b> 🤖', parse_mode='html')
                    bot.ban_chat_member(group, user_id)
                    db.delete_user_into_table(user_id)

                if db.select_lang()[0] == 'en':
                    bot.edit_message_text(chat_id=group, message_id=call.message.message_id, text=f"🚷 <b>{name}</b> has been banned.\n\n❓ Reason: <b>Didn't pass the captcha</b>\n\nConclusion: <b>BOT</b> 🤖", parse_mode='html')
                    bot.ban_chat_member(group, user_id)
                    db.delete_user_into_table(user_id)

            else:
                if db.select_lang()[0] == 'ua':
                    bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text='⛔️ Це не ваша капча! ⛔️')

                if db.select_lang()[0] == 'en':
                    bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text='⛔️ This is not your captcha! ⛔️')
        
    except:
        pass