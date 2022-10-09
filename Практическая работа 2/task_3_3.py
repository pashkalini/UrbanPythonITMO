# PythonUrban_tasks_3 - задача 3
# Написать функцию get_mean_green_index,
# которая в качестве аргумента принимает список объектов типа GreenZoneIndex и считает от них средний индекс озеленения.
from statistics import mean

from task_3_2 import new_list_territories


def get_mean_index(green_list):
    green_index_list = []

    for el in green_list:
        green_index_list.append(el.calculate_green_index())

    print(green_index_list)
    return round(mean(green_index_list), 2)


print(f'Cредний индекс озеленения: {get_mean_index(new_list_territories)}')
