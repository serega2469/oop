class Human:  # Скорее всего этот класс уже не Human,
    # а Person будет правильнее

    def __init__(self, name: str, age: int, many: bool | int, home: str):
        self.name = name
        self.age = age
        self.many = many
        self.home = home

    def info(self):
        template: str = (f'\nМеня зовут {self.name}'
                         f'\nМой возраст: {self.age}'
                         f'\n Наличие денег: {self.many}'
                         f'\n Наличие дома: {self.home}')
        return template

    def make_money(self):
        count = 0
        if not self.many:
            count += 1000
            return f'Вы заработали: {count} руб'
        return self.many

    def buy_a_many(self):
        house_price = 5
        if self.many:  # Проверка ни о чем не говорит, его нужно вычесть
            # из self.many, только если у покупателя достаточно средств на счету
            self.many -= house_price
            # Тут лучше использовать скобки для переноса
            # текста, вместо слэша, как в 11 строке кода
            return f'\nВы купили дом стоимостью: {house_price} руб.' \
                   f' На счете осталось {self.many}'


class Home:
    def __init__(self, area, cost):
        self.area = area
        self.cost = cost

    def discount_home(self):
        discount = 50  # Скидка всегда будет 50% или для всех будет разный %?
        return f'Скидка на покупку дома составляет: {self.cost / discount}'


# Классы должны называться в соответствии с нотацией PascalCase.
class New_home(Home):  # Почитать можно тут: https://skillbox.ru/media/code/notatsii-v-programmirovanii/
    def __init__(self, area, cost):
        # Тут ошибка, забыли круглые скобки после super
        super.__init__(area, cost)


if __name__ == '__main__':  # Используйте точку входа,
    # в коде не должно создаваться никаких объектов.
    user_1 = Human('Cергей', 24, 10000, 'Есть')
    print(user_1.make_money())
    print(user_1.buy_a_many())
