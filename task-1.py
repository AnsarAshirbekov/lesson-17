# Реализуйте класс «Автомобиль». Необходимо хранить в полях класса: название модели,
# год выпуска, производителя, объем двигателя, цвет машины, цену. Реализуйте методы класса
# для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.

class Car: # Создаем класс "Автомобиль"
    def __init__(self): # Создаем конструктор для задания атрибутов для класса 
        self.model = "" # Создаем атрибут для модели автомобиля со значением пустой строки
        self.year = 0 # Создаем атрибут для года выпуска автомобиля со значением целого числа
        self.manufacturer = "" # Создаем атрибут для названия производителя со значением пустой строки
        self.engine_capacity = 0.0 # Создаем атрибут для объема двигателя со значением десятичного числа
        self.color = "" # Создаем атрибут для цвета автомобиля со значением пустой строки
        self.price = 0.0 # Создаем атрибут для цены автомобиля со значением десятичного числа
    # Конструктор необходим для задания дефолтных (по умолчанию) значений для атрибутов класса
    # Создаем метод, который будет запрашивать от пользователя конкретные значения для атрибутов, которые потом перезапишутся 
    def input_data(self):
        self.model = input("Введите модель автомобиля: ")
        self.year = int(input("Введите год выпуска: "))
        self.manufacturer = input("Введите производителя: ")
        self.engine_capacity = float(input("Введите объем двигателя: "))
        self.color = input("Введите цвет автомобиля: ")
        self.price = float(input("Введите цену автомобиля: "))
    # Создаем метод для выдачи данных атрибутов, то есть его значений, сразу всех
    def display_data(self):
        print(f"Модель: {self.model}")
        print(f"Год выпуска: {self.year}")
        print(f"Производитель: {self.manufacturer}")
        print(f"Объем двигателя: {self.engine_capacity} л")
        print(f"Цвет: {self.color}")
        print(f"Цена: {self.price} тенге")
    # Создадим методы get-ры, которые будут нам выдавать значения атрбутов по отдельности
    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_manufacturer(self):
        return self.manufacturer

    def get_engine_capacity(self):
        return self.engine_capacity

    def get_color(self):
        return self.color

    def get_price(self):
        return self.price
    # Создадим методы set-ры, которые будут запрашивать у пользователя значения для атрибутов по отдельности
    def set_model(self):
        self.model = input("Введите модель автомобиля: ")

    def set_year(self):
        self.year = int(input("Введите год выпуска: "))

    def set_manufacturer(self):
        self.manufacturer = input("Введите производителя: ")

    def set_engine_capacity(self):
        self.engine_capacity = float(input("Введите объем двигателя: "))

    def set_color(self):
        self.color = input("Введите цвет автомобиля: ")

    def set_price(self):
        self.price = float(input("Введите цену автомобиля: "))

# Создадим один экземпляр класса и протестируем на нем все методы
car = Car()
car.input_data()
car.display_data()
car.set_model()
car.set_year()
car.set_manufacturer()
car.set_engine_capacity()
car.set_color()
car.set_price()
model = car.get_model()
year = car.get_year()
manufacturer = car.get_manufacturer()
engine_capacity = car.get_engine_capacity()
color = car.get_color()
price = car.get_price()
print(f"Модель: {model}")
print(f"Год выпуска: {year}")
print(f"Производитель: {manufacturer}")
print(f"Объем двигателя: {engine_capacity} л")
print(f"Цвет: {color}")
print(f"Цена: {price} тенге")