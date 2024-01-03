import string


class Alphabet:  # В этом классе все правильно!
    def __init__(self, lang: str, letters: str) -> None:
        self.lang = lang
        self.letters = letters

    def print(self) -> None:
        print(self.letters)

    def letters_num(self) -> int:
        return len(self.letters)


class EngAlphabet(Alphabet):
    # Статическое свойство
    __letters_num = 0

    # 1. Согласно ТЗ конструктор этого класса ничего не принимает.
    """
    Условие:
    2. Создайте метод __init__(), внутри которого будет вызываться родительский метод __init__(). 
    В качестве параметров ему будут передаваться обозначение языка(например, 'En') и строка, состоящая 
    из всех букв алфавита(можно воспользоваться свойством ascii_uppercase из модуля string).
    """

    def __init__(self, lang, letters):
        super().__init__(lang, letters)

    def is_en_letter(self, letter: str):
        if letter in string.ascii_letters:  # 2. После того как исправите в конструкторе,
            # Вам здесь нужно проверить букву в self.letters, вместо string.ascii_letters
            print('Буква относится к английскому алфавиту')
        else:
            print('Не относится')

    def letters_num(self):
        return self.__letters_num

    @staticmethod
    def example() -> str:
        return ('Lorem ipsum dolor sit amet, '
                'consectetur adipiscing elit. '
                'Nunc posuere enim non dolor congue, sed.')


if __name__ == '__main__':
    # 3. Тут тоже изменится см. замечание №1
    user_1 = EngAlphabet('En', string.ascii_uppercase)

    user_1.print()
    print(user_1.letters_num())
    user_1.is_en_letter('F')
    user_1.is_en_letter('Щ')
    print(EngAlphabet.example())

# После того, как все исправите удалите мои комментарии из кода.
