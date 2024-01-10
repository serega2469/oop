class Tomato:
    states = {
        1: 'Отсутствует',
        2: 'Цветение',
        3: 'Зеленый',
        4: 'Красный'
    }

    def __init__(self, index):
        self.__current_state = 1
        self._index = index
        self._state = Tomato.states.get(self.__current_state)

    @staticmethod
    def __get_states_length():
        return len(Tomato.states)

    def grow(self):
        if self.__current_state >= Tomato.__get_states_length():
            print('Помидоры находятся в финальной стадии')
            return
        self.__current_state += 1

    def is_ripe(self):
        return self.__current_state == Tomato.__get_states_length()

    def __str__(self):
        return f'Tomato {self._index}'
class TomatoBush:
    def __init__(self, tomato_count: int):
        self.__tomato_count = tomato_count
        self.tomatoes = [
            Tomato(i) for i in range(1, self.__tomato_count + 1)
        ]
        # Вывод списка обьектов Tomato
        print(*self.tomatoes, sep='\n')


if __name__ == '__main__':
    t_1 = TomatoBush(5)
