import telebot 
from forex_python.converter import CurrencyRates
import requests as r
from PIL import Image
from io import BytesIO


TOKEN = ''
bot = telebot.TeleBot(TOKEN, parse_mode='html')

COMMANDS = ['start', 'convert', 'get_coffee_picture', 'update_math_skills','get_smart_quote','shakal_picture']


@bot.message_handler(commands=COMMANDS)
def start_message(message) -> None:
    '''
        Главная функция, обрабатывающая команды, полученные от пользователя
    '''

    keyboard = get_main_keyboard()

    if message.text.lower() == '/start':
        bot.send_message(message.chat.id, f'<b color="red">{message.from_user.username}</b>, добро пожаловать в MIEMUniversalBot 🤩 \n\nДанный бот имеет множество различных полезных команд, все они приведены в списке ниже! \n\n/convert - команда для конвертации валюты!\n/get_coffee_picture - команда для получения рандомной картинки кофе!\n/update_math_skills - команда для прокачки большого ума!\n/get_smart_quote - команда для получения пищи для размышлений!\n/shakal_picture - команда для шакалинга картинки!', reply_markup=keyboard)
 
    elif message.text.lower() == '/convert':
        ask_for_pair(message)

    elif message.text.lower() == '/get_coffee_picture':
        get_coffee_picture(message)

    elif message.text.lower() == '/update_math_skills':
        update_math_skills(message)

    elif message.text.lower() == '/get_smart_quote':
        get_smart_quote(message)
    
    elif message.text.lower() == '/shakal_picture':
        ask_for_photo(message)

    else:
        bot.send_message(message.chat.id, "Пока что я не знаю, как на такое реагировать!🥺")


@bot.message_handler(content_types=['text'])
def text_processing(message) -> None:
    '''
        Функция обработки обыного текста от пользователя
    '''
    
    if 'конвертировать' in message.text.lower():
        ask_for_pair(message)

    elif 'кофе' in message.text.lower():
        get_coffee_picture(message)

    elif 'решить' in message.text.lower() or 'пример' in message.text.lower() or 'матан' in message.text.lower():
        update_math_skills(message)

    elif 'цитат' in message.text.lower() or 'поумничать' in message.text.lower():
        get_smart_quote(message)

    elif 'начал' in message.text.lower():
        keyboard = get_main_keyboard()
        bot.send_message(message.chat.id, 'Добро пожаловать обратно в главное меню 😵‍💫', reply_markup=keyboard)

    elif 'подшаман' in message.text.lower() or 'шакалить' in message.text.lower():
        ask_for_photo(message)

    else:
        bot.send_message(message.chat.id, "Пока что я не знаю, как на такое реагировать!🥺")

def get_main_keyboard() -> telebot.types.ReplyKeyboardMarkup:
    '''
        Функция, возвращающая главные кнопки нашего бота
    '''

    main_keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    main_keyboard.row('Хочу кофе ☕️', 'Мне бы валюту конвертировать 💶')
    main_keyboard.row('Надо к матану готовиться 🤯','Хочу поумничать перед друзьями 🥸')
    main_keyboard.row('Надо чето с картинкой подшаманить 🪄')

    return main_keyboard

def ask_for_photo(message) -> None:
    bot.send_message(message.chat.id, f'Отправьте картинку, которую надо зашакалить Ꮗ')
    bot.register_next_step_handler(message, picture_magic)

def picture_magic(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('Хочу шакалить еще🧐', 'Хочу в начало 🥱')
    
    try:
        fileID = message.photo[0].file_id
        file_path = f"https://api.telegram.org/file/bot" + str(TOKEN) + "/" + str(bot.get_file(fileID).file_path)

        response = r.get(file_path)
        img = Image.open(BytesIO(response.content))

        bot.send_photo(message.chat.id, img)
        bot.send_message(message.chat.id, f'Да это же картинка на 10 шакалов из 10, не надо благораности ⑀', reply_markup=keyboard)
    except:
        bot.send_message(message.chat.id, f'Сказали же картинку, а не что-то неясное ⑀', reply_markup=keyboard)
        

def get_smart_quote(message) -> None:
    '''
        С помощью данной функции пользователь может получить умную цитатку
        и отяжелить свой мозг умными мыслями
    '''
    res = r.get('https://api.fisenko.net/v1/quotes/ru/random')

    if res.status_code == 200:
        try:
            expression = res.json()['text']
            author = res.json()['author']['name']
            
            keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.row('Давай еще по одной цитатке 🧐', 'Хочу в начало 🥱')

            bot.send_message(message.chat.id, f'Как однажды сказал <b>{author}</b>: <i>"{expression}"</i>. Есть над чем подумать!\n\nМожет еще по одной цитатке? 😏', reply_markup=keyboard)
            
        except:
            bot.send_message(message.chat.id, 'Во время обращения к API произошла ошибка, пожалуйста, попробуйте позже 🥲', reply_markup=get_main_keyboard())
    else:
        bot.send_message(message.chat.id, 'Во время обращения к API произошла ошибка, пожалуйста, попробуйте позже 🥲', reply_markup=get_main_keyboard())


def update_math_skills(message) -> None:
    '''
        Функция реализующая прокачку математический скиллов пользователя
    '''

    res = r.get('https://x-math.herokuapp.com/api/random')

    if res.status_code == 200:
        try:
            expression = res.json()['expression']
            answer = int(res.json()['answer'])

            bot.send_message(message.chat.id, f'Вам предлагается решить данный пример для увеличения своей скорости счета, чем быстрее решите, тем лучше! 🤓\n\n<b>{expression} = ?</b>\n\nПросто напишите мне ответ 🧐', reply_markup=None)
            bot.register_next_step_handler(message, check_math_answer, answer)

        except:
            bot.send_message(message.chat.id, 'Во время обращения к API произошла ошибка, пожалуйста, попробуйте позже 🥲',reply_markup=get_main_keyboard())
    else:
        bot.send_message(message.chat.id, 'Во время обращения к API произошла ошибка, пожалуйста, попробуйте позже 🥲', reply_markup=get_main_keyboard())

def check_math_answer(message, answer) -> None:
    '''
        Функция проверки ответа пользовтеля по математической операции
    '''
    
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('Решить еще пример 😱', 'Хочу в начало 🥱')

    try:
        user_answer = int(message.text)
    
        if user_answer == answer:
            bot.send_message(message.chat.id, f'<b>{message.from_user.username}</b>, да вы супер мега крутой 😶‍🌫️\nНе хотите решить еще примерчик?', reply_markup=keyboard)
        else:
            bot.send_message(message.chat.id, f'<b>{message.from_user.username}</b>, это было очень близко, но нет😣 \n Не хотите решить еще примерчик?', reply_markup=keyboard)

    except:
        bot.send_message(message.chat.id, 'Похоже, что вы вводите не число!🥲\nПопробуем еще разик?', reply_markup=keyboard)

def get_coffee_picture(message) -> None:
    '''
        Функция, возвращающая рандомную картинку кофе
    '''
    
    res = r.get('https://coffee.alexflipnote.dev/random.json')

    if res.status_code == 200:
        try:
            keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.row('Еще кофе 🥴', 'Хочу в начало 🥱')

            bot.send_photo(message.chat.id, res.json()['file'])
            bot.send_message(message.chat.id, 'Вот ваша фоточка прекрасного напитка! 🤪', reply_markup=keyboard)
        except:
            bot.send_message(message.chat.id, 'Во время обращения к API произошла ошибка, пожалуйста, попробуйте позже 🥲', reply_markup=get_main_keyboard())
    else:
        bot.send_message(message.chat.id, 'Во время обращения к API произошла ошибка, пожалуйста, попробуйте позже 🥲', reply_markup=get_main_keyboard())

def ask_for_pair(message) -> None:
    '''
        Функция, на которой мы страшиваем у пользователя валютную пару.
    '''
    
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('USD RUB', 'EUR RUB', 'GBP RUB')
    keyboard.row('USD GBP', 'EUR GBP', 'EUR USD')

    bot.send_message(message.chat.id, f'<b>{message.from_user.username}</b>, выберите интересующую вас валютную пару для перевода или впишите свою 🤩 \n\n Пример <b>EUR USD</b>', reply_markup=keyboard)
    bot.register_next_step_handler(message, prep_pair)


def prep_pair(message) -> None:
    '''
        Функция предобработки данных введенных пользователем
    '''
    
    user_prep = list(map(lambda x: x.upper(), filter(lambda x: x != ' ' or x != '', message.text.strip().split(' '))))    
    
    if len(user_prep) != 2:
        bot.send_message(message.chat.id, 'Ошибка в вводе! 🙁\nПожалуйста, проверьте правильность введеных данных и повторите попытку!', reply_markup=get_main_keyboard())
    else:
        bot.send_message(message.chat.id,"Введите сумму, которую необходимо перевести 🥶")
        bot.register_next_step_handler(message, convert, user_prep)

def convert(message, pair) -> None:
    '''
        Функция непосредственной конвертации валюты    
    '''

    try:
        money_amount = abs(float(message.text))
    except:
        bot.send_message(message.chat.id, 'Ошибка в вводе! 🙁\nСумма должна быть числовым значением!', reply_markup=get_main_keyboard())

    c = CurrencyRates()
    curr_1 = pair[0]
    curr_2 = pair[1]
    try:
        rate = c.get_rate(curr_1, curr_2)
        
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.row('Конвертировать еще 👁','Вернуться к началу 🧐')

        bot.send_message(message.chat.id, f'Результат конвертации по паре <b>{curr_1} {curr_2}</b>:\n\n <b>{money_amount} {curr_1} = {(rate * money_amount):.2f} {curr_2}</b>', reply_markup=keyboard)
    except:
        bot.send_message(message.chat.id, 'Ошибка в вводе! 🙁\nПожалуйста, проверьте правильность введеных данных и повторите попытку!', reply_markup=get_main_keyboard())

        
bot.polling()

