from library import LibraryManagement
from menu import main_menu
from manage_book import manage_books
from manage_user import manage_users
from manage_author import manage_authors

class CLI:
    def __init__(self):
        self.library_system = LibraryManagement()

    def run(self):

        while True:
            main_menu()
            choice = input("Select an option: ")

            if choice =='1':
                manage_books(self.library_system)
            elif choice == '2':
                manage_users(self.library_system)
            elif choice == '3':
                manage_authors(self.library_system)
            elif choice == '4':
                print("Quitting the application.")
                break