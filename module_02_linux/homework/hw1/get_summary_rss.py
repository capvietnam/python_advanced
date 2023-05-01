"""
С помощью команды ps можно посмотреть список запущенных процессов.
С флагами aux эта команда выведет информацию обо всех процессах, запущенных в системе.

Запустите эту команду и сохраните выданный результат в файл:

$ ps aux > output_file.txt

Столбец RSS показывает информацию о потребляемой памяти в байтах.

Напишите функцию get_summary_rss, которая на вход принимает путь до файла с результатом выполнения команды ps aux,
а возвращает суммарный объём потребляемой памяти в человекочитаемом формате.
Это означает, что ответ надо перевести в байты, килобайты, мегабайты и так далее.
"""
import math
import os


def get_summary_rss(file_path: str) -> str:
    with open(file_path, 'r') as file:
        lines = file.readlines()
        rss_sum = 0
        for line in lines[1:]:  # пропускаем первую строку с заголовками
            items = line.split()
            rss_bytes = int(items[5])
            rss_sum += rss_bytes

        if rss_sum == 0:
            return "0B"
        size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
        i = int(math.floor(math.log(rss_sum, 1024)))
        p = math.pow(1024, i)
        s = round(rss_sum / p, 2)
        return "%s %s" % (s, size_name[i])


if __name__ == '__main__':
    path: str = os.path.join(os.path.dirname(__file__), 'output_file.txt')
    summary_rss: str = get_summary_rss(path)
    print(summary_rss)
