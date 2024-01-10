import abc


class AbstractUser(abc.ABC):

    @abc.abstractmethod
    def get_username(self):
        pass


class BaseUser(AbstractUser):
    """Базовый класс пользователя."""

    def __init__(self,
                 username: str,
                 email: str,
                 password: str,
                 first_name: str,
                 last_name: str,
                 is_admin: bool = False,
                 is_vip: bool = False):
        self.__username = username
        self.__email = email
        self.__password = password
        self.first_name = first_name
        self.last_name = last_name
        self.is_admin = is_admin
        self.is_vip = is_vip

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    @property  # декоратор
    def email(self):  # доступ к email
        return self.__email

    @email.setter
    def email(self, value):  # установить новое значение атрибута
        if not isinstance(value, str):
            raise ValueError('Почта должна быть строкой')
        self.__email = value

    @property
    def username(self):
        return self.__username


class Admin(BaseUser):
    def __init__(self,
                 username: str,
                 email: str,
                 password: str,
                 first_name: str,
                 last_name: str,
                 is_admin: bool = False,
                 is_vip: bool = False):
        super().__init__(username,
                         email,
                         password,
                         first_name,
                         last_name,
                         is_admin,
                         is_vip)


if __name__ == '__main__':
    admin_1 = Admin('maks',
                    'maks@mail.com',
                    'strong_123',
                    'Max',
                    'Ivanov',
                    is_admin=True)
    print(admin_1.email)
    admin_1.email = 'dffdffd'
    print(admin_1.email)



