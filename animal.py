import abc


class Animal(abc.ABC):
    """Абстрактный класс."""

    @abc.abstractmethod
    def head(self):
        pass

    @abc.abstractmethod
    def tail(self):
        pass

    @abc.abstractmethod
    def four_paws(self):
        pass

    @abc.abstractmethod
    def ears(self):
        pass


class AnimalBase(Animal):
    """Базовый класс животных."""

    def __init__(
            self, name: str, breed: str, gender: str, color: str
    ) -> None:
        self.name = name
        self.breed = breed
        self.gender = gender
        self.color = color

    def head(self):
        print('Голова')

    def tail(self):
        print('Хвост')

    def four_paws(self):
        print('Четыре лапы')

    def ears(self):
        print('Уши')

    def info(self) -> str:
        template: str = (f'\nМеня зовут {self.name}'
                         f'\nПорода: {self.breed}'
                         f'\nПол: {self.gender}')

        return template


class Cat(AnimalBase):
    """Класс кошек."""

    def __init__(
            self, name: str, breed: str, gender: str, color: str
    ) -> None:
        super().__init__(name, breed, gender, color)

    def purr(self):
        print('Мурлыкать')


class Dog(AnimalBase):
    def __init__(
            self, name: str, breed: str, gender: str, color: str, age: int
    ) -> None:
        super().__init__(name, breed, gender, color)
        self.age = age

    def checking_for_old_age(self):
        if self.age >= 50:
            return 'Собака в возрасте'
        return 'молодая'

    def info(self) -> str:
        template = super().info()
        template += f'\nСтарая или молодая? {self.checking_for_old_age()}'
        return template


if __name__ == '__main__':
    cat_1 = Cat('Рыжик', 'A+', 'M', 'рыжий')
    print(cat_1.info())
    print(cat_1.purr())

    dog = Dog('Соня', 'Сибирская', 'девочка', 'Черная', 30)
    print(dog.info())
