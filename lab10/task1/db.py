import sqlite3

def create_table():
    conn = sqlite3.connect('phonebook.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS phonebook (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            phone TEXT NOT NULL UNIQUE
        )
    ''')
    conn.commit()
    conn.close()
