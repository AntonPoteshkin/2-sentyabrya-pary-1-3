class Car:
    def __init__(self):
        self._engine_temperature = 20

    def start_engine(self):
        self._engine_temperature = 90
        print("Двигатель прогрет")

    def drive(self):
        if self._engine_temperature >= 90:
            print("Поехали!")
        else:
            print("Двигатель не прогрет! Сначала запустите start_engine()")


car = Car()


car.drive()


print(f"Температура двигателя (прямой доступ): {car._engine_temperature}")
car._engine_temperature = 100
print(f"Температура двигателя (изменена напрямую): {car._engine_temperature}")
car.drive()


car.start_engine()
car.drive()