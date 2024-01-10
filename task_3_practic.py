# НАСЛЕДОВАНИЕ

# Родительский класс
# class Phone:
#
#     # Инициализатор
#     def __init__(self):
#         self.is_on = False
#
#     # Включаем телефон
#     def turn_on(self):
#         self.is_on = True
#
#     # Если телефон включен, делаем звонок
#     def call(self):
#         if self.is_on:
#             print('Making call...')
#
#
# class MobilePhone(Phone):
#     def __init__(self):
#         super().__init__()
#         self.battery = 0
#
#     def charge(self, num):
#         self.battery = num
#         print(f'Charging battery up to ... {self.battery}%')
#
#
# my_mobile_phone = MobilePhone()
# # print(my_mobile_phone.turn_on())
# # print(my_mobile_phone.call())
# print(my_mobile_phone.charge(76))

# ПОЛИМОРФИЗМ

class Phone:

    def __init__(self):
        self.is_on = False

    def turn_on(self):
        pass

    def call(self):
        pass

    # Метод, который выводит короткую сводку по классу Phone
    def info(self):
        print(f'Class name: {Phone.__name__}')
        print(f'If phone is ON: {self.is_on}')


class MobilePhone(Phone):

    def __init__(self):
        super().__init__()
        self.battery = 0

    # Такой же метод, который выводит короткую сводку по классу MobilePhone
    # Обратите внимание, что названия у методов совпадают - оба метода называются info()
    # Однако их содержимое различается
    def info(self):
        print(f'Class name: {MobilePhone.__name__}')
        print(f'If mobile phone is ON: {self.is_on}')
        print(f'Battery level: {self.battery}')


# Демонстрационная функция

# Создаем список из классов
# В цикле перебираем список и для каждого элемента списка(а элемент - это класс)
# Создаем объект и вызываем метод info()
# Главная особенность: запись object.info() не дает информацию об объекте, для которого будет вызван метод info()
# Это может быть объект класса Phone, а может - объект класса MobilePhone
# И только в момент исполнения кода становится ясно, для какого именно объекта нужно вызывать метод info()
    def show_polymorphism():
        for item in [Phone, MobilePhone]:
            print('-------')
            object = item()
            object.info()
