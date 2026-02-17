from lab01_intro_classes.tasks.book import Book


class Library:
    """Задача: library"""
    def __init__(self):
        self.books = []

    def add_book(self, title: str):
        self.title = title
        self.books.append(title)

