import random

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import config


dev_config = config.get("development")
settings = dev_config.settings


class Keyboards:
	def captcha_kb(self):
		random_e = [i for i in random.sample(dev_config.emojis, 6)]

		c_kb = InlineKeyboardMarkup(row_width=2)

		c_kb.row(
			InlineKeyboardButton(random_e[0], callback_data=random_e[0]),
			InlineKeyboardButton(random_e[1], callback_data=random_e[1]),
			InlineKeyboardButton(random_e[2], callback_data=random_e[2])
		)

		c_kb.row(
			InlineKeyboardButton(random_e[3], callback_data=random_e[3]),
			InlineKeyboardButton(random_e[4], callback_data=random_e[4]),
			InlineKeyboardButton(random_e[5], callback_data=random_e[5])
		)

		return c_kb, random_e

	def bot_settings_kb(self, lang):
		bot_settings = InlineKeyboardMarkup(row_width=2)

		bot_settings.row(
			InlineKeyboardButton(settings[lang][3], callback_data='off_on'),
			InlineKeyboardButton(settings[lang][4], callback_data='lang'),
			InlineKeyboardButton(settings[lang][5], callback_data='close')
		)

		return bot_settings

	def off_on_kb(self, lang):
		off_on = InlineKeyboardMarkup(row_width=2)

		off_on.row(
			InlineKeyboardButton(settings[lang][6][0], callback_data='on'),
			InlineKeyboardButton(settings[lang][6][1], callback_data='off'),
		)

		off_on.add(
			InlineKeyboardButton(settings[lang][7], callback_data='back')
		)

		return off_on

	def languages_kb(self, lang):
		languages = InlineKeyboardMarkup(row_width=2)

		languages.row(
			InlineKeyboardButton('Українська 🇺🇦', callback_data='ua'),
			InlineKeyboardButton('English 🇬🇧', callback_data='en')
		)

		languages.add(InlineKeyboardButton(settings[lang][7], callback_data='back'))

		return languages