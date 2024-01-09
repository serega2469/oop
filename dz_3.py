class Tomato:
    states = ['Отсутствует', 'Цветение', 'Зеленый', 'Красный']

    def __init__(self, index, state=states[0]):
        self._index = index
        self._state = state


        
