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

def kafedra_KMAD(update, context):
    kb_start_kmad = [
        [InlineKeyboardButton('Викладачі', callback_data = 'vikladachi')],
        [InlineKeyboardButton('Відмінності кафедри', callback_data = 'vidminnosti_kafedri')],
        [InlineKeyboardButton('Історія кафедри', callback_data = 'istoria_kafedri')],
        [InlineKeyboardButton('Аудиторії кафедри', callback_data = 'auditorii_kafedri')],
        [InlineKeyboardButton('Наші випускники', callback_data = 'nashi_vipuskniki')]
    ]
    reply = InlineKeyboardMarkup(kb_start_kmad)
    update.message.reply_text('blah', reply_markup= reply)

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

    
#UMOVY_VSTUPU ФУНКЦИИ

def konk_pred_ZNO(update,context):
    update.callback_query.message.reply_text('Перший обов’язковий предмет — українська мова.\
                                            Другий обов’язковий предмет — математика.\
                                            Третій вибірковий предмет — історія України, іноземна мова, фізика, хімія, біологія, географія.\
                                            УВАГА! Абітурієнти кафедри КМАД здають документи до Приймальної комісії факультету комп’ютерних наук і програмної інженерії: \
                                            навчальний корпус У2, кімната 506, тел. +380(97)583-82-29.')

def pozp_konk_bal(update,context):
    update.callback_query.message.reply_text('Нижче формула  розрахунку твого конкурсного балу для вступу на нашу спеціальність.\
                                            Розрахування відбудеться автоматично у твоєму особистому кабінеті.\
                                            Але ми гадаємо, що тобі, як математику, важливо дізнатись, як все відбувається.\
                                            КБ= 0,2*П1+0,5*П2+0,3*П3\
                                            КБ — конкурсний бал.\
                                            П1, П2 — оцінювання першого (українська мова) та другого (математика) обов`язкових предметів.\
                                            П3 — оцінювання третього вибіркового предмета  (на вибір історія України, іноземна мова, фізика, хімія, біологія, географія).\
                                            УВАГА! Абітурієнти кафедри КМАД здають документи до Приймальної комісії факультету комп’ютерних наук і програмної інженерії:\
                                            навчальний корпус У2, кімната 506, тел.  +380(97) 583-82-29.')

def etap_vstup_komp(update,context):
    update.callback_query.message.reply_text('У цьому розділі розповімо, з яких етапів буде складатися твій вступ:\
                                            1.Реєстрація електронних кабінетів вступників — 01.07.\
                                            2.Початок приймання заяв та документів — 14.07.\
                                            3.Закінчення приймання заяв (на основі сертифікатів ЗНО) — 23.07 о 18:00.\
                                            4.Оприлюднення списку рекомендованих до зарахування вступників — за держ.замовленням – 28.07, за кошти фіз. та/або юр. осіб – до 10.08.\
                                            5.Виконання вимог до зарахування — за держ.замовленням 02.08 до 18:00.\
                                            6.Зарахування вступників — за держ.замовленням – 09.08 до 12:00, за кошти фізичних та/або юридичних осіб – до 30.09.\
                                            7.Переведення на вакантні місця державного замовлення осіб, які зараховані на навчання за кошти фізичних та/або юридичних осіб — до 19.08.\
                                            УВАГА! Абітурієнти кафедри КМАД здають документи до Приймальної комісії факультету комп’ютерних наук і програмної інженерії:\
                                            навчальний корпус У2, кімната 506, тел. +380(97) 583-82-29.')

def kor_pos(update,content):
    update.callback_query.message.reply_text('Тут зібрали для тебе усі корисні посилання, які допоможуть тобі під час вступу\
                                             Центральна приймальна комісія НТУ«ХПІ». http://vstup.kpi.kharkov.ua/ \
                                             «Правила прийому до Національного технічного університету “Харківський політехнічний інститут” у 2021 році» . http://vstup.kpi.kharkov.ua/admission/admission_rules/ \
                                              Українский центр оцінювання якості освіти https://testportal.gov.ua/ \
                                              Міністерство освіти та науки України. https://mon.gov.ua/ua \
                                              УВАГА! Абітурієнти кафедри КМАД здають документи до Приймальної комісії факультету комп’ютерних наук і програмної інженерії:\
                                              навчальний корпус У2, кімната 506, тел. +380(97) 583-82-29')

def mt_budj_kont_mt_vstup(update,context):
    update.callback_query.message.reply_text('Ця інформація буде цікавою для тебе, тому що ти полюбляєш будувати прогнози та вичислювати можливості, так? \
                                             Ліцензований обсяг на 1 курс денної форми навчання  у 2019-2020 н. р.  був 36 місць: \
                                             19 — держзамовлення, \
                                             17 — контракт.\
                                             Ліцензований обсяг на 1 курс денної форми навчання на 2021-2022 навчальний рік — 45 місць \
                                             Чекаємо на тебе!  \
                                             УВАГА! Абітурієнти кафедри КМАД здають документи до Приймальної комісії факультету комп’ютерних наук і програмної інженерії: \
                                             навчальний корпус У2, кімната 506, тел. +380(97) 583-82-29.') 


#EEEEEEEEEEEEEEEEEEEEEND......................

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

     #dfdua


    dp.add_handler(MessageHandler(Filters.text, echo))

    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
