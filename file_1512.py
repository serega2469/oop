# fract = 3.576854
# num = 97
# line = 'Заголовок'
# line.capitalize()
# post = 'Новости'
# post.capitalize()

# ----------------------------------------------

# class Human:
#     # атрибуты (или свойства) класса
#     name: str | None = None
#     age: int | None = None
#     sex: str | None = None
#
#
# petya = Human()
# petya.name = 'Петя'
# print(petya.name)
#
# vasya = Human()
# vasya.name = 'Вася'
# vasya.age = 19
# print(vasya.name, vasya.age)


# ----------------------------------------------
class Human:
    # конструктор класса
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = self.check_sex(sex)

    def check_sex(self, value):
        if value.lower() not in ('м', 'ж'):
            raise ValueError('Пол может быть только мусжким или женским')
        return value

    # Поведение - Методы класса (это обычные функции)
    def info(self):
        print(f'Меня зовут {self.name}, мне {self.age}. Пол: {self.sex}')

    def say(self):
        print('Я говорю')


petya = Human(age=18, sex='М', name='Петя')
vasya = Human('Вася', 19, 'М')
anya = Human('Аня', 17, 'Ж')
# example = Human('Выдуманное имя', 27, 'Т')   # Error

petya.info()
vasya.info()
anya.info()

petya.say()
vasya.say()
anya.say()

# TODO: Попробуйте описать класс животных, Кошки, Собаки
