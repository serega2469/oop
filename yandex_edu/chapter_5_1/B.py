class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def move(self, new_x: int, new_y: int):
        self.x += new_x
        self.y += new_y

    def length(self, point):
        result = ((point.x - self.x) ** 2 + (point.y - self.y) ** 2) ** 0.5
        return round(result, 2)