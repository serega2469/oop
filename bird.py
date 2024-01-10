# TODO: Создать класс птиц
import abc
from abc import ABC


class AbstractBird(abc.ABC):
    @abc.abstractmethod
    def get_bird_name(self):
        pass

    @abc.abstractmethod
    def wings(self):
        pass


class BaseBird(AbstractBird):
    def __init__(self, name: str,
                 password: str,
                 email: str,
                 first_name: str,
                 age: str):
        self._password = password
        self._email = email
        self._first_name = first_name

    def get_bird_name(self):
        return self._first_name

    def wings(self):
        print('Лечу')
