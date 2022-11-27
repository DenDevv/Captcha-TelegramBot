from time import sleep

from config import bot, group
from app.database import db
from app.models import keyboards


def captchas(message):
    user_id = message.new_chat_members[0].id
    name = message.new_chat_members[0].first_name
    
    try:
        if db.select_status()[0] == 'on':
            db.insert_user_into_table(user_id)
            bot.restrict_chat_member(group, user_id, can_send_messages=False)

            if db.select_lang()[0] == 'ua':
                bot.send_message(
                    group, 
                    f'Вітаємо тебе <b>{name}</b>, щоб переконатися, що ти не <b>робот</b> пройди перевірку.\n\nВибери емодзі: 👡\n\nУ тебе <b>15</b> секунд, поспішай!', 
                    reply_markup=keyboards.key, 
                    parse_mode='html'
                )

            if db.select_lang()[0] == 'en':
                bot.send_message(
                    group, 
                    f'Hello <b>{name}</b> to make sure that you are not a <b>robot</b> pass the test.\n\nChoose an emoji: 👡\n\nYou have <b>15</b> seconds, hurry up!', 
                    reply_markup=keyboards.key, 
                    parse_mode='html'
                )

            sleep(15)

            if db.select_user(user_id) is None:
                pass
            
            else:
                if db.select_lang()[0] == 'ua':
                    bot.delete_message(chat_id=group, message_id=message.message_id)
                    bot.send_message(chat_id=group, text=f'🚷 <b>{name}</b> був забанений.\n\n❓ Причина: <b>Не пройшов капчу</b>\n\nВисновок: <b>БОТ</b> 🤖', parse_mode='html')
                    db.delete_user_into_table(user_id)
                    bot.ban_chat_member(group, user_id)
                
                if db.select_lang()[0] == 'en':
                    bot.delete_message(chat_id=group, message_id=message.message_id)
                    bot.send_message(chat_id=group, text=f"🚷 <b>{name}</b> has been banned.\n\n❓ Reason: <b>Didn't pass the captcha</b>\n\nConclusion: <b>BOT</b> 🤖", parse_mode='html')
                    db.delete_user_into_table(user_id)
                    bot.ban_chat_member(group, user_id)
        else:
            pass

    except:
        pass
