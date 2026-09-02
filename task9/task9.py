import math

class Figure:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def get_coords(self):
        return self._x, self._y

    def set_coords(self, x, y):
        self._x = x
        self._y = y

    def calculate_area(self):
        pass

class Circle(Figure):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Круг: центр ({self._x}, {self._y}), радиус {self.radius}, площадь = {self.calculate_area():.2f}"

class Square(Figure):
    def __init__(self, x, y, side):
        super().__init__(x, y)
        self.side = side

    def calculate_area(self):
        return self.side ** 2

    def __str__(self):
        return f"Квадрат: центр ({self._x}, {self._y}), сторона {self.side}, площадь = {self.calculate_area():.2f}"

if __name__ == "__main__":
    figures = [
        Circle(0, 0, 5),
        Square(10, 10, 4),
        Circle(3, 7, 2.5),
        Square(-5, -5, 6),
        Circle(8, -3, 3)
    ]

    print("Информация о фигурах:")
    total_area = 0
    for fig in figures:
        print(fig)
        total_area += fig.calculate_area()

    print(f"\nОбщая площадь всех фигур: {total_area:.2f}")

    print("\nДемонстрация инкапсуляции:")
    print(f"Координаты первой фигуры: {figures[0].get_coords()}")
    figures[0].set_coords(10, 10)
    print(f"Новые координаты первой фигуры: {figures[0].get_coords()}")