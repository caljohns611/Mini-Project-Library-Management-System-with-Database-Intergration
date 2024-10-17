from menu import user_operations
from connect_mysql import connect_database

def add_user(cursor, name, library_id):
    query = "INSERT INTO Users (name, library_id) VALUES (%s, %s)"
    cursor.execute(query, (name, library_id))

def view_user(cursor):
    query = """
    SELECT u.id AS UsersID, u.name AS UsersName, u.library_id AS UsersLibrary_id
    FROM Users u
    WHERE u.id
    """
    
    cursor.execute(query)
    for user in cursor.fetchall():
        print(user)

def display_users(cursor):
    query = "SELECT * FROM Users"
    cursor.execute(query)
    for row in cursor.fetchall():
        print(row)

def manage_users(library_system):
    conn = connect_database()
    if conn is not None:
        try: 
            cursor = conn.cursor()
    
            while True:
                user_operations()
                user_choice = input("Select an option: ")
                
                if user_choice == '1':
                    name = input("Enter user name: ")
                    library_id = input("Enter user library ID: ")
                    add_user(cursor, name, library_id)
                    print("User added.")
                
                elif user_choice == '2':
                    input("Enter a users name to view users details: ")
                    view_user(cursor)
                
                elif user_choice == '3':
                    print("\nList of all users: ")
                    display_users(cursor)

                elif user_choice == '4':
                    break

        except Exception as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close()
            conn.close()