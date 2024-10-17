from menu import author_operations
from connect_mysql import connect_database

def add_author(cursor, name, biography):
    query = "INSERT INTO Authors (name, biography) VALUES (%s, %s)"
    cursor.execute(query, (name, biography))

def view_user(cursor):
    query = """
    SELECT a.id AS AuthorID, a.name AS AuthorName, a.biography AS Authorsbiography
    FROM Authors a
    WHERE a.id
    """
    
    cursor.execute(query)
    for author in cursor.fetchall():
        print(author)

def display_authors(cursor):
    query = "SELECT * FROM Authors"
    cursor.execute(query)
    for row in cursor.fetchall():
        print(row)


def manage_authors(library_system):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()

            while True:
                author_operations()
                author_choice = input("Select an option: ")
                if author_choice == '1':
                    name = input("Enter the authors name: ")
                    biography = ("Enter a biography for the author: ")
                    add_author(cursor, name, biography)
                    print("Author added.")
                elif author_choice == '2':
                    name = input("Enter author name to view details: ")
                    view_user(cursor)
                elif author_choice == '3':
                    print("\nList of all authors: ")
                    display_authors(cursor)
                elif author_choice == '4':
                    break

        except Exception as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close()
            conn.close()