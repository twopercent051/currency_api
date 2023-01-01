import json
import requests


def get_currency(rate1, rate2, value):
    session = requests.Session()
    req = session.get(url='https://www.cbr-xml-daily.ru/latest.js')
    response = req.text
    data = json.loads(response)
    if rate1 != 'RUB':
        course1 = float(data['rates'][rate1])
    else:
        course1 = 1
    if rate2 != 'RUB':
        course2 = float(data['rates'][rate2])
    else:
        course2 = 1
    result = value * (course2 / course1)

    return round(result, 2)

