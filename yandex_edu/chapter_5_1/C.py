class RedButton:
    def __init__(self):
        pass

    def click(self):
        pass

    def count(self):
        pass


if __name__ == '__main__':
    first_button = RedButton()
    second_button = RedButton()
    for time in range(5):
        if time % 2 == 0:
            second_button.click()
        else:
            first_button.click()
    print(first_button.count(), second_button.count())
