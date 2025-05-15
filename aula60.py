from dataclasses import dataclass, field
import datetime 

@dataclass
class Book:
    title: str
    author: str
    year_published: int
    genre: str = field(default='Unknown')
    is_bestseller: bool = field(default=False)

    def book_age(self) -> int:
        current_year = datetime.datetime.now().year
        return current_year - self.year_published

# Primeira instância
book = Book(title='1984', author='George Orwell', year_published=1949)
age = book.book_age()

# Segunda instância
book_2 = Book(title='Another Book', author='Another Author', year_published=2000)
age2 = book_2.book_age()

# Terceira instância
book_3 = Book(title='To Kill a Mockingbird', author='Harper Lee', year_published=1960, is_bestseller=True)
age3 = book_3.book_age()

# Quarta instância
book_4 = Book(title='The Great Gatsby', author='F. Scott Fitzgerald', year_published=1925, genre='Classic')
age4 = book_4.book_age()

# Impressão dos resultados
print(f'Book: {book.title}, Author: {book.author}, Age: {age} years')
print(f'Book: {book_2.title}, Author: {book_2.author}, Age: {age2} years')
print(f'Book: {book_3.title}, Author: {book_3.author}, Age: {age3} years, Bestseller: {book_3.is_bestseller}')
print(f'Book: {book_4.title}, Author: {book_4.author}, Age: {age4} years, Genre: {book_4.genre}')