from menu import book_operations
from connect_mysql import connect_database

def add_author(cursor, title, author_id, isbn, publication_date, availablity):
    query = "INSERT INTO Books (title, author_id, isbn, publication_date, availablity) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (title, author_id, isbn, publication_date, availablity))

def search_book(cursor):
    query = """
    SELECT b.id AS BooksID, b.title AS Bookstitle, b.author_id AS Booksauthor_id, b.isbn AS Booksisbn, b.publication_date AS Bookspublication_date, b.availability AS Booksavilability
    FROM Books b
    WHERE b.id
    """
    
    cursor.execute(query)
    for user in cursor.fetchall():
        print(user)

def display_books(cursor):
    query = "SELECT * FROM Books"
    cursor.execute(query)
    for row in cursor.fetchall():
        print(row)


def manage_books(library_system):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()

            while True:
                book_operations()
                book_choice = input("Select an option: ")
                
                if book_choice == '1':
                    title = input("Enter a book title: ")
                    author_id = input("Enter the author: ")
                    isbn = input("Enter the genre: ")
                    publication_date = input("Enter publication date: ")
                    availablity = input("Enter when the book will be available: ")
                    add_author(cursor, title, author_id, isbn, publication_date, availablity)
                    print("Book added.")
                
                elif book_choice == '2':
                    pass
                
                elif book_choice == '3':
                    pass
                    
                elif book_choice == '4':
                    input("Enter a book title to search: ")
                    search_book(cursor)
                elif book_choice == '5':
                    print("\nList of all books: ")
                    display_books(cursor)
                elif book_choice == '6':
                    break

        except Exception as e:
            print(f"Error: {e}")

        finally:
            conn.close()
            cursor.close()