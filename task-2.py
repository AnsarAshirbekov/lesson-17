# Реализуйте класс «Книга». Необходимо хранить в полях класса: название книги, год
# выпуска, издателя, жанр, автора, цену. Реализуйте методы класса для ввода данных, вывода
# данных, реализуйте доступ к отдельным полям через методы класса.

class Book: 
    def __init__(self): 
        self.name = "" 
        self.year = 0 
        self.publisher = "" 
        self.genre = ""
        self.author = "" 
        self.price = 0.0 
    
    def input_data(self):
        self.name = input("Введите название книги: ")
        self.year = int(input("Введите год выпуска книги: "))
        self.publisher = input("Введите издателя книги: ")
        self.genre = input("Введите жанр книги: ")
        self.author = input("Введите автора книги: ")
        self.price = float(input("Введите цену книги: "))
   
    def display_data(self):
        print(f"Название: {self.name}")
        print(f"Год выпуска: {self.year}")
        print(f"Издатель: {self.publisher}")
        print(f"Жанр: {self.genre}")
        print(f"Автор: {self.author}")
        print(f"Цена: {self.price} тенге")
    
    def get_name(self):
        return self.name

    def get_year(self):
        return self.year

    def get_publisher(self):
        return self.publisher

    def get_genre(self):
        return self.genre

    def get_author(self):
        return self.author

    def get_price(self):
        return self.price
    
    def set_name(self):
        self.name = input("Введите название книги: ")

    def set_year(self):
        self.year = int(input("Введите год выпуска книги: "))

    def set_publisher(self):
        self.publisher = input("Введите издателя книги: ")

    def set_genre(self):
        self.genre = input("Введите жанр книги: ")

    def set_author(self):
        self.author = input("Введите автора книги: ")

    def set_price(self):
        self.price = float(input("Введите цену книги: "))


book = Book()
book.input_data()
book.display_data()
book.set_name()
book.set_year()
book.set_publisher()
book.set_genre()
book.set_author()
book.set_price()
print(f"Название: {book.get_name()}")
print(f"Год выпуска: {book.get_year()}")
print(f"Издатель: {book.get_publisher()}")
print(f"Жанр: {book.get_genre()}")
print(f"Автор: {book.get_author()}")
print(f"Цена: {book.get_price()}")