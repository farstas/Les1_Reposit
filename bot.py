import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
dict = {}
import settings

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
					level=logging.INFO,
					filename='bot.log'
					)


def start_bot(bot, update):
	mytext = 'Привет {}! Я простой бот и понимаю только команду {}'.format(update.message.chat.first_name,'/start')
	logging.info('Пользователь {} нажал /start'.format(update.message.chat.username))
	update.message.reply_text(mytext)

def chat(bot, update):
	text = update.message.text
	chat_id = update.message.chat.id
	logging.info(text)

	if text in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '+', '-', '*', '/']:
		 if dict.get(chat_id) == None:
		 	dict[chat_id] = text
		 else:
		 	dict[chat_id] += text
		 	
	elif text == '=':
		clc = dict.get(chat_id)
		print(clc)
		#работа функции + del dict[chat_id]

	elif text == 'Esc':
		clear_keyboards(bot,chat_id)

	else:
		update.message.reply_text(text)

def wordcount_bot(bot, update, args):
	text= update.message.text
	print(text)
	user_text = text.split()
	user_text = [item for item in user_text if item not in ['?','!', '.', '.', ',', ':', ';', '*', '"']]
	
	update.message.reply_text(len(user_text)-1)
	print(len(user_text)-1)


def calculator_bot(bot, update, args):
	print(update.message.chat.id)
	custom_keyboard = [['1', '2', '3', '/'], ['4', '5', '6', '*'], ['7', '8', '9', '-'], ['Esc', '0', '+', '=']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.send_message(chat_id = update.message.chat.id, text = "Используйте кнопки калькулятора для расчета!", reply_markup = reply_markup)

def clear_keyboards(bot, userssss_id):
	reply_markup = telegram.ReplyKeyboardRemove(remove_keyboard=True)
	bot.send_message(chat_id = userssss_id, text = "Наберите новую команду: /start /calculator /wordcount", reply_markup = reply_markup)
	

def main():
	updtr = Updater(settings.TELEGRAM_API_KEY)
	
	updtr.dispatcher.add_handler(CommandHandler('start', start_bot))
	updtr.dispatcher.add_handler(MessageHandler(Filters.text, chat))
	updtr.dispatcher.add_handler(CommandHandler('wordcount', wordcount_bot, pass_args=True))
	updtr.dispatcher.add_handler(CommandHandler('calculator', calculator_bot, pass_args=True))

	updtr.start_polling()
	updtr.idle()



if __name__=='__main__':
	logging.info('Bot started')
	main()

