import sqlite3

def update_entry(old_value, new_value, field='first_name'):
    conn = sqlite3.connect('phonebook.db')
    cursor = conn.cursor()
    cursor.execute(f'''
        UPDATE phonebook
        SET {field} = ?
        WHERE {field} = ?
    ''', (new_value, old_value))
    conn.commit()
    print(f"{cursor.rowcount} row(s) updated.")
    conn.close()
