import abc


class Animal(abc.ABC):

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


class Cat(Animal):
    def __init__(self, name, breed, gender, color):
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

    def info(self):
        template = (f'\nМеня зовут {self.name}'
                    f'\nПорода: {self.breed}'
                    f'\nПол: {self.gender}')

        return template


class Dog(Cat):
    def __init__(self, name, breed, gender, color, age):
        super().__init__(name, breed, gender, color)
        self.age = age

    def checking_for_old_age(self):
        if self.age >= 50:
            return 'Собака в возрасте'
        return 'молодая'

    def info(self):
        template = super().info()
        template += f'\nСтарая или молодая? {self.checking_for_old_age()}'
        return template


dog = Dog('Соня', 'Сибирская', 'девочка', 'Черная', 30)
print(dog.info())
