class Author:
    def __init__(self, name, biography):
        self.__name = name
        self.__biography = biography

    def details(self):
        return f"Author Name: {self.__name}, Biography: {self.__biography}"
