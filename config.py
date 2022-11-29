import os
import pytest
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))


@pytest.fixture
def drop_tables():
    TestingConfig.Base.metadata.drop_all(TestingConfig.engine)
    TestingConfig.Base.metadata.create_all(TestingConfig.engine)


class BaseConfig:
    """Base configuration."""

    BOT_TOKEN = os.environ.get("TOKEN")


class DevelopmentConfig:
    """Development configuration."""

    Base = declarative_base()
    Session = sessionmaker()
    engine = create_engine(
        "sqlite:///app/database/database.db?check_same_thread=False"
    )

    settings = {
        "ua": [
            'Налаштування Анти-Бота(Капчі) ⚙️',
            'Виберіть свою рідну мову.\n\nСтатус: ua',
            'Тут можна вимкнути/увімкнути бота\n\nСтатус: {0}',
            'Вимк./Увімк. 🤖',
            'Мова 🌏',
            'Закрити ❌',
            ['Увімк.🟢', 'Вимк.🔴'],
            'Назад',
            '🚷 <b>{0}</b> був забанений.\n\n❓ Причина: <b>Не пройшов капчу</b>\n\nВисновок: <b>БОТ</b> 🤖',
            '''Вітаємо тебе <b>{0}</b>, щоб переконатися, що ти не <b>робот</b> пройди перевірку.
\nВибери емодзі: {1}
\nУ тебе <b>15</b> секунд, поспішай!''',
            '<b>{name}</b> пройшов капчу, ласкаво просимо до нашої групи!\n\nВисновок: <b>Людина</b> 👶🏻',
            '⛔️ Це не ваша капча! ⛔️'
        ],
        "en": [
            'Anti-Bot(Captcha) settings ⚙️',
            'Please select your native language.\n\nStatus: en',
            'Here you can disable/enable the bot\n\nStatus: {0}',
            'Off/On 🤖',
            'Language 🌏',
            'Close ❌',
            ['On 🟢', 'Off 🔴'],
            'Back',
            '🚷 <b>{0}</b> has been banned.\n\n❓ Reason: <b>Didn\'t pass the captcha</b>\n\nConclusion: <b>BOT</b> 🤖',
            '''Hello <b>{0}</b> to make sure that you are not a <b>robot</b> pass the test.
\nChoose an emoji: {1}
\nYou have <b>15</b> seconds, hurry up!''',
            '<b>{name}</b> passed captcha, welcome to our group!\n\nConclusion: <b>Human</b> 👶🏻',
            '⛔️ This is not your captcha! ⛔️'
        ]
    }

    emojis = ["🌝", "👡", "💙", "📲", "🏸", "😛", "🎃", "😼", "👾", "🧠", "🧩"]


class TestingConfig:
    """Testing configuration."""

    Base = declarative_base()
    Session = sessionmaker()
    engine = create_engine(
        "sqlite:///app/database/test_db.db?check_same_thread=False"
    )


config = dict(
    base=BaseConfig,
    development=DevelopmentConfig, 
    testing=TestingConfig
)