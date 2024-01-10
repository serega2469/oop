# class Phone:
#     # Статические поля (переменные класса)
#     default_color = 'Grey'
#     default_model = 'C385'
#
#     def __init__(self, color, model):
#         self.color = color
#         self.model = model
#
#
# my_phone_red = Phone('Red', 'I495')
# # print(dir(my_phone_red))
# # print(my_phone_red.default_color)
# print(my_phone_red.color)
#
# # print(Phone.default_color)
# # Phone.default_color = 'Black'
# # print(Phone.default_color)

# 1. МЕТОДЫ ЭКЗЕМПЛЯРА КЛАССА (ОБЫЧНЫЕ МЕТОДЫ)

# class Phone:
#
#     def __init__(self, color, model):
#         self.color = color
#         self.model = model
#
#     # Обычный метод
#     # Первый параметр метода - self
#     def check_sim(self, mobile_operator):
#         if self.model == 'I785' and mobile_operator == 'MTS':
#             print('Your mobile operator is MTS')
#
#
# my_phone = Phone('red', 'I785')
# print(my_phone.check_sim('MTS'))

# 2. СТАТИЧЕСКИЕ МЕТОДЫ

# class Phone:
#
#     # Статический метод справочного характера
#     # Возвращает хэш по номеру модели
#     # self внутри метода отсутствует
#     @staticmethod
#     def model_hash(model):
#         if model == 'I785':
#             return 34565
#         elif model == 'K498':
#             return 45567
#         else:
#             return None
#
#     # Обычный метод
#     def check_sim(self, mobile_operator):
#         pass
#
#
# print(Phone.model_hash('K498'))

# МЕТОДЫ КЛАССА

# class Phone:
#
#     def __init__(self, color, model, os):
#         self.color = color
#         self.model = model
#         self.os = os
#
#     # Метод класса
#     # Принимает 1) ссылку на класс Phone и 2) цвет в качестве параметров
#     # Создает специфический объект класса Phone(особенность объекта в том, что это игрушечный телефон)
#     # При этом вызывается инициализатор класса Phone
#     # которому в качестве аргументов мы передаем цвет и модель,
#     # соответствующую созданию игрушечного телефона
#     @classmethod
#     def toy_phone(cls, color):
#         toy_phone = cls(color, 'ToyPhone', None)
#         return toy_phone
#
#     # Статический метод
#     @staticmethod
#     def model_hash(model):
#         pass
#
#     # Обычный метод
#     def check_sim(self, mobile_operator):
#         pass
#
#
# my_toy_phone = Phone.toy_phone('Red')
# print(my_toy_phone)

# УРОВНИ ДОСТУПА

# PROTECTED

# class Phone:
#
#     def __init__(self, color):
#         # Объявляем защищенное поле _color
#         self._color = color
#
#     @property  # Декоратор @property используется для методов класса
#     # и делает их «атрибутами только для чтения».
#     def color(self):
#         return self._color
#
#
# phone = Phone('Grey')
# print(phone.color)

# PRIVATE

class Phone:

    def __init__(self, color):
        # Объявляем приватное поле __color
        self.__color = color

    def user(self):
        return self.__color


phone = Phone('Grey')

# print(dir(phone))
# print(phone._Phone__color)
