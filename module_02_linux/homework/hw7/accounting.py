"""
Реализуйте приложение для учёта финансов, умеющее запоминать, сколько денег было потрачено за день,
а также показывать затраты за отдельный месяц и за целый год.

В программе должно быть три endpoints:

/add/<date>/<int:number> — сохранение информации о совершённой в рублях трате за какой-то день;
/calculate/<int:year> — получение суммарных трат за указанный год;
/calculate/<int:year>/<int:month> — получение суммарных трат за указанные год и месяц.

Дата для /add/ передаётся в формате YYYYMMDD, где YYYY — год, MM — месяц (от 1 до 12), DD — число (от 01 до 31).
Гарантируется, что переданная дата имеет такой формат и она корректна (никаких 31 февраля).
"""

from datetime import datetime
from flask import Flask
from flask import jsonify

app = Flask(__name__)

storage = {}


@app.route("/add/<string:date>/<int:number>")
def add(date, number):
    dt = datetime.strptime(date, "%Y%m%d")
    year = dt.year
    month = dt.month
    day = dt.day

    # Используем setdefault, чтобы создать вложенные словари,
    # если их еще нет в хранилище
    storage.setdefault(year, {})
    storage[year].setdefault(month, {})
    storage[year][month].setdefault(day, 0)

    storage[year][month][day] += number

    # Возвращаем JSON-объект с результатом
    return jsonify({'date': date, 'expense': number})


@app.route("/calculate/<int:year>")
def calculate_year(year):
    year_total = 0

    # Сумма расходов за год
    if year in storage:
        for month in storage[year]:
            for day in storage[year][month]:
                year_total += storage[year][month][day]

    # Возвращаем JSON-объект с результатом
    return jsonify({'year': year, 'total': year_total})


@app.route("/calculate/<int:year>/<int:month>")
def calculate_month(year, month):
    month_total = 0

    # Сумма расходов за месяц
    if year in storage and month in storage[year]:
        for day in storage[year][month]:
            month_total += storage[year][month][day]

    # Возвращаем JSON-объект с результатом
    return jsonify({'year': year, 'month': month, 'total': month_total})


if __name__ == "__main__":
    app.run(debug=True)
