# PythonUrban_tasks_3 - задача 1
class GreenZoneIndex:
    def __init__(self, territory_name, territory_area, green_zones):
        """
        :param territory_name: Название территории
        :param territory_area: Площадь территории
        :param green_zones: Список площадей парков
        """
        # TODO все аргументы конструктора записать в атрибуты экземпляра класса
        self.territory_name = territory_name
        self.territory_area = territory_area
        self.green_zones = green_zones

        self.zones_sum = sum(green_zones)
        # print(f"zones_sum= {self.zones_sum}")

        # TODO посчитать индекс озеленения с помощью метода calculate_green_index
        self.green_index = self.calculate_green_index()  # индекс озеленения

    def calculate_green_index(self):
        """
        Метод для вычисления индекса озеленения.
        Индекс рассчитывается как отношение площади всех парков к площади территории
        """
        # TODO посчитать индекс озеленения с атрибутов экземпляра класса
        return (self.zones_sum / self.territory_area) * 100


territory_name = "Пушкин"
territory_area = 28676
green_zones = [302, 487, 420, 325, 471, 363, 404]
# TODO Создать экземпляр класса и с помощью его атрибутов распечатать индекс озеленения
#  в процентах до 2 знака после запятой.
index = GreenZoneIndex(territory_name, territory_area, green_zones)
print(f" Индекс озеленения территории Пушкин равен {round(index.green_index, 2)}%")

# Ожидаемый ответ Индекс озеленения территории Пушкин равен 9.67%
