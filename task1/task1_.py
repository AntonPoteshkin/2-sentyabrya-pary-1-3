class Cat:

    def __init__(self, breed, name, age):
        self.breed = breed
        self.name = name
        self.age = age


    def info(self):
        print(f"Порода: {self.breed}, Имя: {self.name}, Возраст: {self.age} лет")

cat1 = Cat("Сиамская", "Мурзик", 3)
cat2 = Cat("Британская", "Барсик", 5)
cat3 = Cat("Мейн-кун", "Леопольд", 2)

cat1.info()
cat2.info()
cat3.info()