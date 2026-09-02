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


class Triangle(Figure):
    def __init__(self, coords, width, color, side_a, side_b, side_c):
        super().__init__(coords, width, color)
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def draw(self):
        print("Рисуется треугольник...")


# Создаем список с объектами разных типов (включая новый Triangle)
figures = [
    Line((0, 0), 2, "красный", 10),
    Rect((5, 5), 3, "синий", 7),
    Ellipse((10, 10), 4, "зеленый", 6),
    Triangle((15, 15), 5, "желтый", 3, 4, 5)  # Новый класс без изменения цикла
]

# Цикл остался без изменений! Это и есть магия полиморфизма
for figure in figures:
    figure.draw()