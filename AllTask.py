# Задание 1
class DataBase:
    pk = 1
    title = "Классы и объекты"
    author = "Сергей Балакирев"
    views = 14356
    comments = 12


print("=" * 40)
print("Задание 1:")
print(DataBase.pk)
print(DataBase.title)
print(DataBase.author)
print(DataBase.views)
print(DataBase.comments)


# Задание 2
class Goods:
    title = "Мороженое"
    weight = 154
    tp = "Еда"
    price = 1024


Goods.price = 2048
Goods.inflation = 100

print("=" * 40)
print("Задание 2:")
print(Goods.title)
print(Goods.weight)
print(Goods.tp)
print(Goods.price)
print(Goods.inflation)


# Задание 3
class Car:
    pass


setattr(Car, 'model', "Тойота")
setattr(Car, 'color', "Розовый")
setattr(Car, 'number', "П111УУ77")

print("=" * 40)
print("Задание 3:")
print(Car.__dict__['color'])


# Задание 4
class Notes:
    uid = 1005435
    title = "Шутка"
    author = "И.С. Бах"
    pages = 2


print("=" * 40)
print("Задание 4:")
print(getattr(Notes, 'author'))


# Задание 5
class Dictionary:
    rus = "Питон"
    eng = "Python"


print("=" * 40)
print("Задание 5:")
print(getattr(Dictionary, 'rus_word', False))


# Задание 6
class TravelBlog:
    total_blogs = 0


tb1 = TravelBlog()
tb1.name = 'Франция'
tb1.days = 6
TravelBlog.total_blogs += 1

tb2 = TravelBlog()
tb2.name = 'Италия'
tb2.days = 5
TravelBlog.total_blogs += 1

print("=" * 40)
print("Задание 6:")
print(f"tb1: {tb1.name}, {tb1.days} дней")
print(f"tb2: {tb2.name}, {tb2.days} дней")
print(f"total_blogs: {TravelBlog.total_blogs}")


# Задание 7
class Figure:
    type_fig = 'ellipse'
    color = 'red'


fig1 = Figure()
fig1.start_pt = (10, 5)
fig1.end_pt = (100, 20)
fig1.color = 'blue'

del fig1.color

print("=" * 40)
print("Задание 7:")
print(*fig1.__dict__.keys())


# Задание 8
class Person:
    name = 'Сергей Балакирев'
    job = 'Программист'
    city = 'Москва'


p1 = Person()

print("=" * 40)
print("Задание 8:")
print(hasattr(p1, 'job'))
print('job' in p1.__dict__)


# Задание 9
class MediaPlayer:
    def open(self, file):
        self.filename = file

    def play(self):
        print(f"Воспроизведение {self.filename}")


media1 = MediaPlayer()
media2 = MediaPlayer()

media1.open("filemedia1")
media2.open("filemedia2")

print("=" * 40)
print("Задание 9:")
media1.play()
media2.play()


# Задание 10
class Graph:
    LIMIT_Y = [0, 10]

    def set_data(self, data):
        self.data = data

    def draw(self):
        filtered = [str(num) for num in self.data if self.LIMIT_Y[0] <= num <= self.LIMIT_Y[1]]
        print(" ".join(filtered))


graph_1 = Graph()
graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])

print("=" * 40)
print("Задание 10:")
graph_1.draw()

# Задание 11
import sys  # Добавлен импорт sys


class StreamData:
    def create(self, fields, lst_values):
        if len(fields) != len(lst_values):
            return False

        for field, value in zip(fields, lst_values):
            setattr(self, field, value)
        return True


class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res


print("=" * 40)
print("Задание 11:")
sd = StreamData()
result = sd.create(('id', 'title', 'pages'), ['1', 'Python', '100'])
print(f"Результат создания: {result}")
print(f"id: {sd.id}, title: {sd.title}, pages: {sd.pages}")


# Задание 12
class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def insert(self, data):
        for line in data:
            values = line.split()
            record = dict(zip(self.FIELDS, values))
            self.lst_data.append(record)

    def select(self, a, b):
        return self.lst_data[a:min(b + 1, len(self.lst_data))]


db = DataBase()
db.insert(["1 Сергей 35 120000", "2 Федор 23 12000", "3 Иван 13 1200"])

print("=" * 40)
print("Задание 12:")
print("Все данные:")
for record in db.lst_data:
    print(record)
print("Выборка [0:1]:")
for record in db.select(0, 1):
    print(record)


# Задание 13
class Translator:
    def add(self, eng, rus):
        if 'tr' not in self.__dict__:
            self.tr = {}
        self.tr.setdefault(eng, [])
        if rus not in self.tr[eng]:
            self.tr[eng].append(rus)

    def remove(self, eng):
        if eng in self.tr:
            del self.tr[eng]

    def translate(self, eng):
        return self.tr.get(eng, False)


tr = Translator()
tr.add('tree', 'дерево')
tr.add('car', 'машина')
tr.add('car', 'автомобиль')
tr.add('leaf', 'лист')
tr.add('river', 'река')
tr.add('go', 'идти')
tr.add('go', 'ехать')
tr.add('go', 'ходить')
tr.add('milk', 'молоко')

tr.remove('car')

print("=" * 40)
print("Задание 13:")
translations = tr.translate('go')
print(*translations)


# Задание 14
class Money:
    def __init__(self, money):
        self.money = money


my_money = Money(100)
your_money = Money(1000)

print("=" * 40)
print("Задание 14:")
print(f"my_money: {my_money.money}")
print(f"your_money: {your_money.money}")


# Задание 15
class Point:
    def __init__(self, x, y, color='black'):
        self.x = x
        self.y = y
        self.color = color


points = []
for i in range(1, 2001, 2):
    points.append(Point(i, i))

points[1].color = 'yellow'

print("=" * 40)
print("Задание 15:")
print(f"Количество точек: {len(points)}")
print(f"Точка 0: ({points[0].x}, {points[0].y}), цвет: {points[0].color}")
print(f"Точка 1: ({points[1].x}, {points[1].y}), цвет: {points[1].color}")
print(f"Точка 2: ({points[2].x}, {points[2].y}), цвет: {points[2].color}")

# Задание 16
import random


class Line:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Rect:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


elements = []
classes = [Line, Rect, Ellipse]

for _ in range(217):
    cls = random.choice(classes)
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    c = random.randint(0, 100)
    d = random.randint(0, 100)
    elements.append(cls(a, b, c, d))

for obj in elements:
    if isinstance(obj, Line):
        obj.sp = (0, 0)
        obj.ep = (0, 0)

print("=" * 40)
print("Задание 16:")
print(f"Количество элементов: {len(elements)}")
line_count = sum(1 for obj in elements if isinstance(obj, Line))
rect_count = sum(1 for obj in elements if isinstance(obj, Rect))
ellipse_count = sum(1 for obj in elements if isinstance(obj, Ellipse))
print(f"Line: {line_count}, Rect: {rect_count}, Ellipse: {ellipse_count}")
print(f"Первый элемент: {elements[0].__class__.__name__}, sp: {elements[0].sp}, ep: {elements[0].ep}")


# Задание 17
class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        a, b, c = self.a, self.b, self.c
        if not all(isinstance(x, (int, float)) for x in [a, b, c]) or a <= 0 or b <= 0 or c <= 0:
            return 1
        if a + b <= c or a + c <= b or b + c <= a:
            return 2
        return 3


print("=" * 40)
print("Задание 17:")
tr1 = TriangleChecker(3, 4, 5)
print(f"Стороны 3, 4, 5: {tr1.is_triangle()}")
tr2 = TriangleChecker(1, 1, 3)
print(f"Стороны 1, 1, 3: {tr2.is_triangle()}")
tr3 = TriangleChecker(0, 1, 2)
print(f"Стороны 0, 1, 2: {tr3.is_triangle()}")


# Задание 18
class Graph:
    def __init__(self, data, is_show=True):
        self.data = data.copy()
        self.is_show = is_show

    def set_data(self, data):
        self.data = data.copy()

    def show_table(self):
        if self.is_show:
            print(" ".join(map(str, self.data)))
        else:
            print("Отображение данных закрыто")

    def show_graph(self):
        if self.is_show:
            print(f"Графическое отображение данных: {' '.join(map(str, self.data))}")
        else:
            print("Отображение данных закрыто")

    def show_bar(self):
        if self.is_show:
            print(f"Столбчатая диаграмма: {' '.join(map(str, self.data))}")
        else:
            print("Отображение данных закрыто")

    def set_show(self, fl_show):
        self.is_show = fl_show


print("=" * 40)
print("Задание 18:")
data_graph = [1, 2, 3, 4, 5]
gr = Graph(data_graph)
gr.show_bar()
gr.set_show(False)
gr.show_table()


# Задание 19
class CPU:
    def __init__(self, name, fr):
        self.name = name
        self.fr = fr


class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume


class MotherBoard:
    def __init__(self, name, cpu, *mem_slots):
        self.name = name
        self.cpu = cpu
        self.total_mem_slots = 4
        self.mem_slots = list(mem_slots[:self.total_mem_slots])

    def get_config(self):
        config = []
        config.append(f"Материнская плата: {self.name}")
        config.append(f"Центральный процессор: {self.cpu.name}, {self.cpu.fr}")
        config.append(f"Слотов памяти: {self.total_mem_slots}")
        mem_str = '; '.join([f"{mem.name} - {mem.volume}" for mem in self.mem_slots])
        config.append(f"Память: {mem_str}")
        return config


cpu = CPU("Intel Core i7", "3.4 GHz")
mem1 = Memory("Kingston", "8GB")
mem2 = Memory("Corsair", "16GB")
mb = MotherBoard("ASUS", cpu, mem1, mem2)

print("=" * 40)
print("Задание 19:")
for line in mb.get_config():
    print(line)


# Задание 20
class Table:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class TV:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Notebook:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cart:
    def __init__(self):
        self.goods = []

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        if 0 <= indx < len(self.goods):
            del self.goods[indx]

    def get_list(self):
        return [f"{item.name}: {item.price}" for item in self.goods]


cart = Cart()
cart.add(TV("Samsung 55\"", 50000))
cart.add(TV("LG 42\"", 35000))
cart.add(Table("Дубовый стол", 20000))
cart.add(Notebook("MacBook Pro", 150000))
cart.add(Notebook("Lenovo ThinkPad", 80000))
cart.add(Cup("Кружка с котом", 500))

print("=" * 40)
print("Задание 20:")
print("Товары в корзине:")
for item in cart.get_list():
    print(f"  {item}")