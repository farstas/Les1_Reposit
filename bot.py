import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def start_bot(bot, update):
	mytext = '''Привет {}!

Я протой бот и понимаю только команду /start
	'''.format(update.message.chat.first_name)
	update.message.reply_text(mytext)

def chat(bot, update):
	text = update.message.text
	logging.info(text)
	print(text)
	update.message.reply_text(text)

def main():
	updtr = Updater('372869028:AAHOviCWh1OTpbYSN7okwwZ0rGSAIzITp6k')
	
	updtr.dispatcher.add_handler(CommandHandler('start', start_bot))
	updtr.dispatcher.add_handler(MessageHandler(Filters.text, chat))

	updtr.start_polling()
	updtr.idle()



if __name__=='__main__':
	logging.info('Bot started')
	main()



