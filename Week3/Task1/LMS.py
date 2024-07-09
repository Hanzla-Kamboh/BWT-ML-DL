# Library Management System - LMS.py

class Book:
    def __init__(self, title, author, pages):
        self._title = title
        self._author = author
        self._pages = pages

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        self._author = author

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, pages):
        self._pages = pages

    @classmethod
    def reading_time(cls, pages, speed=250):
        # Assuming average words per page is 300
        words = pages * 300
        return words / speed

class Ebook(Book):
    def __init__(self, title, author, pages, format):
        super().__init__(title, author, pages)
        self.format = format

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}, Format: {self.format}"

# Example usage:
try:
    my_book = Book("1984", "George Orwell", 328)
    print(f"Book: {my_book.title}, Author: {my_book.author}, Pages: {my_book.pages}")

    my_book.title = "Animal Farm"
    print(f"Updated Book: {my_book.title}, Author: {my_book.author}, Pages: {my_book.pages}")

    reading_time = Book.reading_time(my_book.pages)
    print(f"Reading time: {reading_time} minutes")

    my_ebook = Ebook("Brave New World", "Aldous Huxley", 268, "PDF")
    print(my_ebook)
except Exception as e:
    print(f"An error occurred: {e}")
