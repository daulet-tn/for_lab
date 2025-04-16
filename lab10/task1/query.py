import sqlite3

def query_data(filter_by=None, value=None):
    conn = sqlite3.connect('phonebook.db')
    cursor = conn.cursor()
    if filter_by and value:
        cursor.execute(f'SELECT * FROM phonebook WHERE {filter_by} = ?', (value,))
    else:
        cursor.execute('SELECT * FROM phonebook')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()
