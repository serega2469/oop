class Human:
    default_name: str = 'Неизвестно'
    default_age: int | None = None

    def __init__(self,
                 name: str = default_name,
                 age: int = default_age) -> None:
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        print(
            (f'\nИмя: {self.name}\nВозраст: {self.age}'
             f'\nБаланс: {self.__money}\nДом: {self.__house}')
        )

    @staticmethod
    def default_info():
        print(
            f'\nИмя по умолчанию: {Human.default_name}'
            f'\nВозраст по умолчанию: {Human.default_age}'
        )

    def __make_deal(self, obj: 'House', price: float | int) -> None:
        self.__money = self.__money - price
        self.__house = obj

    def earn_money(self, value: float | int) -> None:
        """
        Увеличивает значение свойства money.

        :param value: Сумма, которую нужно положить на счет.
        :return: None
        """
        if value < 0:
            raise ValueError('Укажите корректную сумму')

        if not isinstance(value, (float, int)):
            raise TypeError('Укажите числовое значение')

        self.__money += value

    def buy_house(self, house: 'House', discount: float) -> None:
        curr_price = house.final_price(discount)

        if self.__money < curr_price:
            raise ValueError('Недостаточно средств')

        self.__make_deal(obj=house, price=curr_price)


class House:
    def __init__(self, area, price) -> None:
        self._area = area
        self._price = price

    def final_price(self, discount: float) -> float:
        """
        Возвращает цену с учетом данной скидки.

        :param discount: Размер скидки.
        :return:
        """
        return self._price - (self._price * discount)

        # Хлеб - 110р <---- 40%
        # 0.4 * 110р = 44р
        # 110р - 44р = 66р


class SmallHouse(House):
    def __init__(self, area=40, price=600):
        super().__init__(area, price)


if __name__ == '__main__':
    # protected - _
    # private - __

    Human.default_info()
    h_1 = Human('Макс', 19)
    h_1.info()

    # h_2 = Human()
    # h_2.info()

    sm_1 = SmallHouse()
    # h_1.buy_house(sm_1, 0.1)  # ValueError: Недостаточно средств

    h_1.earn_money(1000)  # Положили на счет 1000р
    h_1.buy_house(sm_1, 0.1)
    h_1.info()
