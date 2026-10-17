class Book:
    def __init__(self, title: str, author:str, isbn: str, year: int, pages: int):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year
        self.pages = pages
        self._is_available = True
        self._last_read_pages = 0
    def __eq__(self, other):
        return self.isbn == other.year

    def __lt__(self, other):
        return self.year < other.year
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', '{self.isbn}', {self.year}, {self.pages})"

    @property
    def is_available(self):
        return self._is_available

    @property
    def last_read_pages(self):
        return self._last_read_pages

    def borrow(self):
        if not self._is_available : raise ValueError
        self._is_available = False

    def give_back(self, pages_read: int):
        if pages_read > self.pages: raise ValueError
        self._is_available = True
        self._last_read_pages = pages_read

class Reader:
    def __init__(self, name: str):
        self.name = name
        self.books = []
        self.pages_read = 0

    def __repr__(self):
        return f"Reader('{self.name}')"

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book: Book):
        self._books.append(book)

    def find_by_isbn(self, isbn: str):
        for book in self._books:
            if book.isbn == isbn:
                return book
        return None

    def find_by_author(self, author: str):
        return [book for book in self._books if book.author == author]

    def lend(self, isbn: str, reader: Reader):
        book = self.find_by_isbn(isbn)
        if book is None:
            raise KeyError(f"Книга с ISBN {isbn} не найдена")
        if not book.is_available:
            raise ValueError(f"Книга с ISBN {isbn} уже выдана")
        book.borrow()
        reader.books.append(book)

    def take_back(self, isbn: str, reader: Reader, pages_read: int):
        book = self.find_by_isbn(isbn)
        if book is None:
            raise ValueError(f"Книга с ISBN {isbn} не найдена")
        if book not in reader.books:
            raise ValueError(f"У читателя {reader.name} нет книги с ISBN {isbn}")
        if pages_read < 0 or pages_read > book.pages:
            raise ValueError(f"Недопустимое число страниц: {pages_read}")

        book.give_back(pages_read)
        reader.books.remove(book)
        reader.pages_read += pages_read

    def available(self):
        return [book for book in self._books if book.is_available]

    def unfinished(self):
        return [
            book for book in self._books
            if 0 < book.last_read_pages < book.pages
        ]

    def __len__(self):
        return len(self._books)