from main import bot
from extensions import *


@bot.message_handler(commands=['start', 'help']) # основные информирующие команды
def info_bt(message):
    bot.send_message(message.chat.id, f"Привет, <b>{message.from_user.first_name}</b>, здесь ты можешь проконвертировать валюты💵!\n"
                     f"Инструкция по конвертированию:\n"
                     f"1 - <b>валюта, цену которой хотим узнать</b>✅\n"
                     f"2 - <b>валюта, в которой надо узнать цену первой валюты</b>✅\n"
                     f"3 - <b>кол-во первой валюты✅</b>\n"
                     f"Задавать параметры по инструкции надо в строчку через пробел!💻\n"
                     f"Пример:\n"
                     f"<b>доллар рубль 35</b>📈\n"
                     f"Для нахождения доступных валют используйте /values ❤️", parse_mode="html") #вывод текста


@bot.message_handler(commands=['values']) # показ доступных валют
def check_currencies(message):
    avaible_currencies = "Доступные валюты:"
    for key in lst_ofcurrency.keys(): # проходимся по ключам списка из конфига
        avaible_currencies = "\n".join((avaible_currencies, key)) # через перенос строки будет печатать наши валюты
    bot.send_message(message.chat.id, avaible_currencies)


@bot.message_handler(content_types=['text']) # принимаем наш тект, ожидаем что поступит название двух валют и кол-во, которое хотим получть
def get_convertating(message):
    try: #пробуем разбить названия наших валют и кол-во в список
        values = message.text.split()
        if len(values) < 3: # если нас не устраивает длина(кол-во заданных параметров)
            raise ConvertExeption("Недостаточно параметров📝!") # возбуждаем собственное исключение, которое потом будем ловить
        elif len(values) > 3: # аналогично
            raise ConvertExeption("Слишком много параметров📝!")
        quote, base, amount = values #присваиваем значения из списка трем элементам
        try: # будем проверять, корректно ли введено кол-во
            amount = float(amount.replace(",", "."))
        except ValueError: #будем отлавливать встроенное исключение и возбуждать своё для будущего отлова
            raise ConvertExeption(f"Не удалось обработать количество '{amount}'")
        try:
            if amount < 1:
                raise ValueError
        except ValueError:
            raise ConvertExeption(f"Нельзя брать кол-во меньше единицы❌") # аналогично
        command_result = ConvertCurrency.get_price(quote, base) #вызываем статический метод через класс из другого фала,
        # для получения нужного JSON ответа, который записываем в переменную
    except ConvertExeption as e: #как раз отлов собственных исключений
        bot.reply_to(message, f"Произошла ошибка❗️:\n"f"{e}")
    except Exception as e: # отлов исключения, которое может возникнуть из-за системных проблем, а не из-за ошибок пользователя
        bot.reply_to(message, f"Не удалось обработать команду❗️\n"f"{e}")
    else:
        bot.send_message(message.chat.id, f"При конвертации из валюты <i>'{quote}'</i> в валюту <i>'{base}'</i> стоимость составила💸:\n"
                                          f"<b>{command_result*amount}</b>✅", parse_mode="html") # печатаем нашу стоимость
