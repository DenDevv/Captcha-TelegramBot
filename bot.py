from config import bot
from app.handlers import commands
from app.handlers.new_chat_member_handler import captchas
from app.handlers.query_handler import query


bot.register_message_handler(commands.bot_settings, commands=['settings'])


@bot.message_handler(content_types=["new_chat_members"])
def messages(message):
    print(message.chat.id)

@bot.message_handler(content_types=["new_chat_members"])
def new_chat_member_handlers(message):
    captchas(message)


@bot.callback_query_handler(func=lambda call: True)
def query_handlers(call):
    query(call)

bot.polling(non_stop=True, interval=0)