import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from telebot import types

# Token for the Telegram bot
token = 'Your_token_here'
bot = telebot.TeleBot(token)

# Dictionary to keep track of previous states
user_states = {}


# Handler for the /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = (
        """
Вітаємо👋  
Ми раді, що ти долучився до нашої НУБіП родини🤗 
Слідкуй за нами на офійційній сторінці університету https://nubip.edu.ua/
Ми в Інстаграм, скоріш підписуйся❤
https://www.instagram.com/nubip.1898?igsh=am8zZmU3YjRham9x
Дякуємо, що ти з нами, все буде Україна💙💛 
"""
    )
    bot.reply_to(message, welcome_text)

    # Create markup and buttons
    markup = InlineKeyboardMarkup()
    buttons_main = [
        InlineKeyboardButton("Кампус", callback_data='info_campus'),
        InlineKeyboardButton("Канали комунікації", callback_data='info_communicationchannels'),
        InlineKeyboardButton("Навчання", callback_data='study'),
        InlineKeyboardButton("Зразки заяв", callback_data='info_examples'),
        InlineKeyboardButton("Соціальне забезпечення", callback_data='info_benefits'),
        InlineKeyboardButton("Війскьовий облік", callback_data='info_militaryregistration'),
    ]

    for button in buttons_main:
        markup.add(button)

    bot.send_message(message.chat.id, "Яку інформацію ти хочеш дізнатися?", reply_markup=markup)


# Callback query handler
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    chat_id = call.message.chat.id
    user_state = user_states.get(chat_id, 'main_menu')

    if call.data == 'info_campus':
        user_states[chat_id] = 'main_menu'
        send_campus_info(call.message)
    elif call.data == 'back_to_main':
        send_main_menu(call.message)
    elif call.data == 'back_to_campus':
        send_campus_info(call.message)
    elif call.data == 'info_studybuildings':
        send_study_building(call.message)
    elif call.data == 'info_dormitories':
        send_dormitories_info(call.message)
    elif call.data == 'dormitories_menu':
        send_dormitories_info(call.message)
    elif call.data == 'info_availabledormitories':
        send_available_dormitories(call.message)
    elif call.data.startswith('info_') and 'campus' in user_state:
        send_submenu(call.message, call.data)
    elif call.data == 'info_communicationchannels':
        send_communication_channels(call.message)
    elif call.data == 'back_to_communication':
        send_communication_channels(call.message)
    elif call.data == 'info_maincommunication':
        send_main_communication(call.message)
    elif call.data == 'info_facultycommunication':
        send_faculty_communication(call.message)
    elif call.data == 'back_to_faculty_communication':
        send_faculty_communication(call.message)
    elif call.data == 'info_nni':
        send_nni_communication(call.message)
    elif call.data == 'info_basicfaculty':
        send_basic_faculty(call.message)
    elif call.data == 'info_removalfromregistrationsplace':
        send_removal_from_registration_place(call.message)
    elif call.data == 'info_removalmilitaryregistration':
        send_removal_from_military_registration(call.message)
    elif call.data == 'info_study':
        send_study_message(call.message)
    elif call.data == 'back_to_study':
        send_study_message(call.message)
    elif call.data == 'info_vstup':
        send_vstup_information(call.message)
    elif call.data == 'info_studygraph':
        send_study_graphic(call.message)
    elif call.data == 'info_schedule':
        send_schedule(call.message)
    elif call.data == 'info_studyportal':
        send_study_portal(call.message)
    elif call.data =='info_examples':
        send_zayavi_examples(call.message)
    elif call.data == 'info_benefits':
        send_social_benefits(call.message)
    elif call.data == 'back_to_social_benefits':
        send_social_benefits(call.message)
    elif call.data == 'info_academyscholarship':
        send_academy_scholarship(call.message)
    elif call.data == 'info_socialscholarship':
        send_social_scholarship(call.message)
    elif call.data == 'info_trasfertobudget':
        send_transfer_to_budget(call.message)
    elif call.data == 'info_benefitlivingindormitory':
        send_benefit_living_in_dormitory(call.message)
    elif call.data == 'info_militaryregistration':
        send_military_accounting(call.message)
    elif call.data == 'info_shelters':
        send_shelters(call.message)
    elif call.data == 'info_dinings':
        send_dinings(call.message)
    elif call.data == 'info_interestingplaces':
        send_interesting_places(call.message)
    elif call.data == 'info_benefitliving':
        send_benefit_living(call.message)
    elif call.data == 'info_mainpayment':
        send_main_payment(call.message)
    elif call.data == 'back_to_payment':
        send_main_payment(call.message)
    elif call.data == 'info_studypayment':
        send_study_payment(call.message)
    elif call.data == 'info_studypartpayment':
        send_part_payment(call.message)
    elif call.data == 'info_dormitorypayment':
        send_dormitory_payment(call.message)
    elif call.data == 'info_dormitorypartpayment':
        send_dormitory_part_payment(call.message)
    elif call.data == 'info_studentid':
        send_student_id_payment(call.message)
    elif call.data == 'info_zalikovka':
        send_zalikova_book(call.message)
    elif call.data == 'info_documents':
        send_documents(call.message)
    elif call.data == 'info_procedure':
        send_procedure(call.message)
    elif call.data == 'info_mainpayment':
        send_main_payment(call.message)


def send_main_menu(message):
    markup = InlineKeyboardMarkup()
    buttons_main = [
        InlineKeyboardButton("Кампус", callback_data='info_campus'),
        InlineKeyboardButton("Канали комунікації", callback_data='info_communicationchannels'),
        InlineKeyboardButton("Навчання", callback_data='info_study'),
        InlineKeyboardButton("Зразки заяв", callback_data='info_examples'),
        InlineKeyboardButton("Оплата", callback_data='info_mainpayment'),
        InlineKeyboardButton("Соціальне забезпечення", callback_data='info_benefits'),
        InlineKeyboardButton("Військовий облік", callback_data='info_militaryregistration'),
    ]

    for button in buttons_main:
        markup.add(button)

    bot.send_message(message.chat.id, "Яку інформацію ти хочеш дізнатися?", reply_markup=markup)


def send_campus_info(message):
    markup = InlineKeyboardMarkup()
    buttons_campus = [
        InlineKeyboardButton("Навчальні корпуси", callback_data='info_studybuildings'),
        InlineKeyboardButton("Гуртожитки", callback_data='info_dormitories'),
        InlineKeyboardButton("Укриття", callback_data='info_shelters'),
        InlineKeyboardButton("Їдальні", callback_data='info_dinings'),
        InlineKeyboardButton("Цікаві місця", callback_data='info_interestingplaces'),
        InlineKeyboardButton("Назад", callback_data='back_to_main')
    ]
    for button in buttons_campus:
        markup.add(button)
    bot.send_message(message.chat.id, """
🏛Кампус НУБіП України - це наше університетське містечко в Голосієво🌳🌲 , де ти отримаєш якісну освіту👨‍🎓👩‍🎓, нових друзів🤝 та багато позитивних емоцій та вражень🎉☀🌈         
    """, reply_markup=markup)


def send_communication_channels(message):
    markup = InlineKeyboardMarkup()
    buttons_communication = [
        InlineKeyboardButton("Загальні ", callback_data='info_maincommunication'),
        InlineKeyboardButton("ННІ/Факультети", callback_data='info_facultycommunication'),
        InlineKeyboardButton("Назад", callback_data='back_to_main'),
    ]
    for button in buttons_communication:
        markup.add(button)
    bot.send_message(message.chat.id, """
📣 Комунікація в НУБіП України - це ключ до твого успіху! 🤝 Спілкуйся з викладачами та одногрупниками, долучайся до студентського сенату, висловлюй свою думку та будь активним. Разом ми досягнемо більше! 🎓

    """, reply_markup=markup)

def send_main_communication(message):
    markup = InlineKeyboardMarkup()
    buttons_main_communication = [
        InlineKeyboardButton("Назад", callback_data='back_to_communication')
    ]
    for button in buttons_main_communication:
        markup.add(button)
    bot.send_message(message.chat.id, ("\n"
                                       "✅ Сайт університету: https://nubip.edu.ua/\n"
                                       "\n"
                                       "✅ Facebook сторінка університету: https://www.facebook.com/share/vkZnkcgYkyApreMA/?mibextid=LQQJ4d\n"
                                       " \n"
                                       "✅Instagram сторінка університету: https://www.instagram.com/nubip.1898?igsh=am8zZmU3YjRham9x\n"
                                       "\n"
                                       "✅Інстаграм ССО: https://www.instagram.com/sso.nubip1898?igsh=MW9veW05NTlsNHA3dA==\n"
                                       "\n"
                                       "✅ Телеграм канал NUBIP WORK: https://t.me/nules_work\n"
                                       "\n"
                                       "✅Телеграм канал НУБІП 1898 https://t.me/nubip1898 \n"
                                       "    "),reply_markup=markup)

def send_faculty_communication(message):
    markup = InlineKeyboardMarkup()
    buttons_main_communication = [
        InlineKeyboardButton("Навчально-наукові інститути:", callback_data='info_nni'),
        InlineKeyboardButton("Факультети базового закладу:", callback_data='info_basicfaculty'),
        InlineKeyboardButton("Назад", callback_data='back_to_communication')
    ]
    for button in buttons_main_communication:
        markup.add(button)
    bot.send_message(message.chat.id,"Обирай категорію",reply_markup=markup)

def send_nni_communication(message):
    markup = InlineKeyboardMarkup()
    buttons_nni_communication = [
        InlineKeyboardButton("🔗ННІ енергетики, автоматики і енергозбереження", url='https://nubip.edu.ua/structure/nni-eae'),
        InlineKeyboardButton("🔗ННІ лісового і садово-паркового господарства", url='https://nubip.edu.ua/structure/nni-lispg'),
        InlineKeyboardButton("🔗ННІ неперервної освіти і туризму", url='https://nubip.edu.ua/structure/nni-nt'),
        InlineKeyboardButton("Назад", callback_data='back_to_faculty_communication')
    ]
    for button in buttons_nni_communication:
        markup.add(button)
    bot.send_message(message.chat.id, """Який ННІ ти шукаєш?""",reply_markup=markup)

def send_basic_faculty(message):
    markup = InlineKeyboardMarkup()
    buttons_basic_faculty = [
        InlineKeyboardButton("🔗Аграрного менеджменту", url='https://nubip.edu.ua/structure/fam'),
        InlineKeyboardButton("🔗Агробіологічний", url='https://nubip.edu.ua/structure/abf'),
        InlineKeyboardButton("🔗Ветеринарної медицини", url='https://nubip.edu.ua/structure/fvm'),
        InlineKeyboardButton("🔗Гуманітарно-педагогічний", url='https://nubip.edu.ua/structure/gpf'),
        InlineKeyboardButton("🔗Економічний", url='https://nubip.edu.ua/structure/ef'),
        InlineKeyboardButton("🔗Захисту рослин, біотехнологій та екології", url='https://nubip.edu.ua/structure/zrbe'),
        InlineKeyboardButton("🔗Землевпорядкування:", url='https://nubip.edu.ua/structure/fzv'),
        InlineKeyboardButton("🔗Інформаційних технологій", url='https://nubip.edu.ua/structure/IT.NUBIP'),
        InlineKeyboardButton("🔗Конструювання та дизайну", url='https://nubip.edu.ua/structure/kd'),
        InlineKeyboardButton("🔗Механіко-технологічний факультет", url='https://nubip.edu.ua/structure/mtf'),
        InlineKeyboardButton("🔗Тваринництва та водних біоресурсів", url='https://nubip.edu.ua/structure/tvb'),
        InlineKeyboardButton("🔗Харчових технологій та управління якістю продукції АПК", url='https://nubip.edu.ua/structure/fht'),
        InlineKeyboardButton("🔗Юридичний", url='https://nubip.edu.ua/structure/law'),
        InlineKeyboardButton("Назад", callback_data='back_to_faculty_communication')
    ]
    for button in buttons_basic_faculty:
        markup.add(button)
    bot.send_message(message.chat.id, """Який факультет ти шукаєш?""", reply_markup=markup)

def send_dormitories_info(message):
    markup = InlineKeyboardMarkup()
    buttons_dormitories = [
        InlineKeyboardButton("Доступні гуртожитки для поселення", callback_data='info_availabledormitories'),
        InlineKeyboardButton("Зняття з місця реєстрації для жителів гуртожитку",callback_data='info_removalfromregistrationsplace'),
        InlineKeyboardButton("Зняття з військового обліку", callback_data='info_removalmilitaryregistration'),
        InlineKeyboardButton("Пільгове проживання", callback_data='info_benefitliving'),
        InlineKeyboardButton("Оплата частинами", callback_data='info_dormitorypartpayment'),
        InlineKeyboardButton("Перелік документів для поселення", callback_data='info_documents'),
        InlineKeyboardButton("Процедура поселення студентів у гуртожиток", callback_data='info_procedure'),
        InlineKeyboardButton("Назад", callback_data='back_to_campus')
    ]
    for button in buttons_dormitories:
        markup.add(button)
    bot.send_message(message.chat.id, """Оберіть пункт:""", reply_markup=markup)


def send_available_dormitories(message):
    markup = InlineKeyboardMarkup()
    buttons_dormitories = [
        InlineKeyboardButton("📍Гуртожиток 1", url='https://maps.app.goo.gl/e3DbbxvHv3uehSdVA'),
        InlineKeyboardButton("📍Гуртожиток 2", url='https://maps.app.goo.gl/LxZxkgeeqyCiP7Wg6'),
        InlineKeyboardButton("📍Гуртожиток 3", url='https://maps.app.goo.gl/3hGdywpLuhXSuY2j7'),
        InlineKeyboardButton("📍Гуртожиток 4", url='https://maps.app.goo.gl/ZSuPvoF4S956GSe3A'),
        InlineKeyboardButton("📍Гуртожиток 5", url='https://maps.app.goo.gl/kqXGQVJWwweLKTdz9'),
        InlineKeyboardButton("📍Гуртожиток 6", url='https://maps.app.goo.gl/sxMiFZAKFgqTnsjx9'),
        InlineKeyboardButton("📍Гуртожиток 7", url='https://maps.app.goo.gl/G7oiUw43sTFXC4Jx8'),
        InlineKeyboardButton("📍Гуртожиток 8", url='https://maps.app.goo.gl/DFFwKHK52PBbJ1Sb9'),
        InlineKeyboardButton("📍Гуртожиток 9", url='https://maps.app.goo.gl/5EZUW3NCJx3bneodA'),
        InlineKeyboardButton("📍Гуртожиток 10", url='https://maps.app.goo.gl/JYcuPmtiU7ZGYGnp6'),
        InlineKeyboardButton("📍Гуртожиток 11", url='https://maps.app.goo.gl/RyQuyzrkqdJ78gf69'),
        InlineKeyboardButton("Назад", callback_data='dormitories_menu')
    ]
    for buttons in buttons_dormitories:
        markup.add(buttons)
    bot.send_message(message.chat.id, """Оберіть пункт:""", reply_markup=markup)


def send_shelters(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Назад", callback_data='back_to_campus'))
    bot.send_message(message.chat.id, "Якщо у разі 📢 звучання сирен (сигнал оголошення повітряної тривоги) Ви перебували на вулиці або в навчальному корпусі, то необхідно відразу прямувати до найближчого укриття📍")
    with open('IMG_8784.png', 'rb') as photo2:
        bot.send_photo(message.chat.id, photo=photo2, reply_markup=markup)

def send_dinings(message):
    markup = InlineKeyboardMarkup()
    buttons_dinings = [
        InlineKeyboardButton("Центральна їдальня ", url='https://maps.app.goo.gl/xuT1zMHMRJr75wH96'),
        InlineKeyboardButton("Їдальня в корпусі № 3", url='https://maps.app.goo.gl/9kMM8MeF9GZGbG8E6'),
        InlineKeyboardButton("Їдальня в корпусі № 10 ", url='https://maps.app.goo.gl/Mcxzb1aPfEhwikUPA'),
        InlineKeyboardButton("Їдальня в корпусі № 11", url='https://maps.app.goo.gl/aCNeyDSABQSXpUk98'),
        InlineKeyboardButton("Буфети в корпусі № 1, № 2, № 4, № 12 ", url='https://maps.app.goo.gl/ojLYsWD5iDMcABkA8\n https://maps.app.goo.gl/kB5GTqvcfjUYRXnq8\n https://maps.app.goo.gl/tZaG4UQaXNTz5uaJ9\n https://maps.app.goo.gl/izuHFWUyw51HMuQE8 '),
        InlineKeyboardButton("Назад", callback_data='back_to_campus')
    ]
    for button in buttons_dinings:
        markup.add(button)
    bot.send_message(message.chat.id, ("\n"
                                       "🍽️ Запрошуємо вас відвідати наші заклади харчування, які працюють з понеділка по суботу з 8:00 до 17:00 🍽️\n"
                                       "На території нашого університету працюють їдальні:\n"
                                       "\n"
                                       "    "), reply_markup=markup)


def send_interesting_places(message):
    markup = InlineKeyboardMarkup()
    buttons_interestings = [
        InlineKeyboardButton("Ботанічний сад НУБіП – перлина садово-паркового мистецтва міста Києва", url='https://maps.app.goo.gl/pcuoRx3L8xyoRRmY7'),
        InlineKeyboardButton("Музей історії НУБіП України ", url='https://maps.app.goo.gl/Y8V2JaB92FLekYKM9'),
        InlineKeyboardButton("Алея Слави – вшанування видатних науковців, фундаторів аграрної освіти і науки ", url='https://maps.app.goo.gl/yBUsiU5xbqst1DEr6'),
        InlineKeyboardButton("Музей ґрунтів ім. проф. М.М. Годліна", url='https://maps.app.goo.gl/ViSaGiE5YvbJ4Ddi9'),
        InlineKeyboardButton("Музей лісових звірів та птахів ім. проф. О.О. Салганського ", url='https://maps.app.goo.gl/uMD7qP7MU3dtz7Dz5'),
        InlineKeyboardButton("Музей Анатомії НУБіП України", url='https://maps.app.goo.gl/hNk7TZfq81Teg8ceA'),
        InlineKeyboardButton("Музей грошей, банківської справи та страхування ", url='https://maps.app.goo.gl/CKxmXWWrmsNzCJDm7'),
        InlineKeyboardButton("Кафедра бджільництва та конярства", url='https://maps.app.goo.gl/aKYoMCN6QnKyVf979'),
        InlineKeyboardButton("Назад", callback_data='back_to_campus')
    ]
    for button in buttons_interestings:
        markup.add(button)
    bot.send_message(message.chat.id, ("\n"
                                       "Унікальність сучасного університетського кампусу НУБіП полягає у тому, що він знаходиться у Голосіївській лісопарковій зоні 🌳  – природній перлині столиці України .\n"
                                       "    "))
    with open("IMG_8785.png", 'rb') as photo4:
        bot.send_photo(message.chat.id, photo=photo4, reply_markup=markup)




def send_removal_from_registration_place(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Назад", callback_data='dormitories_menu'))
    bot.send_message(message.chat.id, ("\n"
                                       "👩‍💼 Дівчатам можна пройти зміну місця реєстрації в паспортному столі в гуртожитку.\n"
                                       "\n"
                                       "🧑‍💼 Для хлопців, що планують жити в гуртожитку і не мають статусу ВПО, для зняття з місця реєстрації треба:\n"
                                       "Замовити довідку про зарахування \n"
                                       "Дочекатися розподілу місць по гуртожитках\n"
                                       "Звернутися з довідкою про зарахування в військкомат для зняття з обліку\n"
                                       "Знятися з місця реєстрації в сервісному центрі \n"
                                       "Вказати дані для відправки документів - Голосіївський ТЦК та СП (військомат).\n"
                                       "\n"
                                       "УВАГА! СОЦІАЛЬНИМ КАТЕГОРІЯМ, ОСОБЛИВО ВПО ПЕРЕД ЗНЯТТЯМ З МІСЦЯ РЕЄСТРАЦІЇ І ПОСТАНОВКИ ЗВЕРНУТИСЯ В ДЕКАНАТ ЗА УТОЧНЕННЯМ АБО САМОСТІЙНО ПРОАНАЛІЗУВАТИ ЧИ НЕ ЗНИКНЕ ЇХ ПІЛЬГА ПРИ ЦІЙ ОПЦІЇ.\n"
                                       "\n"
                                       "    "), reply_markup=markup)

def send_removal_from_military_registration(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Назад", callback_data='dormitories_menu'))
    bot.send_message(message.chat.id, ("\n"
                                       "❗️Всі особи чоловічої статі незалежно від місця реєстрації мають подати свої документи в профільний відділ для постановки на облік та отримання довідки 20 про відстрочку,яку подати в свій військкомат до 1 жовтня за місцем реєстрації.❗️\n"
                                       "\n"
                                       "Крок 1. До початку навчання підготуйте та візьміть з собою:\n"
                                       "-сіра папка на завʼязках з вказаним своїм прізвищем, спеціальністю, роком вступу, телефоном, військомат  (де зареєстровані або плануєте бути зареєстрованим);\n"
                                       "-3 конверти з марками;\n"
                                       "-військово-обліковий документ 2 копії (військовий квиток або приписне) та оригінал  документу обов'язково;\n"
                                       "-паспорт 2 копії (id карта, навіть якщо прострочена);\n"
                                       "-довідка про реєстрацію місця проживання 2 копії/ або зняття;\n"
                                       "-картка платника податків 2 копії;\n"
                                       "-одне фото 3х4;\n"
                                       "\n"
                                       "Крок 2. В призначені деканатом день та місце (сповіщення в каналі деканату)\n"
                                       "-подайте вказані документи \n"
                                       "-заповніть заяви про постановку на облік\n"
                                       "-алфавітку два екземпляра \n"
                                       "-заповнюєте гугл форму https://docs.google.com/forms/d/e/1FAIpQLSek22yaxPpi4iBD78JAT95MhpwDoVdphx-fhht-DN9Dua50Ng/viewform \n"
                                       "Наказ про зарахування (деканат надасть в 1 тиждень навчання в каналі деканату) або його можна самостійно знайти на сайті https://nubip.edu.ua/node/6140 .\n"
                                       "\n"
                                       "Крок 3. Якщо успішно подані документи Вам нададуть протягом тижня довідку 20, яку ви:\n"
                                       "в разі не проживання в гуртожитку – забираєте і везете в військомат\n"
                                       "в разі проживання в гуртожитку та реєстрації – забираєте, робите копію довідки 20, пізніше понесете її паспортисту в гуртожиток, приписне оригінал та довідку 20 подаєте в спец. відділ (КОЛИ СКАЖЕ ДЕКАНАТ). У Голосіївський ТЦК та СП (військомат) ЖИТЕЛІ ГУРТОЖИТКУ ЧОЛОВІЧОЇ СТАТІ  після постановки на облік в університеті не йдуть! Режимно-мобілізаційний відділ буде їх ставити на облік централізовано. Така домовленість з Голосіївським ТЦК та СП!\n"
                                       "\n"
                                       "Крок 4. В разі проживання в гуртожитку та реєстрації – забираєте своє прописне після постановки на облік в Голосіївський ТЦК та СП (військомат), несете паспортисту в гуртожиток для завершення зміни реєсрації. Після реєстрації забираєте свій паспорт.\n"
                                       "\n"
                                       "ПРОФІЛЬНИЙ ВІДДІЛ 17 корпус 210-212 кабінет – Геннадій Миколайович РЖЕВСЬКИЙ, +380445278560\n"
                                       "\n"
                                       "    "),reply_markup=markup)


def send_benefit_living(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Назад", callback_data='dormitories_menu'))
    bot.send_message(message.chat.id, ("\n"
                                       " ❗️Для забезпечення пільгового проживання студентів окремих категорій у 2024-2025 навчальному році в гуртожитках студмістечка необхідно у двотижневий термін з моменту поселення у гуртожитки подати деканатам факультетів/дирекціям ННІ відповідні заяви з необхідними документами.\n"
                                       "\n"
                                       "   👩‍🎓Студенти, які вже отримували зазначену пільгу раніше, подають лише заяву, а всі інші-заяву з відповідним пакетом документів. Деканати факультетів/дирекції ННІ збирають заяви, зазначають в них дату та номер наказу, згідно якого студент поселений на поточний навчальний рік у гуртожиток і централізовано передають їх відділу соціальної роботи, який готує відповідний наказ.\n"
                                       " \n"
                                       "   📝 З переліком категорій студентів денної форми навчання (держзамовлення і контракт) та документів для надання їм пільги з оплати за проживання в гуртожитку, а також формою заяви можна ознайомитися на сайті НУБіП України у розділі «Студенту».\n"
                                       " \n"
                                       "   ❗️Що стосується студентів-сиріт та осіб з їх числа, то для пільгового проживання в гуртожитках вони також на тих же умовах мають подати до відділу соціальної роботи заяву, відповідно до своєї пільгової категорії.\n"
                                       "\n"
                                       "    "), reply_markup=markup)


def send_dormitory_part_payment(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Назад", callback_data='dormitories_menu'))
    bot.send_message(message.chat.id, ("\n"
                                       "❗️Почасткова оплата можлива лише за наявності пільг і виключно при погоджені заяви на оплату частинами (посеместрово) деканатом та профспілковою організацією студентів.\n"
                                       "👉🏻Детальніше про пільги: https://nubip.edu.ua/node/4743\n"
                                       "    "),reply_markup=markup)

def send_documents(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Назад", callback_data='dormitories_menu'))
    bot.send_message(message.chat.id, ("\n"
                                       "✅ копію паспорта (при наявності паспорта громадянина України старого зразку (в формі книжечки) 1,2 сторінки та місце реєстрації/зняття з реєстрації, студенти які мають паспорт в формі ID-картки роблять копію з двох сторін);\n"
                                       "✅ фотокартки розміром 3х4 (3 шт.);\n"
                                       "✅ довідку про проходження флюорографії та довідку про стан санітарно-епідеміологічного оточення дитини. Довідка надається сімейним лікарем, в якій вказується епідеміологічний стан дитини (наявність/відсутність педикульозу, шкірних захворювань, що протягом 21 дня не було контактів а людьми, які хворіють інфекційними хворобами та не перебуває на самоізоляції, тощо); \n"
                                       "✅ квитанцію про оплату за проживання в гуртожитку. Без наявності квитанції про оплату (оригінал або копія) за проживання у гуртожитку поселення студентів категорично забороняється. ЗА УМОВ ПІЛЬГ КОПІЇ ДОКУМЕНТІВ ПРО ПІЛЬГИ;\n"
                                       "✅ студенти чоловічої статі - приписне свідоцтво з відміткою про зняття з військового обліку за попереднім місцем проживання; \n"
                                       "\n"
                                       "\n"
                                       "📌 Вказати в приймальній комісії потребу в гуртожитку. Поселення пріоритетно поряд з своєю групою в одному гуртожитку, кімнаті, по 5-6 студентів.\n"
                                       "\n"
                                       "    "), reply_markup=markup)

def send_procedure(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Назад", callback_data='dormitories_menu'))
    bot.send_message(message.chat.id, """📎 Інформація щодо поселення студентів в гуртожитки студентського містечка НУБіП України: https://nubip.edu.ua/node/4743""", reply_markup=markup)


def send_study_building(message):
    markup = types.InlineKeyboardMarkup()
    buttons_building = [
        types.InlineKeyboardButton(text="🏫Навчальний Корпус 1", url="https://maps.app.goo.gl/ojLYsWD5iDMcABkA8"),
        types.InlineKeyboardButton(text="🏫Навчальний Корпус 2", url="https://maps.app.goo.gl/kB5GTqvcfjUYRXnq8"),
        types.InlineKeyboardButton(text="🏫Навчальний Корпус 3", url="https://maps.app.goo.gl/am69zC8bkacF94136"),
        types.InlineKeyboardButton(text="🏫Навчальний Корпус 4", url="https://maps.app.goo.gl/tZaG4UQaXNTz5uaJ9"),
        types.InlineKeyboardButton(text="🏫Навчальний Корпус 5", url="https://maps.app.goo.gl/caNjqZTrFe4v3AAi8"),
        types.InlineKeyboardButton(text="🏫Навчальний Корпус 6", url="https://maps.app.goo.gl/HDSGs4RfNj1Jx14D8"),
        types.InlineKeyboardButton(text="🏫Навчальний Корпус 7", url="https://maps.google.com?q=%D0%BA%D0%BE%D1%80%D0%BF%D1%83%D1%81%207%20%D0%9D%D0%A3%D0%91%D1%96%D0%9F%20%D0%A3%D0%BA%D1%80%D0%B0%D1%97%D0%BD%D0%B8,%20%D0%B2%D1%83%D0%BB%D0%B8%D1%86%D1%8F%20%D0%93%D0%B5%D1%80%D0%BE%D1%97%D0%B2%20%D0%9E%D0%B1%D0%BE%D1%80%D0%BE%D0%BD%D0%B8,%2012%D0%92,%20%D0%9A%D0%B8%D1%97%D0%B2,%2002000&ftid=0x40d4c8c0207d6815:0x440b25db283cbb5a&entry=gps&lucs=,94224825,94227247,94227248,47071704,47069508,94218641,94203019,47084304,94208458,94208447&g_st=com.google.maps.preview.copy"),
        types.InlineKeyboardButton(text="🏫Навчальний Корпус 7а", url="https://maps.app.goo.gl/RQLUJXYSwj8pwfaaA"),
        types.InlineKeyboardButton(text="🏫Навчальний Корпус 8", url="https://maps.app.goo.gl/5RtMz2vWLY1SX75A6"),
        types.InlineKeyboardButton(text="🏫Навчальний Корпус 9", url="https://maps.app.goo.gl/oduaKet9YSM4bCXB6"),
        types.InlineKeyboardButton(text="🏫Навчальний Корпус 10", url="https://maps.app.goo.gl/Mcxzb1aPfEhwikUPA"),
        types.InlineKeyboardButton(text="🏫Навчальний Корпус 11", url="https://maps.app.goo.gl/aCNeyDSABQSXpUk98"),
        types.InlineKeyboardButton(text="🏫Навчальний Корпус 12", url="https://maps.app.goo.gl/izuHFWUyw51HMuQE8"),
        types.InlineKeyboardButton(text="🏫Навчальний Корпус 15", url="https://maps.app.goo.gl/g1B4qDK5zSCq5uBN9"),
        types.InlineKeyboardButton(text="🏫Навчальний Корпус 17", url="https://maps.google.com?q=%D0%9D%D0%A3%D0%91%D1%96%D0%9F%20%D0%A3%D0%BA%D1%80%D0%B0%D1%97%D0%BD%D0%B8,%20%D0%BA%D0%BE%D1%80%D0%BF%D1%83%D1%81%20%E2%84%9617,%20%D0%A1%D1%96%D0%BB%D1%8C%D1%81%D1%8C%D0%BA%D0%BE%D0%B3%D0%BE%D1%81%D0%BF%D0%BE%D0%B4%D0%B0%D1%80%D1%81%D1%8C%D0%BA%D0%B8%D0%B9%20%D0%BF%D1%80%D0%BE%D0%B2%D1%83%D0%BB%D0%BE%D0%BA,%204,%20%D0%9A%D0%B8%D1%97%D0%B2,%2003041&ftid=0x40d4c8bfd6c8689d:0x2cfb4103a57e1191&entry=gps&lucs=,94224825,94227247,94227248,47071704,47069508,94218641,94203019,47084304,94208458,94208447&g_st=com.google.maps.preview.copy"),
        types.InlineKeyboardButton(text="Назад",callback_data='back_to_campus')
    ]
    for button in buttons_building:
        markup.add(button)
    bot.send_message(message.chat.id, ("\n"
                                       "    Щоб швидше знайти аудиторію, де проходить пара або ж необхідний підрозділ (ННІ/факультет) пропоную план-схему розташування корпусів НУБіП України \n"))
    with open('IMG_8786.png', 'rb') as photo4:
        bot.send_photo(message.chat.id, photo=photo4, reply_markup=markup)



def send_study_message(message):
    markup = InlineKeyboardMarkup()
    buttons_study = [
        InlineKeyboardButton("Вступ", callback_data='info_vstup'),
        InlineKeyboardButton("Графік освітнього процесу", callback_data='info_studygraph'),
        InlineKeyboardButton("Розклад навчальних занять", callback_data='info_schedule'),
        InlineKeyboardButton("Навчальний портал НУБіП України", callback_data='info_studyportal'),
        InlineKeyboardButton("Назад", callback_data='back_to_main')
    ]
    for button in buttons_study:
        markup.add(button)
    bot.send_message(message.chat.id, ("\n"
                                       " 📚 Навчання в НУБіП України - це захоплива подорож до нових знань і навичок! 🎓 Відвідуй лекції, семінари та лабораторні, де теорія зустрічається з практикою. Розкривай свої таланти, відкривай нові горизонти та готуйся до блискучої кар'єри! 🚀🌟\n"
                                       "    "),reply_markup=markup)

def send_vstup_information(message):
    markup = InlineKeyboardMarkup()
    button_backward = [
        InlineKeyboardButton("Назад", callback_data='back_to_study')
    ]
    for button in button_backward:
        markup.add(button)
    bot.send_message(message.chat.id, ("\n"
                                       "🔗 Накази на зарахування 🔗\n"
                                       "👇🏻 Ваш статус студента ви можете перевірити в кабінеті вступника (статус “до наказу”), а також відповідно до наказів про зарахування: https://nubip.edu.ua/node/6140\n"
                                       "👇🏻 За вашим запитом приймальна комісія може сформувати повідомлення про зарахування протягом тижня після підписаного відповідного наказу. Просимо заповнити форму для бажаючих: https://forms.gle/XinQTwSTupDnungN7  (Актуально це для подачі в школу,коледж, зміни місця реєстрації - Think about). Про готовність буде проінформовано на вказану вами у формі пошту.\n"
                                       "👇🏻 Терміни подачі документів та формування наказів на зарахування: https://nubip.edu.ua/node/8033\n"
                                       "\n"
                                       "\n"
                                       "💰Вартість навчання💰\n"
                                       "\n"
                                       "Переглянути вартість навчання на 2024-2025 навчальний рік можна тут: https://nubip.edu.ua/node/1660\n"
                                       "    "),reply_markup=markup)

def send_study_graphic(message):
    markup = InlineKeyboardMarkup()
    button_backward = [
        InlineKeyboardButton("Назад", callback_data='back_to_study')
    ]
    for button in button_backward:
        markup.add(button)
    bot.send_message(message.chat.id, ("\n"
                                       "📅 Орієнтована дата початку навчання 19.08.2024. \n"
                                       "За деталями слідкуй тут:\n"
                                       "https://nubip.edu.ua/node/23920 \n"
                                       "    "), reply_markup=markup)

def send_schedule(message):
    markup = InlineKeyboardMarkup()
    button_backward = [
        InlineKeyboardButton("Назад", callback_data='back_to_study')
    ]
    for button in button_backward:
        markup.add(button)
    bot.send_message(message.chat.id, ("\n"
                                       "🗓️ Розклад навчальних занять  доступний тут https://nubip.edu.ua/node/23920 та в каналі деканату \n"
                                       "    "),reply_markup=markup)

def send_study_portal(message):
    markup = InlineKeyboardMarkup()
    button_backward = [
        InlineKeyboardButton("Назад", callback_data='back_to_study')
    ]
    for button in button_backward:
        markup.add(button)
    bot.send_message(message.chat.id, ("\n"
                                       "💻 Шановні вступники! Протягом першого тижня після зарахування кожному з вас буде створено логін і пароль для доступу до https://elearn.nubip.edu.ua/, де будуть розміщені навчальні матеріали та завдання для виконання.\n"
                                       "Про облікові дані повідомить вас деканат або на 1 занятті з дисциплін.\n"
                                       "\n"
                                       "    "),reply_markup=markup)



def send_zayavi_examples(message):
    markup = InlineKeyboardMarkup()
    buttons_examples = [
        InlineKeyboardButton("📝 Зразок заяви на призначення соціальної стипендії  ", url='https://nubip.edu.ua/sites/default/files/u101/zrazok_zayavi_2023.docx'),
        InlineKeyboardButton("📝 Зразок заяви на пільгове проживання у гуртожиток ", url ='https://nubip.edu.ua/sites/default/files/u101/zayavi_na_pilgove_prozhivannya_u_gurtozhitok-2022.docx'),
        InlineKeyboardButton("📝 Зразок заяви на звільнення від оплати за проживання дітей-сиріт", url='https://nubip.edu.ua/sites/default/files/u331/zrazok_zayavi_na_zvilnennya_vid_oplati_sirit_za_prozhivannya_v_gurt.docx'),
        InlineKeyboardButton("Назад", callback_data='back_to_main')
    ]
    for button in buttons_examples:
        markup.add(button)
    bot.send_message(message.chat.id, ("\n"
                                       "📋Заповнюй усі заяви вчасно,⏰ і памʼятай, що вони є доступними на сайті університету🧑‍💻 або в деканаті твого факультету!📋\n"
                                       "    "),reply_markup=markup)

def send_main_payment(message):
    markup = InlineKeyboardMarkup()
    buttons_payment = [
        InlineKeyboardButton("Навчання", callback_data='info_studypayment'),
        InlineKeyboardButton("Оплата частинами", callback_data='info_studypartpayment'),
        InlineKeyboardButton("Гуртожиток",callback_data='info_dormitorypayment'),
        InlineKeyboardButton("Студентський квиток ", callback_data='info_studentid'),
        InlineKeyboardButton("Залікова книжка", callback_data='info_zalikovka'),
        InlineKeyboardButton("Назад", callback_data='back_to_main')
    ]
    for button in buttons_payment:
        markup.add(button)
    bot.send_message(message.chat.id, ("\n"
                                       "💰В процесі навчання в НУБіП України тобі доведеться стикатися з питаннями оплати💶: оплата за навчання📚, за проживання в гуртожитку🏡 та інші платежі. Всю інформацію про строки та способи оплати можна знайти на сайті університету🎓📅\n"
                                       "    "),reply_markup=markup)

def send_study_payment(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Назад", callback_data='back_to_payment'))
    bot.send_message(message.chat.id, ("\n"
                                       "❗️Всі вступники,які будуть навчатися за кошти фіз. осіб (контракт), мають здійснити оплату за навчання ЗА СЕМЕСТР, екзаменаційну книжку і студ.квиток та  надіслати квитанції в деканат ❗️\n"
                                       "\n"
                                       "🔹 СУМИ ЗА НАВЧАННЯ (для оплати за семестр розділити річну суму на 2) https://nubip.edu.ua/node/1660\n"
                                       "\n"
                                       "🖇️Реквізити для оплати за навчання:\n"
                                       "Одержувач: Національний університет біоресурсів і природокористування України\n"
                                       "Адреса: 03041, м. Київ, вул. Героїв Оборони, 15\n"
                                       "IBAN: UA088201720313211002201016289\n"
                                       "Банк: ДКСУ м. Київ\n"
                                       "ЄДРПОУ: 00493706\n"
                                       "П.І.Б.\n"
                                       "Факультет ___\n"
                                       "\n"
                                       "ОБОВ’ЯЗКОВА ДЛЯ ЗАПОВНЕННЯ КОНТРАКТНИКАМ  форма для надсилання квитанцій про оплату в деканат:????   https://forms.gle/jkszFHnzApfqwZSh9  \n"
                                       "\n"
                                       "\n"
                                       "\n"
                                       "👉🏻Договори після підписання буде передано в деканат, співробітники проінформують про можливість отримання.\n"
                                       "\n"
                                       "🔹Здійснити оплату за навчання необхідно до початку навчання. За необхідності до початку навчання прийти і написати заяву на часткову оплату в деканат факультету.\n"
                                       "🔹Замовники освітніх послуг на підставі квитанцій та договору можуть відшкодувати до 15% за податковою знижкою❗️.\n"
                                       "\n"
                                       "☺️ p.s. Вступники за кошти Бюджету отримують залікову книжку і студ квиток безкоштовно на початку навчання!  \n"
                                       "\n"
                                       "    "), reply_markup=markup)

def send_part_payment(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Назад", callback_data='back_to_payment'))
    bot.send_message(message.chat.id, ("Деталі щодо оплати за навчання в семестрі частинами?????? https://docs.google.com/document/d/15f5oFoeN5lPgtbILpJov1x-l4ynAfbJE-QQkgsvVILo/edit?usp=sharing"),reply_markup=markup)

def send_dormitory_payment(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Назад", callback_data='back_to_payment'))
    bot.send_message(message.chat.id, ("\n"
                                       "🏡 Гуртожиток — це місце, де студент може знайти нових друзів і відчути студентське життя👫🎈. Тут створені умови для проживання, навчання і відпочинку, що сприяють успішній адаптації до університетського середовища🔑.\n"
                                       "\n"
                                       "🖇️ Реквізити для оплати за проживання в гуртожитках:\n"
                                       "Одержувач: Національний університет біоресурсів і природокористування України\n"
                                       "Адреса: 03041, м. Київ, вул. Героїв Оборони, 15\n"
                                       "Телефон: 527-81-92\n"
                                       "IBAN: UA338201720313281002202016289\n"
                                       "Банк: ДКСУ м. Київ\n"
                                       "ЄДРПОУ: 00493706\n"
                                       "Призначення платежу: за проживання в гуртожитку № ___ (вказати гурт., в якому буде проживати) П.І.Б. (вказувати повністю ініціали студента, який проживатиме в гурт.), факультет ___\n"
                                       "\n"
                                       "✅ Вартість проживання: 8810 грн за навчальний рік  (19.08.2024-18.07.2025)\n"
                                       "\n"
                                       "    "),reply_markup=markup)

def send_student_id_payment(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Назад", callback_data='back_to_payment'))
    bot.send_message(message.chat.id, ("\n"
                                       "🪪 Студентський квиток державного зразка - документ, що містить персональні дані про студента, який може бути використаний для ідентифікації особи, підтвердження права на пільгу проїзду пасажира в міському 🚎 та залізничному 🚊 транспорті.\n"
                                       "\n"
                                       "🖇️Реквізити для оплати студентського квитка тільки для контрактників:\n"
                                       "Одержувач: Національний університет біоресурсів і природокористування України\n"
                                       "Адреса: м.Київ, вул.Героїв Оборони, 15\n"
                                       "Розрахунковий рахунок: Nº31254225216289\n"
                                       "IBAN: UA338201720313281002202016289\n"
                                       "Банк: ДКСУ м.Київ\n"
                                       "Код банку: 820172\n"
                                       "ЄДРПОУ: 00493706\n"
                                       "Призначення платежу: код 16.03.01.03.01- за студентський квиток\n"
                                       "П.I.Б.\n"
                                       "Факультет ___\n"
                                       "\n"
                                       "👉🏻 Інструкція з використання студентського квитка детально на сайті:\n"
                                       "https://nubip.edu.ua/node/114887 \n"
                                       "\n"
                                       "❗️Перевірка активності студ квитка: https://info.edbo.gov.ua/student-tickets/❗️\n"
                                       "\n"
                                       "    "),reply_markup=markup)

def send_zalikova_book(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Назад", callback_data='back_to_payment'))
    bot.send_message(message.chat.id, ("\n"
                                       "📘 Залікова книжка — важливий документ для кожного першокурсника. Вона фіксує всі складені іспити та заліки, відображаючи успіхи студента✔️. Ведення залікової книжки допомагає слідкувати за навчальним прогресом📈 і може впливати на отримання стипендії чи переведення на наступний курс🎊.\n"
                                       "\n"
                                       "🖇️Реквізити для оплати залікової книжки тільки для контрактників: \n"
                                       "Одержувач: Національний університет біоресурсів і природокористування України\n"
                                       "Адреса: 03041, м.Київ, вул.Героїв Оборони, 15\n"
                                       "Телефон: 527-81-92\n"
                                       "Розрахунковий рахунок: Nº31254225216289\n"
                                       "IBAN: UA338201720313281002202016289\n"
                                       "Банк: ДКСУ м. Київ\n"
                                       "Код банку: 820172\n"
                                       "ЄДРПОУ: 00493706\n"
                                       "Особовий рахунок: 25.13\n"
                                       "Призначення платежу: за залікову книжку\n"
                                       "П.І.Б.\n"
                                       "Факультет ___\n"
                                       "\n"
                                       "    "),reply_markup=markup)




def send_social_benefits(message):
    markup = InlineKeyboardMarkup()
    buttons_social = [
        InlineKeyboardButton("Академічна стипендія", callback_data='info_academyscholarship'),
        InlineKeyboardButton("Соціальна стипендія", callback_data='info_socialscholarship'),
        InlineKeyboardButton("Переведення на бюджет", callback_data="info_trasfertobudget"),
        InlineKeyboardButton("Пільгове проживання в гуртожитку", callback_data='info_benefitlivingindormitory'),
        InlineKeyboardButton("Назад", callback_data='back_to_main')
    ]
    for button in buttons_social:
        markup.add(button)
    bot.send_message(message.chat.id, ("\n"
                                       "У НУБіП України студенти мають можливість отримати стипендії 💷, гранти🎁, медичне обслуговування💊 та участь у культурних заходах. Це допомагає забезпечити комфортне навчання та повноцінний розвиток кожного студента.🤩\n"
                                       "    "),reply_markup=markup)
def send_military_accounting(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Назад", callback_data='back_to_main'))
    bot.send_message(message.chat.id, ("\n"
                                       "🫡В НУБіП України студенти мають можливість проходити військовий облік, що включає в себе навчання військово-тактичним навичкам, фізичну підготовку💪 та інші аспекти військової служби.🪖 Це дозволяє студентам отримати необхідні знання та навички для подальшої служби у Збройних Силах України та відповідної кар'єри.📈\n"
                                       "    "),reply_markup=markup)

def send_academy_scholarship(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Назад", callback_data='back_to_social_benefits'))
    bot.send_message(message.chat.id, ("\n"
                                       "Якщо Ви вступили на навчання за кошти держзамовлення (бюджет):\n"
                                       "\n"
                                       "1️⃣ Замовте карту для виплат в ПриватБанку (не кредитна, і не юніор) або за наявності вище вказаної додайте наступні налаштування, \n"
                                       "2️⃣ Підключіть в будь-якому відділенні або за допомогою гарячої лінії 3700 стипендіальний проект НУБіП (ЄДРПОУ: 00493706)\n"
                                       "3️⃣ Принесіть в деканат довідку за реквізитами, яку можна сформувати самостійно онлайн через розділ  «Послуги» в Приват24. \n"
                                       "4️⃣ ????Заповніть анкету: https://forms.gle/JAeJWC8hVbBzQdgz8\n"
                                       "5️⃣ Інформацію про академічну стипендію буде надано впродовж 10 робочих днів з початку навчання. 40% з бюджету спеціальності отримують її на основі рейтингу за конкурсними балами.\n"
                                       "6️⃣ Розмір стипендії звичайна- 2000 грн щомісяця, підвищена - 2910 грн щомісяця.\n"
                                       "7️⃣ 1 семестр - призначається за конкурсним балом вступників (період призначення - вересень-грудень 2024 року), всі наступні семестри - за рейтингом на підставі зведеної навчальної успішності - середнього балу (90%) та додаткових балів за громадську активність (10%)\n"
                                       "\n"
                                       "    "),reply_markup=markup)

def send_social_scholarship(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Назад", callback_data='back_to_social_benefits'))
    bot.send_message(message.chat.id, ("\n"
                                       "✍️Перелік документів для призначення соціальної стипендії студентам пільгових категорій денної форми за державним замовленням  та вимоги до їх оформлення , а також зразок на призначення соціальної стипендії тут: https://nubip.edu.ua/students\n"
                                       "\n"
                                       "\n"
                                       "❗️Документи необхідно подати очно в деканат – копії в 3-х екземплярах та заява. ДУЖЕ БАЖАНО НЕ ПІЗНІШЕ 1 тижня навчання в університеті❗️\n"
                                       "\n"
                                       "🧑‍💻Шановні студенти, які мають соціальну категорію  (бюджет і контракт)\n"
                                       "Просимо всіх долучитися в даний чат - тут буде розміщуватися вся важлива для вас інформація та живе спілкування про всі наявні питання.\n"
                                       "\n"
                                       "😉Соціалочка ІТ НУБіП:  https://t.me/+G8CbBwqVe9KtjlVT\n"
                                       "    "),reply_markup=markup)

def send_transfer_to_budget(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Назад", callback_data='back_to_social_benefits'))
    bot.send_message(message.chat.id, ("\n"
                                       "🟡 Інформація про зміну фінансування буде розміщуватися в каналі деканату, переведення можливе на 1 курсі, якщо під час роботи приймальної комісії вам зафіксували в ЄДЕБО пільгу, та подавали документи на бюджетне місці, зараховані за цією заявою. Переведення можливе на додаткові або вакантні місця.\n"
                                       "\n"
                                       "🟡 Поза приймальною комісією можливе на старших курсах. Інформація по мірі можливостей буде надаватися в каналі деканату.\n"
                                       "\n"
                                       "🟡 В період очікування переведення просимо оплатити за студ квиток і екзаменаційну книжку. Дякуємо за розуміння!\n"
                                       "\n"
                                       "    "),reply_markup=markup)

def send_benefit_living_in_dormitory(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Назад", callback_data='back_to_social_benefits'))
    bot.send_message(message.chat.id, ("\n"
                                       "❗️Для забезпечення пільгового проживання студентів окремих категорій у 2024-2025 навчальному році в гуртожитках студмістечка необхідно у двотижневий термін з моменту поселення у гуртожитки подати деканатам факультетів/дирекціям ННІ відповідні заяви з необхідними документами.\n"
                                       "\n"
                                       "   👩‍🎓Студенти, які вже отримували зазначену пільгу раніше, подають лише заяву, а всі інші-заяву з відповідним пакетом документів. Деканати факультетів/дирекції ННІ збирають заяви, зазначають в них дату та номер наказу, згідно якого студент поселений на поточний навчальний рік у гуртожиток і централізовано передають їх відділу соціальної роботи, який готує відповідний наказ.\n"
                                       " \n"
                                       "   📝 З переліком категорій студентів денної форми навчання (держзамовлення і контракт) та документів для надання їм пільги з оплати за проживання в гуртожитку, а також формою заяви можна ознайомитися на сайті НУБіП України у розділі «Студенту».\n"
                                       " \n"
                                       "   ❗️Що стосується студентів-сиріт та осіб з їх числа, то для пільгового проживання в гуртожитках вони також на тих же умовах мають подати до відділу соціальної роботи заяву, відповідно до своєї пільгової категорії.\n"
                                       "\n"
                                       "    "),reply_markup=markup)



def send_submenu(message, submenu):
    markup = InlineKeyboardMarkup()
    buttons_submenu = [
        InlineKeyboardButton("Назад", callback_data='info_campus')
    ]
    for button in buttons_submenu:
        markup.add(button)
    bot.send_message(message.chat.id, f"Інформація про {submenu}", reply_markup=markup)


# Run the bot
if __name__ == '__main__':
    print("Bot started and ready to use!")
    bot.polling()
