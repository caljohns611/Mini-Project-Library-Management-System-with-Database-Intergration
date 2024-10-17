from book import Book
from user import User
from author import Author

class LibraryManagement:
    def __init__(self):
        self.books = []     
        self.users = []     
        self.authors = []   

    def add_book(self, title, author, genre, pub_date):
        new_book = Book(title, author, genre, pub_date)
        self.books.append(new_book)

    def add_user(self, name, library_id):
        new_user = User(name, library_id)
        self.users.append(new_user)

    def add_author(self, name, biography):
        new_author = Author(name, biography)
        self.authors.append(new_author)

    def borrow_book(self, library_id, book_title):
        return "Book borrowed successfully"

    def return_book(self, library_id, book_title):
        return "Book returned successfully"

    def display_books(self):
        for book in self.books:
            print(book.details())

    def display_users(self):
        for user in self.users:
            print(user.details())

    def display_authors(self):
        for author in self.authors:
            print(author.details())

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def find_user(self, library_id):
        for user in self.users:
            if user.library_id == library_id:
                return user
        return None

    def find_author(self, name):
        for author in self.authors:
            if author.name == name:
                return author
        return None
