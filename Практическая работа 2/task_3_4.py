# PythonUrban_tasks_3 - задача 4
# Написать функцию filter_min_green_index,
# которая в качестве аргументов принимает список объектов типа GreenZoneIndex
# и минимальный порог озеленения, значение по умолчанию 0.1.
# Результатом функции должно быть число территорий,
# индекс озеленения которых ниже заданного минимального порога.

from task_3_3 import *


def filter_min_green_index(green_list, min_green_index):
    low_green_index_cnt = 0
    for el in green_list:
        if el.calculate_green_index() < (min_green_index * 100):
            low_green_index_cnt += 1

    return low_green_index_cnt


print(f'Кол-во территорий с низким индексом озеленения: {filter_min_green_index(new_list_territories, 0.1)}')
