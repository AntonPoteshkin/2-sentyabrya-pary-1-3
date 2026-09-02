from task5.task5 import Figure


class Line(Figure):
    def __init__(self, coords, width, color, length):
        super().__init__(coords, width, color)
        self.length = length

    def info(self):
        print(f"Линия: координаты {self.coords}, ширина {self.width}, цвет {self.color}, длина {self.length}")


class Rect(Figure):
    def __init__(self, coords, width, color, height):
        super().__init__(coords, width, color)
        self.height = height

    def info(self):
        print(f"Прямоугольник: координаты {self.coords}, ширина {self.width}, цвет {self.color}, высота {self.height}")


class Ellipse(Figure):
    def __init__(self, coords, width, color, radius):
        super().__init__(coords, width, color)
        self.radius = radius

    def info(self):
        print(f"Эллипс: координаты {self.coords}, ширина {self.width}, цвет {self.color}, радиус {self.radius}")


line = Line((0, 0), 2, "красный", 10)
rect = Rect((5, 5), 3, "синий", 7)
ellipse = Ellipse((10, 10), 4, "зеленый", 6)

line.info()
rect.info()
ellipse.info()