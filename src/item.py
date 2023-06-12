from abc import ABC, abstractproperty
import csv


class Item(ABC):
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    @property
    def name(self):
        """
        :return: Значение приватного атрибута name
        """
        return self.__name

    @name.setter
    def name(self, new_name):
        """
        Присваивает при определенном условии приватному атрибуту name новое значение
        :param new_name: Новое значение имени
        """
        if len(new_name) <= 10:
            self.__name = new_name
        else:
            print("Длина наименования товара превышает 10 символов.")

    @classmethod
    def instantiate_from_csv(cls, path):
        """
        Класс-метод, инициализирующий экземпляры класса `Item` данными из файла _src/items.csv_
        """
        with open(f'{path}', encoding='cp1251') as file:
            file = csv.DictReader(file, delimiter=",")

            for row in file:
                name = row["name"]
                price = row["price"]
                quantity = row["quantity"]
                cls(name, price, quantity)

    @staticmethod
    def string_to_number(string):
        """
        Статический метод, возвращающий число из числа-строки
        """
        string = string.split(".")

        if len(string) > 1 and int(string[1]) > 5 * (10 ** (len(string[1]) - 1)):
            return int(string[0]) + 1
        else:
            return int(string[0])

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate


