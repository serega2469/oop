class Human:

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
        if self.many:
            self.many -= house_price
            return f'\nВы купили дом стоимостью: {house_price} руб.' \
                   f' На счете осталось {self.many}'


user_1 = Human('Cергей', 24, 10000, 'Есть')
print(user_1.make_money())
print(user_1.buy_a_many())


class Home:
    def __init__(self, area, cost):
        self.area = area
        self.cost = cost

    def discount_home(self):
        discount = 50
        return f'Скидка на покупку дома составляет: {self.cost / discount}'


class New_home(Home):
    def __init__(self, area, cost):
        super.__init__(area, cost)





