# Абстракция
import abc


class Human(abc.ABC):
    """Абстрактный класс человека."""

    @abc.abstractmethod
    def head(self):
        pass

    @abc.abstractmethod
    def brain(self):
        pass

    @abc.abstractmethod
    def hands(self):
        pass

    @abc.abstractmethod
    def foots(self):
        pass


class HumanBase(Human):
    """Базовый класс для человека."""

    def __init__(self, name, date_of_birth, sex, height, weight):
        self.name = name
        self.date_of_birth = date_of_birth
        self.sex = sex
        self.height = height
        self.weight = weight

    def head(self):
        print('Голова')

    def brain(self):
        print('Мозг')

    def hands(self):
        print('Руки')

    def foots(self):
        print('Ноги')

    def info(self):
        template: str = (f'\nМеня зовут {self.name}'
                         f'\nМой рост: {self.height} см.'
                         f'\nМой вес: {self.weight}')

        return template


class Student(HumanBase):
    def __init__(self,
                 name,
                 date_of_birth,
                 sex,
                 height,
                 weight,
                 high_education: bool = True):
        super().__init__(name, date_of_birth, sex, height, weight)
        self.high_education = high_education

    def _check_edu(self):
        if self.high_education:
            return 'имеется'
        return 'не имеется'

    # переопределить метод info родительского класс
    def info(self):
        template = super().info()
        template += f'\nВысшее образование: {self._check_edu()}'

        return template


class Employee(HumanBase):
    pass
    # def position_info(self):
    #     print('Я менеджер')


if __name__ == '__main__':
    h1 = HumanBase('Человек-Паук', '01.01.1970', 'М', 1.75, 72)
    s1 = Student('Макс', '01.01.2000', 'М', 1.65, 60, False)

    h1.brain()
    s1.foots()
    print(h1.info())
    print(s1.info())

    e1 = Employee('Вася', '01.01.1970', 'М', 1.95, 78)
    print(e1.info())
