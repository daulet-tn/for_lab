import sqlite3


def insert_from_console():
    first_name = input("Enter name: ")
    phone = input("Enter phone: ")
    conn = sqlite3.connect('phonebook.db')
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO phonebook (first_name, phone) VALUES (?, ?)', (first_name, phone))
        conn.commit()
        print("Inserted successfully.")
    except sqlite3.IntegrityError:
        print("Phone number already exists.")
    conn.close()
