class Drink:
    volume = 200

    def __init__(self, name, price):
        self.name = name
        self.price = price

        self.remains = self.volume

    def drink_info(self):

        print(f'Название: {self.name}. Стоимость: {self.price}. Обьём: {self.volume}. Осталось {self.remains} ')

    def _is_enough(self, need):
        if self.remains >= need and self.remains > 0:
            return True
        print('Осталось недостаточно напитка')
        return False

    def sip(self):
        if self._is_enough(20):
            self.remains -= 20
            print('Друг сделал глоток')

    def small_sip(self):
        if self._is_enough(10):
            self.remains -= 10
            print('Друг сделал маленький глоток')

    def drink_all(self):
        if self._is_enough(0):
            self.remains = 0
            print('Друг выпил напиток залпом')


class Juice(Drink):
    def __init__(self, name, price, taste):
        super().__init__(name, price)
        self.taste = taste


apple_juice = Juice('Сок', 250, 'яблочный')
coffee = Drink('Кофе', 300)

apple_juice.small_sip()
apple_juice.sip()
apple_juice.drink_info()
