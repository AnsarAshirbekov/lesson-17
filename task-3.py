# Реализуйте класс «Стадион». Необходимо хранить в полях класса: название стадиона,
# дату открытия, страну, город, вместимость. Реализуйте методы класса для ввода данных,
# вывода данных, реализуйте доступ к отдельным полям через методы класса.

class Stadium: 
    def __init__(self): 
        self.name = "" 
        self.open_date = 0.0 
        self.country = "" 
        self.city = ""
        self.capacity = 0 
    
    def input_data(self):
        self.name = input("Введите название стадиона: ")
        self.open_date = float(input("Введите дату открытия стадиона: "))
        self.country = input("Введите страну расположения стадиона: ")
        self.city = input("Введите город расположения стадиона: ")
        self.capacity = int(input("Введите вместимость стадиона: "))
   
    def display_data(self):
        print(f"Название: {self.name}")
        print(f"Дата открытия: {self.open_date}")
        print(f"Страна: {self.country}")
        print(f"Город: {self.city}")
        print(f"Вместимость: {self.capacity} человек")
    
    def get_name(self):
        return self.name

    def get_open_date(self):
        return self.open_date

    def get_country(self):
        return self.country

    def get_city(self):
        return self.city

    def get_capacity(self):
        return self.capacity
    
    def set_name(self):
        self.name = input("Введите название стадиона: ")

    def set_open_date(self):
        self.open_date = float(input("Введите дату открытия стадиона: "))

    def set_country(self):
        self.country = input("Введите страну расположения стадиона: ")

    def set_city(self):
        self.city = input("Введите город расположения стадиона: ")

    def set_capacity(self):
        self.capacity = int(input("Введите вместимость стадиона: "))


stadium = Stadium()
stadium.input_data()
stadium.display_data()
stadium.set_name()
stadium.set_open_date()
stadium.set_country()
stadium.set_city()
stadium.set_capacity()
print(f"Название: {stadium.get_name()}")
print(f"Дата открытия: {stadium.get_open_date()}")
print(f"Страна: {stadium.get_country()}")
print(f"Город: {stadium.get_city()}")
print(f"Вместимость: {stadium.get_capacity()} человек")