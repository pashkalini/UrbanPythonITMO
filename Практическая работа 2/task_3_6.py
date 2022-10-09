# LIST COMPREHENSION
# Задача. Отфильтровать города с населением больше 1 млн. человек.

list_cities = [
    {
        "name": "Москва",
        "population": 12 * 10 ** 6,
    },
    {
        "name": "Санкт-Петербург",
        "population": 5 * 10 ** 6,
    },
    {
        "name": "Ижевск",
        "population": 0.6 * 10 ** 6,
    },
]
filter_population = 10 ** 6
# TODO отфильтровать города
list_cities_filtered = [item for item in list_cities if item['population'] > filter_population]

print(f'Города с населением больше 1 млн. человек: {list_cities_filtered}')