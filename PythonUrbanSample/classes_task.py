# класс - 1
class Car:
    def __init__(self, brand: str, max_speed: int, year: int):
        """
        Создание и подготовка к работе объекта "Автомобиль"

        :param brand: марка автомобиля
        :param max_speed: максимальная скорость автомобиля
        :param year: год выпуска автомобиля
        """
        self.brand = brand
        self.max_speed = max_speed
        self.year = year

    def is_car(self) -> bool:
        """
        Функция которая проверяет является ли словарь автомобилем

        :return: Является ли объект автомобилем или нет
        """
        ...

    def is_old(self, years_old: int) -> bool:
        """
        Проверка автомобиля на возраст
        :param years_old: кол-во лет

        :return: старше заданного кол-ва лет или нет
        """
        ...

    def producing_country(self, countries_dict: dict) -> str:
        """
        Нахождение страны производства марки автомобиля

        :param countries_dict: словарь страна - марки автомобилей
        :return: страна
        """
        ...


if __name__ == "__main__":
    mercedes = Car("mercedes benz", 300, 2019)  # инициализация экземпляра класса


# класс - 2
class TwitterPost:
    def __init__(self, nickname: str, post_text: str):
        """
        Создание и подготовка к работе объекта "Твит"

        :param nickname: никнейм автора
        :param post_text: текст твита
        """
        self.nickname = nickname
        self.post_text = post_text

    def is_twit(self) -> bool:
        """
        Функция которая проверяет является ли словарь твитом

        :return: Является ли объект твитом или нет
        """
        ...

    def twit_length(self) -> int:
        """
        Расчет длины твита (текста твита)

        :return: длина текста твита
        """
        ...

    def add_copyright(self, copy_right: str) -> str:
        """
        Добавление в конец твита автора (из nickname) со значком копирайта

        :param copy_right: копирайт, автор поста
        :return: твит с автором
        """
        ...


if __name__ == "__main__":
    my_twit = TwitterPost("my_nickname", "Hello, Twitter!")  # инициализация экземпляра класса


# класс - 3
class Box:
    def __init__(self, volume: int, color: str, material: str):
        """
        Создание и подготовка к работе объекта "Коробка"

        :param volume: объем коробки
        :param color: цвет коробки
        :param material: материал коробки
        """
        self.volume = volume
        self.color = color
        self.material = material

    def is_box(self) -> bool:
        """
        Функция которая проверяет является ли словарь коробкой

        :return: Является ли объект коробкой или нет
        """
        ...

    def is_suitable_volume(self, thing_volume: int) -> bool:
        """
        Подойдет ли коробка под заданный объем вещи

        :param thing_volume: объем вещи
        :return: помещается вещь в коробку или нет
        """
        ...

    def change_color(self, new_color: str) -> str:
        """
        Изменение цвета коробки

        :param new_color: новый цвет для коробки
        :return: новый цвет коробки
        """
        ...


if __name__ == "__main__":
    new_box = Box(25,"green", "paper")  # инициализация экземпляра класса