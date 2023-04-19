import requests
import json
from nums import keys

class APIException(Exception):
    pass

class Converter:
    @staticmethod
    def convert(val1: str, val2: str, amount: str):

        if val1 == val2:
            raise APIException(f'Невозможно перевести одинаковые валюты.')

        try:
           val1_ticker = keys[val1]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту, {val1}')

        try:
            val2_ticker = keys[val2]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту, {val2}')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать валюту. {amount}')

        r = requests.get(f'https://v6.exchangerate-api.com/v6/3239995c513c2e2f2a9c7732/pair/{val1_ticker}/{val2_ticker}/{amount}')
        total = json.loads(r.content)['conversion_result']
        return total