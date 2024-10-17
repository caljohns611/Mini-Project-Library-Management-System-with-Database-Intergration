class Book:
    def __init__(self, title, author, genre, pub_date):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__pub_date = pub_date
        self.__available = True

    def details(self):
        return (f"Title: {self.__title}, Author: {self.__author}, "
                f"Genre: {self.__genre}, Publication Date: {self.__pub_date}, "
                f"Available: {'Yes' if self.__available else 'No'}")

    def title(self):
        return self.__title

    def borrow(self):
        self.__available = False

    def return_book(self):
        self.__available = True
