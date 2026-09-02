class Figure:
    def __init__(self, coords, width, color):
        self.coords = coords
        self.width = width
        self.color = color

    def info(self):
        print(f"Координаты: {self.coords}, Ширина: {self.width}, Цвет: {self.color}")