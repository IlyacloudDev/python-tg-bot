from config import lst_ofcurrency
import requests
import json


class ConvertExeption(Exception): # наше собственное исключение
    pass


class ConvertCurrency: #класс для получения JSON-ответа(стоимость, полученная при конвертации, в данном случае)
    @staticmethod
    def get_price(quote, base):  # статический метод, который будет вызываться от класса с некоторыми параметрами для получения
        # нужного JSON объекта
        if quote == base:  # будет вызвано исключение, если валюты совпадают, далее в файле functions будем ловить исключение
            raise ConvertExeption("Нельзя перевести валюты друг в друга 🚫")

        try:
            quote_position = lst_ofcurrency[quote]
        except KeyError:  # будет вызвано, если первая написанная валюта некорректна или её нет в списке
            raise ConvertExeption(f"Не удалось обработать валюту '{quote}'🔁❌")

        try:
            base_position = lst_ofcurrency[base]
        except KeyError:  # будет вызвано, если вторая написанная валюта некорректна или её нет в списке
            raise ConvertExeption(f"Не удалось обработать валюту '{base}'🔁❌")

        r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={quote_position}&tsyms={base_position}")  # отправляем get-HTTP
        # запрос для получения нужной информации
        result = json.loads(r.content)[base_position]  # преобразуем эту информацию из JSON формата в Python формат, и берём JSON от base_position
        # base_position = lst_ofcurrency[quote] = значению ключа, следовательно получим ответ по значению ключа, но в JSON
        # ответе это значение ключа будет выступать КЛЮЧОМ ! для стоимости
        return result  # и возвращаем его
