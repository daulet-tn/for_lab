import sqlite3

def delete_entry(field, value):
    conn = sqlite3.connect('phonebook.db')
    cursor = conn.cursor()
    cursor.execute(f'DELETE FROM phonebook WHERE {field} = ?', (value,))
    conn.commit()
    print(f"{cursor.rowcount} row(s) deleted.")
    conn.close()
