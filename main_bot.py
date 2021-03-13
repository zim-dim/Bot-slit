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


      
      ####
      


def start(update, context):
    update.message.reply_text('Starting...')
    
    kb_start = [
        [InlineKeyboardButton('Кафедра', callback_data = 'kafedra_KMAD')],
        [InlineKeyboardButton('aaaaaaa', callback_data = 'moglyv_stud')],
        [InlineKeyboardButton('Умови вступу', callback_data = 'umovi_vstupu')]
    ]
    reply = InlineKeyboardMarkup(kb_start)
    update.message.reply_text('blah', reply_markup= reply)

def kafedra_kmad(update, context):
    content ='З чого почнемо?'

    ####
    
    kaf_start=[
        [InlineKeyboardButton('Викладачі',callback_data='vykladach')],
        [InlineKeyboardButton('Відмінності кафедри',callback_data='vidmin_kaf')],
        [InlineKeyboardButton('Історія кафедри (фото)',callback_data='hist_kaf')],
        [InlineKeyboardButton('Аудиторії кафедри(фото)',callback_data='aud_kaf')],
        [InlineKeyboardButton('Наші випускники(Картинка с лого компаний как в ролике)',callback_data='n_vypuskniki')]
        ]
    replud = InlineKeyboardMarkup(kaf_start)

    update.callback_query.message.reply_text(content, reply_markup = replud)

def help(update, context):
    update.message.reply_text('Help!')

def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)
    
def umovy_vstupu(update, context):
    kb_start = [
                [InlineKeyboardButton('konk_pred_ZNO', callback_data = 'konk_pred_ZNO')],
                [InlineKeyboardButton('pozp_konk_bal', callback_data = 'pozp_konk_bal')],
                [InlineKeyboardButton('etap_vstup_komp', callback_data = 'etap_vstup_komp')],
                [InlineKeyboardButton('kor_pos', callback_data = 'kor_pos')],
                [InlineKeyboardButton('mt_budj_kont_mt_vstup', callback_data = 'mt_budj_kont_mt_vstup')],]
    reply = InlineKeyboardMarkup(kb_start)
    update.message.reply_text('Наши умови', reply_markup = reply)

    
    
#------------------KAFEDRA_KMAD ФУНКЦИИ----------------

def vykladach(update,context):
    content = 
    update.callback_query.message.reply_text(content, parse_mode="Markdown")

def vidmin_kaf(update,context):
    update.callback_query.message.reply_text()

def hist_kaf(update,context):
    update.callback_query.message.reply_text()

def aud_kaf(update,context):
    update.callback_query.message.reply_text()

def n_vypuskniki(update,context):
    update.callback_query.message.reply_text()
def prakt(update,context):
    update.callback_query.message.reply_text()
#------------------ end KAFEDRA_KMAD ФУНКЦИИ----------------

#----------------------------block umovy---------------------------
def proekt_nav(update, context):
    update.callback_query.message.reply_text('Проєктне навчання ')
    
def du_osvita(update, context):
    update.callback_query.message.reply_text('Дуальна освіта ')
    
def pracevl(update, context):
    update.callback_query.message.reply_text('Працевлаштування ')
    
def prakt(update, context):
    update.callback_query.message.reply_text('Практика ')

#---------------------------- end block umovy---------------------------

#EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEND......................
    
    
    
    
#UMOVY_VSTUPU ФУНКЦИИ

def konk_pred_ZNO(update,context):
    update.callback_query.message.reply_text()

def pozp_konk_bal(update,context):
    update.callback_query.message.reply_text()

def etap_vstup_komp(update,context):
    update.callback_query.message.reply_text()

def kor_pos(update,content):
    update.callback_query.message.reply_text()

def mt_budj_kont_mt_vstup(update,context):
    update.callback_query.message.reply_text() 


#EEEEEEEEEEEEEEEEEEEEEND......................

def echo(update, context):
    update.message.reply_text(update.message.text)

def kafedra_KMAD(update, context):
    update.callback_query.message.reply_text(' про кафедру')
    
def moglyv_stud(update, context):
    """Send a message when the command /start is issued."""
    #update.callback_query.message.reply_text('У нас є багато цікавих можливостей для студентів. З чого почнемо? ')
    
    kb_moglyv_stud = [[InlineKeyboardButton("Проєктне навчання",callback_data = "proekt_nav")],
               [InlineKeyboardButton("Дуальна освіта",callback_data = "du_osvita")],
               [InlineKeyboardButton("Працевлаштування",callback_data = "pracevl")],
               [InlineKeyboardButton("Практика",callback_data = "prakt")]]
    

    
    reply = InlineKeyboardMarkup(kb_moglyv_stud)
    
    update.callback_query.message.reply_text('У нас є багато цікавих можливостей для студентів. З чого почнемо?', reply_markup = reply)
'''
def about_of_CMAD_department(update, context):
    update.callback_query.message.reply_text()
def opportunties_for_the_student(update, context):
    update.callback_query.message.reply_text()
def conditions_of_entry(update, context):
    update.callback_query.message.reply_text()
def importances(update, context):
    update.message.reply_text('b')

def conditions(update, context):
    update.message.reply_text('c')
'''


    
def main():
    updater = Updater("1612051672:AAHr1oAA9dLdABLUJKgZ7mX0lgYj1cULjSg", use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CallbackQueryHandler( kafedra_KMAD  , pattern = 'kafedra_KMAD'))
    dp.add_handler(CallbackQueryHandler( umovy_vstupu  , pattern = 'umovy_vstupu'))
    dp.add_handler(CallbackQueryHandler(moglyv_stud, pattern = 'moglyv_stud'))
    
    #kafedra_kmad
    dp.add_handler(CallbackQueryHandler(vykladach,
                                        pattern ='vykladach'))

    dp.add_handler(CallbackQueryHandler(vidmin_kaf,
                                        pattern ='vidmin_kaf'))

    dp.add_handler(CallbackQueryHandler(hist_kaf,
                                        pattern ='hist_kaf'))

    dp.add_handler(CallbackQueryHandler(aud_kaf,
                                        pattern ='aud_kaf'))

    dp.add_handler(CallbackQueryHandler(n_vypuskniki,
                                        pattern ='n_vypuskniki'))

    
    dp.add_handler(CallbackQueryHandler(proekt_nav, pattern = 'proekt_nav'))
    dp.add_handler(CallbackQueryHandler(du_osvita, pattern = 'du_osvita'))
    dp.add_handler(CallbackQueryHandler(pracevl, pattern = 'pracevl'))
    dp.add_handler(CallbackQueryHandler(prakt, pattern = 'prakt'))
       
      #umovy_vstupu
    
    dp.add_handler(CallbackQueryHandler(konk_pred_ZNO,
                                        pattern ='konk_pred_ZNO'))
    dp.add_handler(CallbackQueryHandler(pozp_konk_bal,
                                        pattern ='pozp_konk_bal'))
    dp.add_handler(CallbackQueryHandler(etap_vstup_komp,
                                        pattern ='etap_vstup_komp'))
    dp.add_handler(CallbackQueryHandler(kor_pos,
                                        pattern ='kor_pos'))
    dp.add_handler(CallbackQueryHandler(mt_budj_kont_mt_vstup,
                                        pattern ='mt_budj_kont_mt_vstup'))
    
    '''
    dp.add_handler(CallbackQueryHandler(about_of_CMAD_department,
                                    pattern = 'about_of_CMAD_department'))
    dp.add_handler(CallbackQueryHandler(opportunties_for_the_student,
                                    pattern = 'opportunties_for_the_student'))
    dp.add_handler(CallbackQueryHandler(conditions_of_entry,
                                    pattern = 'conditions_of_entry'))
    ''' 
     #dfdua

      

    #djfdsfusdu

      

    dp.add_handler(MessageHandler(Filters.text, echo))

    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()
    
    dp.add_handler(CallbackQueryHandler(vykladach,
                                        pattern ='Викладачі'))

    dp.add_handler(CallbackQueryHandler(vidmin_kaf,
                                        pattern ='Відомості о Кафедрі'))

    dp.add_handler(CallbackQueryHandler(hist_kaf,
                                        pattern ='Історична Кафедра'))

    dp.add_handler(CallbackQueryHandler(aud_kaf,
                                        pattern ='Аудеторія Кафедри'))

    dp.add_handler(CallbackQueryHandler(n_vypuskniki,
                                        pattern ='Наші Випусники'))

if __name__ == '__main__':
    main()
