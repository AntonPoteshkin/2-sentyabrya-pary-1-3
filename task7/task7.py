from task5.task5 import Figure


class Line(Figure):
    def __init__(self, coords, width, color, length):
        super().__init__(coords, width, color)
        self.length = length

    def draw(self):
        print("Рисуется линия...")


class Rect(Figure):
    def __init__(self, coords, width, color, height):
        super().__init__(coords, width, color)
        self.height = height

    def draw(self):
        print("Рисуется прямоугольник...")


class Ellipse(Figure):
    def __init__(self, coords, width, color, radius):
        super().__init__(coords, width, color)
        self.radius = radius

    def draw(self):
        print("Рисуется эллипс...")

figures = [
    Line((0, 0), 2, "красный", 10),
    Rect((5, 5), 3, "синий", 7),
    Ellipse((10, 10), 4, "зеленый", 6)
]

for figure in figures:
    figure.draw()