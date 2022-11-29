import telebot
from config import config
from app.handlers import CaptchaHandler, CaptchaQueryHadnler
from app.utils import SettingsCommand


dev_config = config.get("development")
base_config = config.get("base")

# Create a database table
dev_config.Base.metadata.create_all(dev_config.engine)


class TelegramBot:
    def __init__(self) -> None:
        self.bot = telebot.TeleBot(base_config.BOT_TOKEN)
        self.bot.parse_mode = "html"
        SettingsCommand(self.bot)

        @self.bot.callback_query_handler(func=lambda call: True)
        def query_handlers(call):
            CaptchaQueryHadnler().query(call, self.bot)

        @self.bot.message_handler(content_types=["new_chat_members"])
        def new_chat_member_handlers(message):
            CaptchaHandler().new_chat_member(message, self.bot)

    def start(self):
        self.bot.infinity_polling()