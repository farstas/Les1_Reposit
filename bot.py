import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
dict = {}
import settings

from win_unicode_console import enable
enable()

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
					level=logging.INFO,
					filename='bot.log'
					)


def start_bot(bot, update):
	print(update.message.chat.id)
	custom_keyboard = [['/calculator', '/Planets'], ['/Towns', 'Esc']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.send_message(chat_id = update.message.chat.id, text = "Нажмите интересующую вас опцию или Esc для выхода из меню", reply_markup = reply_markup)
	logging.info('Пользователь {} нажал /start'.format(update.message.chat.username))



def chat(bot, update):
	text = update.message.text
	chat_id = update.message.chat.id
	print(text)

	if text in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '+', '-', '*', '÷']:
		 if dict.get(chat_id) == None:
		 	dict[chat_id] = text
		 else:
		 	dict[chat_id] += text
		 			 			 	
	elif text == '=':
		clc = dict.get(chat_id)
		clc = clc.replace('*' , ' * ')
		clc = clc.replace('÷' , ' ÷ ')
		clc = clc.replace('+' , ' + ')
		clc = clc.replace('-' , ' - ')
		clc = clc.split()
		
		if clc[1] == '*':
			result = int(clc[0]) * int(clc[2])
			bot.send_message(chat_id, 'Результат вычисления: {} * {} = {}'.format(clc[0], clc[2], result))
			del dict[chat_id]
		elif clc[1] == '+':
			result = int(clc[0]) + int(clc[2])
			bot.send_message(chat_id, 'Результат вычисления: {} + {} = {}'.format(clc[0], clc[2], result))
			del dict[chat_id]
		elif clc[1] == '-':
			result = int(clc[0]) - int(clc[2])
			bot.send_message(chat_id, 'Результат вычисления: {} - {} = {}'.format(clc[0], clc[2], result))
			del dict[chat_id]
		elif clc[1] == '÷':
			try:
				result = int(clc[0]) / int(clc[2])
				bot.send_message(chat_id, 'Результат вычисления: {} / {} = {}'.format(clc[0], clc[2], result))
				del dict[chat_id]
			except (ZeroDivisionError):
				bot.send_message(chat_id, 'Ошибка деления на ноль. Проверьте корректность ввода данных!')
				del dict[chat_id]
		else:
			bot.send_message(chat_id, 'Проверьте корректность ввода данных для расчет!')
			del dict[chat_id]

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
	custom_keyboard = [['1', '2', '3', '÷'], ['4', '5', '6', '*'], ['7', '8', '9', '-'], ['/menu', '0', '+', '=']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	bot.send_message(chat_id = update.message.chat.id, text = "Используйте кнопки калькулятора для расчета!", reply_markup = reply_markup)

def clear_keyboards(bot, userssss_id):
	reply_markup = telegram.ReplyKeyboardRemove(remove_keyboard=True)
	bot.send_message(chat_id = userssss_id, text = "Для выхода в основное меню наберите команду: /menu", reply_markup = reply_markup)

	

def main():
	updtr = Updater(settings.TELEGRAM_API_KEY)
	
	updtr.dispatcher.add_handler(CommandHandler('menu', start_bot))
	updtr.dispatcher.add_handler(MessageHandler(Filters.text, chat))
	updtr.dispatcher.add_handler(CommandHandler('wordcount', wordcount_bot, pass_args=True))
	updtr.dispatcher.add_handler(CommandHandler('calculator', calculator_bot, pass_args=True))

	updtr.start_polling()
	updtr.idle()



if __name__=='__main__':
	logging.info('Bot started')
	main()

