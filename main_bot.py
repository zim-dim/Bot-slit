import logging
import configparser
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CallbackQueryHandler, CommandHandler, MessageHandler, Filters
'''
TOK = None
config = configparser.ConfigParser()
config.read('config.ini')
TOK = config['INFO']['token']
'''
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def KMAD(update, context):
    update.message.reply_text('a')

def importances(update, context):
    update.message.reply_text('b')

def conditions(update, context):
    update.message.reply_text('c')

def start(update, context):
    update.message.reply_text('Starting...')
    
    kb_start = [
        [InlineKeyboardButton('Кафедра', callback_data = 'kafedra_KMAD')],
        [InlineKeyboardButton('aaaaaaa', callback_data = 'moglyv_stud')],
        [InlineKeyboardButton('Умови вступу', callback_data = 'umovi_vstupu')]
    ]
    reply = InlineKeyboardMarkup(kb_start)
    update.message.reply_text('blah', reply_markup= reply)


def help(update, context):
    update.message.reply_text('Help!')

def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def echo(update, context):
    update.message.reply_text(update.message.text)

def kafedra_KMAD(update, context):
    update.callback_query.message.reply_text(' про кафедру')
    
def main():
    updater = Updater("1612051672:AAHr1oAA9dLdABLUJKgZ7mX0lgYj1cULjSg", use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CallbackQueryHandler( kafedra_KMAD  , pattern = 'kafedra_KMAD'))

    dp.add_handler(MessageHandler(Filters.text, echo))

    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
