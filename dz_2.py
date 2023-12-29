import string


class Alphabet:

    def __init__(self, lang: str, letters: str):
        self.lang = lang
        self.letters = letters

    def print(self):
        print(self.letters)

    def letters_num(self):
        return len(self.letters)


class EngAlphabet(Alphabet):
    # Статическое свойство
    __letters_num = 0

    def __init__(self, lang, letters):
        super().__init__(lang, letters)

    def is_en_letter(self, letter: str):
        if letter in string.ascii_letters:
            print('Буква относится к английскому алфавиту')
        else:
            print('Не относится')

    def letters_num(self):
        return super().letters_num()

    @staticmethod
    def example():
        return 'Plkflf;dfd;lfjd;lfjd;;;;'


if __name__ == '__main__':
    user_1 = EngAlphabet('En', string.ascii_uppercase)
    user_1.print()
    print(user_1.letters_num())
    user_1.is_en_letter('Щ')
