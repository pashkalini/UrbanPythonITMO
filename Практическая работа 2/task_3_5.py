# LIST COMPREHENSION
# Задача. Сделать название городов с заглавной буквы.

list_cities = ["москва", "иЖЕВСк", "Владивосток", "новосибирсК", "мУРМАНСК"]
# TODO метод строки capitalize делает первую букву заглавной, а все остальные строчными
list_cities = [item.capitalize() for item in list_cities]
print(list_cities)
