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

      
      ####
      
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
    
def umovy_vstupu(update, context):
    kb_start = [
                [InlineKeyboardButton('konk_pred_ZNO', callback_data = 'konk_pred_ZNO')],
                [InlineKeyboardButton('pozp_konk_bal', callback_data = 'pozp_konk_bal')],
                [InlineKeyboardButton('etap_vstup_komp', callback_data = 'etap_vstup_komp')],
                [InlineKeyboardButton('kor_pos', callback_data = 'kor_pos')],
                [InlineKeyboardButton('mt_budj_kont_mt_vstup', callback_data = 'mt_budj_kont_mt_vstup')],]
    reply = InlineKeyboardMarkup(kb_start)
    update.message.reply_text('Наши умови', reply_markup = reply)

    
    
#KAFEDRA_KMAD ФУНКЦИИ

def vykladach(update,context):
    update.callback_query.message.reply_text('На кафедрі КМАД працюють:\
                                             7 професорів,\
                                             13 доцентів,\
                                             5 докторів технічних та фізико-математичних наук,\
                                             12 кандидатів технічних та фізико-математичних наук,\
                                             Засновник кафедри — лауреат Державної премії України, академік АН Вищої школи України, доктор технічних наук, професор — Любчик Леонід Михайлович\
                                             Завідувачка кафедри — доцентка, кандидатка технічних наук, професорка — Ахієзер Олена Борисівна\
                                             Щоб познайомитися з усіма викладачами, запрошуємо тебе на сторінку https://web.kpi.kharkov.ua/kmmm/uk/o_kafedre_ua/profesorsko-vikladatskij-sklad/')

def vidmin_kaf(update,context):
    update.callback_query.message.reply_text('Абревіатура «КМАД» розшифровується як «Комп’ютерна Математика і Аналіз Даних».\
                                            Кафедра КМАД готує бакалаврів та магістрів за освітньою програмою «Інтелектуальний аналіз даних».\
                                            Система така:\
                                            Спеціальність «Прикладна математика» → \
                                            освітня програма «Інтелектуальний аналіз даних» →\
                                            на виході професії програмувальника, інженера Big Data та Data Science, фахівця зі штучного інтелекту та машинного навчання, бізнес-аналітика та інші.\
                                            Важливо: з другого курсу студенти обирають вибірковий блок дисциплін для вузької спеціалізації.\
                                            «Інтелектуальний аналіз даних в обробці сигналів та зображень» або «Бізнес-аналіз, статистичний аналіз в економіці та фінансах». \
                                            Що ми маємо:\
                                            Базова фундаментальна математична освіта +\
                                            професійна комп’ютерна підготовка з технологій програмування та програмної інженерії +\
                                            спеціальна підготовка в галузі математичних методів та інформаційних технологій інтелектуального аналізу даних +\
                                            проєктне навчання +\
                                            дуальна освіта +\
                                            розвиток соціально-особистісних компетенцій (Soft Skills) +\
                                            англійська мова.\
                                            (Про «проєктне навчання» та «дуальну освіту» розповідаємо в інших розділах чат-боту)\
                                            Кафедра КМАД співпрацює з багатьма IT-компаніями України та із видатними вченими інших технічних університетів.')

def hist_kaf(update,context):
    update.callback_query.message.reply_text('(Фото в сториз инстаграм-аккаунта. Здесь превью)\
                                             Кафедра була створена у 2002 році. \
                                             Через рік будемо святкувати двадцятиріччя. \
                                             Сподіваємось, що вже разом із тобою!\
                                             З чого все почалося?\
                                             У 2002 році на базі факультету інформатики та управління створюється нова кафедра — \
                                             кафедра комп’ютерної математики і математичного моделювання.\
                                             Зараз відома як КМАД — комп’ютерна математика та аналіз даних.\
                                             З перших днів існування кафедру очолив відомий вчений і фахівець в галузі математичної теорії керування та математичного моделювання,\
                                             Лауреат Державної премії України, доктор технічних наук, професор Л.М. Любчик.\
                                             Задачею кафедри була математична підготовка студентів комп’ютерних та економічних спеціальностей.\
                                             Водночас на кафедру передається спеціальність «Прикладна математика».\
                                             Так ми стаємо першою математичною кафедрою в університеті, що випускає фахівців в цій галузі.\
                                             Отже, з початку була математика.\
                                             Через декілька років до математики приєдналась розробка програмних систем.\
                                             В результаті утворилась науково-навчальна концепція з підготовки математиків-програмістів.\
                                             Наші студенти в рівній мірі володіють методами прикладної математики й навичками створення комп’ютерних програм.\
                                             В процесі математика поєдналась із програмуванням.\
                                             У другому десятиріччі формується новий напрямок, пов’язаний з інтелектуальним аналізом даних на основі методів машинного навчання.\
                                             Кафедра стає однією з перших в Україні, яка створила освітню програму в області Data Science.\
                                             Зараз маємо фундаментальну математику, поєднану із програмуванням та посилену Data Science.\
                                             На кафедрі постійно проводяться наукові дослідження,\
                                             формується наукова школа в галузі математичних методів керування і прийняття рішень в умовах невизначеності.\
                                             Ми маємо фундаментальні наукові результати в області теорії обернених задач динаміки керованих систем,\
                                             компенсації невимірних збурень, розвитку сучасної теорії інваріантності.\
                                             На кафедрі виконані прикладні розробки щодо вдосконалення систем керування енергоблоками ТЕС і АЕС,\
                                             централізованою відпусткою тепла, моніторингу якості теплопостачання, систем керування каскадами водосховищ.\
                                             Ми маємо, чим пишатися. Запрошуємо тебе стати частиною цього світу!')

def aud_kaf(update,context):
    update.callback_query.message.reply_text('В инсте есть фото\
                                             Приміщення кафедри КМАД розташовані в корпусі факультету комп’ютерних наук і програмної інженерії (У-2) і в навчальному корпусі (У-5),\
                                             а також у навчальному філіалі ІТ компанії-партнера Cloud Works, район ст. м. «Проспект Гагаріна».\
                                             Загалом:\
                                             10 кафедральних аудиторій,\
                                             2 центри проєктного навчання в Cloud Works та NIX Solutions.\
                                             Аудиторії для лекцій та лабораторних робіт обладнані всією необхідною технікою та програмним забезпеченням.\
                                             У тому числі для дистанційних онлайн-лекцій, необхідність у яких виникає за потребою.\
                                             Також відмітимо, що все частіше наші аудиторії з’являються в офісах IT-компаній міста.\
                                             Під час дуальної освіти та проектного навчання, з якими ви можете ознайомитися на іншій вкладці.')

def n_vypuskniki(update,context):
    update.callback_query.message.reply_text('(Картинка в сториз)\
                                              Кафедра КМАД готує фахівців для високотехнологічних IT-компаній, зайнятих дослідженнями й розробками (R&D), для виконання наукомістких проєктів. \
                                              Ким працюють випускники кафедри КМАД:\
                                              - менеджери проектів,\
                                              - фахівці з аналізу даних,\
                                              - інженери Big Data, \
                                              - фахівці з обробки сигналів та зображень\
                                              - фахівці з машинного навчання та штучного інтелекту;\
                                              - програмісти \
                                              - тестувальники,\
                                              Де працюють наші випускники: Google, Facebook, Amazon, IBM, Samsung Electronics,\
                                              World Bank, Nix Solutions, Greed Dynamics, Global Logic, Sigma Software, Cloud Works та інших світових компаніях.\
                                              Можна їх фото та імена побачити на сторінці кафедри. http://web.kpi.kharkov.ua/kmmm/uk/o_kafedre_ua/nashi-vipuskniki/ \
                                              Ми дуже пишаємось тим, що маємо зв’язок із кожним випускником. Постійно спілкуємось та обмінюємось новинами. \
                                              Приєднуйся і ти до нас!')





#EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEND......................
    
    
    
    
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
    
def moglyv_stud(update, context):
    """Send a message when the command /start is issued."""
    #update.callback_query.message.reply_text('У нас є багато цікавих можливостей для студентів. З чого почнемо? ')
    
    kb_moglyv_stud = [[InlineKeyboardButton("Проєктне навчання",callback_data = "proekt_nav")],
               [InlineKeyboardButton("Дуальна освіта",callback_data = "du_osvita")],
               [InlineKeyboardButton("Працевлаштування",callback_data = "pracevl")],
               [InlineKeyboardButton("Практика",callback_data = "prakt")]]
    

    
    reply = InlineKeyboardMarkup(kb_moglyv_stud)
    
    update.callback_query.message.reply_text('У нас є багато цікавих можливостей для студентів. З чого почнемо?', reply_markup = reply)
def about_of_CMAD_department(update, context):
    update.callback_query.message.reply_text()
def opportunties_for_the_student(update, context):
    update.callback_query.message.reply_text()
def conditions_of_entry(update, context):
    update.callback_query.message.reply_text()
def proekt_nav(update, context):
    """Send a message when the command /start is issued."""
    update.callback_query.message.reply_text('Проєктне навчання ')
def du_osvita(update, context):
    """Send a message when the command /start is issued."""
    update.callback_query.message.reply_text('Дуальна освіта ')
def pracevl(update, context):
    """Send a message when the command /start is issued."""
    update.callback_query.message.reply_text('Працевлаштування ')
def prakt(update, context):
    """Send a message when the command /start is issued."""
    update.callback_query.message.reply_text('Практика ')
def main():
    updater = Updater("1612051672:AAHr1oAA9dLdABLUJKgZ7mX0lgYj1cULjSg", use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CallbackQueryHandler( kafedra_KMAD  , pattern = 'kafedra_KMAD'))
    dp.add_handler(CallbackQueryHandler( umovy_vstupu  , pattern = 'umovy_vstupu'))
    dp.add_handler(CallbackQueryHandler(moglyv_stud, pattern = 'moglyv_stud'))
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
    dp.add_handler(CallbackQueryHandler(about_of_CMAD_department,
                                    pattern = 'about_of_CMAD_department'))
    dp.add_handler(CallbackQueryHandler(opportunties_for_the_student,
                                    pattern = 'opportunties_for_the_student'))
    dp.add_handler(CallbackQueryHandler(conditions_of_entry,
                                    pattern = 'conditions_of_entry'))

     #dfdua

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


    #djfdsfusdu

      

    dp.add_handler(MessageHandler(Filters.text, echo))

    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
