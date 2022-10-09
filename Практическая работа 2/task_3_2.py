# PythonUrban_tasks_3 - задача 2

# Дан список словарей территорий.
# Сделать новый список с объектами ранее реализованного типа GreenZoneIndex.
from task_3_1 import GreenZoneIndex

list_territories = [
    {
        "territory_name": "Пушкин",
        "territory_area": 28676,
        "green_zones": [302, 487, 420, 325, 471, 363, 404]
    },
    {
        "territory_name": "Павловск",
        "territory_area": 21025,
        "green_zones": [360, 375, 223, 258, 345, 296, 303]
    },
    {
        "territory_name": "Петергоф",
        "territory_area": 44274,
        "green_zones": [364, 447, 438, 223, 336, 431, 442]
    },
]

new_list_territories = []
for el in list_territories:
    new_list_territories.append(GreenZoneIndex(el["territory_name"], el["territory_area"], el["green_zones"]))

print(new_list_territories)

for el in new_list_territories:
    print(el.territory_name, el.territory_area, el.green_zones)


