import string


class Alphabet:
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

    def __init__(self):
        super().__init__(lang='En', letters=string.ascii_uppercase)

    def is_en_letter(self, letter: str):
        """

        :param letter:
        :return:
        """
        if letter.upper() in self.letters:  # При проверке, переданный
            # аргумент лучше перевести к верхнему регистру
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

    # """Минимальное количество постов."""
    # MIN_AMOUNT = 15

    # https://thomas-cokelaer.info/tutorials/sphinx/docstring_python.html
    # reStructuredText
    user_1 = EngAlphabet()

    user_1.print()
    print(user_1.letters_num())
    user_1.is_en_letter('F')
    user_1.is_en_letter('Щ')
    print(EngAlphabet.example())
