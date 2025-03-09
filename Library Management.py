import mysql.connector
from mysql.connector import Error
from datetime import date

# Database connection function
def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",  # Replace with your MySQL username
            password="1234",  # Replace with your MySQL password
            database="library_db"
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

# Function to add a new member
def add_member(name, email, phone):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = "INSERT INTO members (name, email, phone) VALUES (%s, %s, %s)"
            cursor.execute(query, (name, email, phone))
            connection.commit()
            print("Member added successfully!")
        except Error as e:
            print(f"Error adding member: {e}")
        finally:
            cursor.close()
            connection.close()

# Function to add a new book
def add_book(title, author, quantity, price):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = "INSERT INTO books (title, author, quantity, price) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (title, author, quantity, price))
            connection.commit()
            print("Book added successfully!")
        except Error as e:
            print(f"Error adding book: {e}")
        finally:
            cursor.close()
            connection.close()

# Function to issue or buy a book
def issue_or_buy_book(member_id, book_id, transaction_type):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            # Check if the book is available
            cursor.execute("SELECT quantity FROM books WHERE book_id = %s", (book_id,))
            result = cursor.fetchone()
            if result and result[0] > 0:
                # Add transaction
                query = "INSERT INTO transactions (member_id, book_id, transaction_type, transaction_date) VALUES (%s, %s, %s, %s)"
                cursor.execute(query, (member_id, book_id, transaction_type, date.today()))
                # Update book quantity
                if transaction_type == "issue":
                    cursor.execute("UPDATE books SET quantity = quantity - 1 WHERE book_id = %s", (book_id,))
                connection.commit()
                print(f"Book {transaction_type}d successfully!")
            else:
                print("Book not available.")
        except Error as e:
            print(f"Error processing transaction: {e}")
        finally:
            cursor.close()
            connection.close()

# Function to display all members
def display_members():
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM members")
            members = cursor.fetchall()
            for member in members:
                print(f"ID: {member[0]}, Name: {member[1]}, Email: {member[2]}, Phone: {member[3]}")
        except Error as e:
            print(f"Error fetching members: {e}")
        finally:
            cursor.close()
            connection.close()

# Function to display all books
def display_books():
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM books")
            books = cursor.fetchall()
            for book in books:
                print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Quantity: {book[3]}, Price: {book[4]}")
        except Error as e:
            print(f"Error fetching books: {e}")
        finally:
            cursor.close()
            connection.close()

# Main menu
def main_menu():
    while True:
        print("\nLibrary Management System")
        print("1. Add Member")
        print("2. Add Book")
        print("3. Issue Book")
        print("4. Buy Book")
        print("5. Display Members")
        print("6. Display Books")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter member name: ")
            email = input("Enter member email: ")
            phone = input("Enter member phone: ")
            add_member(name, email, phone)
        elif choice == "2":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            quantity = int(input("Enter book quantity: "))
            price = float(input("Enter book price: "))
            add_book(title, author, quantity, price)
        elif choice == "3":
            member_id = int(input("Enter member ID: "))
            book_id = int(input("Enter book ID: "))
            issue_or_buy_book(member_id, book_id, "issue")
        elif choice == "4":
            member_id = int(input("Enter member ID: "))
            book_id = int(input("Enter book ID: "))
            issue_or_buy_book(member_id, book_id, "buy")
        elif choice == "5":
            display_members()
        elif choice == "6":
            display_books()
        elif choice == "7":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main_menu()

    