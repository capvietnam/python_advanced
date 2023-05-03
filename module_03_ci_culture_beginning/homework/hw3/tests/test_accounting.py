import unittest
from datetime import datetime
from accounting import app, storage
import json


class TestApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Добавляем начальные данные в storage
        storage[2022] = {1: {1: 100, 2: 200, 3: 300}, 2: {15: 500, 28: 600}}
        storage[2023] = {6: {10: 50, 11: 100}}

    # Проверяем, что endpoint /add/ работает
    def test_add(self):
        # Добавляем одну запись
        client = app.test_client()
        response = client.get('/add/20260104/50')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), {'date': '20260104', 'expense': 50})
        self.assertEqual(storage[2026][1][4], 50)

        # Добавляем ещё одну запись в другой день
        response = client.get('/add/20260228/150')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), {'date': '20260228', 'expense': 150})
        self.assertEqual(storage[2026][2][28], 150)

        response = client.get('/add/20220228/150')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), {'date': '20220228', 'expense': 150})
        self.assertEqual(storage[2022][2][28], 750)

    # Проверяем, что оба endpoints /calculate/ работают
    def test_calculate(self):
        client = app.test_client()
        # Проверяем расчет за год, когда есть данные
        response = client.get('/calculate/2022')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), {'year': 2022, 'total': 1850})

        # Проверяем расчет за месяц, когда есть данные
        response = client.get('/calculate/2022/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), {'year': 2022, 'month': 1, 'total': 600})

        # Проверяем расчет за год, когда нет данных
        response = client.get('/calculate/2024')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), {'year': 2024, 'total': 0})

    # Проверяем, что endpoint /add/ может принять дату только в формате YYYYMMDD,
    # а при подаче невалидного значения что-то идёт не так
    def test_invalid_date_format(self):
        client = app.test_client()
        # Подаем дату неверного формата — должно вывестись сообщение с ошибкой
        response = client.get('/add/2022/1/4/50')
        self.assertEqual(response.status_code, 404)

    # Проверяем, как будут работать endpoints /calculate/, если в storage ничего нет
    def test_no_data_in_storage(self):
        client = app.test_client()
        # Проверяем расчет за год, когда нет данных
        response = client.get('/calculate/2024')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), {'year': 2024, 'total': 0})

        # Проверяем расчет за месяц, когда нет данных
        response = client.get('/calculate/2024/3')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), {'year': 2024, 'month': 3, 'total': 0})

        response = client.get('/calculate/2028/3')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), {'year': 2028, 'month': 3, 'total': 0})


if __name__ == '__main__':
    unittest.main()
