import psycopg2
import csv

# Подключение к базе данных
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="061214500802",
    host="localhost",
    port="5432"
)

# Создание курсора
cur = conn.cursor()

def create_table():
    cur.execute("""CREATE TABLE IF NOT EXISTS contacts(
                   id SERIAL PRIMARY KEY,
                   name VARCHAR(40) NOT NULL,
                   number VARCHAR(20) NOT NULL UNIQUE);""")
    conn.commit()

def insert_from_console():
    name = input("Name: ")
    number = input("Number: ")
    cur.execute("""INSERT INTO contacts (name, number)
                   VALUES (%s, %s);""", (name, number))
    conn.commit()

def insert_from_csv():
    try:
        with open("contacts.csv", newline='') as csv_file:
            r = csv.reader(csv_file)
            count = 0
            for row in r:
                if len(row) != 2:
                    continue
                try:
                    cur.execute("""INSERT INTO contacts (name, number)
                                   VALUES (%s, %s);""", (row[0], row[1]))
                    count += 1
                except psycopg2.errors.UniqueViolation:
                    conn.rollback()  # откат если номер уже есть
                    print(f"Контакт c номером {row[1]} уже существует.")
            conn.commit()
            print(f"{count} контактов добавлено из CSV.")
    except FileNotFoundError:
        print("Файл не найден")


def delete_contact():
    print("\nIf you want to delete contact \n1. By name\n2. By number")
    n = int(input())
    if n == 1:
        name = input("Name: ")
        cur.execute("""DELETE FROM contacts WHERE name = %s;""", (name,))
    elif n == 2:
        number = input("Number: ")
        cur.execute("""DELETE FROM contacts WHERE number = %s;""", (number,))
    else:
        print("Error")
    conn.commit()

def update_contact():
    print("\nYou want to update \n1. By contact's number\n2. By contact's name")
    n = int(input())
    if n == 1:
        number = input("Old number: ")
        name = input("New name: ")
        cur.execute("""UPDATE contacts 
                       SET name = %s
                       WHERE number = %s;""", (name, number))
    elif n == 2:
        name = input("Name: ")
        number = input("New number: ")

        # Проверка на наличие уже существующего номера
        cur.execute("SELECT * FROM contacts WHERE number = %s;", (number,))
        if cur.fetchone():
            print("К сожалению номер уже используется другим контактом.")
            return
        
        cur.execute("""UPDATE contacts 
                       SET number = %s
                       WHERE name = %s;""", (number, name))
    else:
        print("Error")
    conn.commit()


def search_contacts():
    print("\nHow you want search")
    print("1. By name")
    print("2. By number")
    print("3. By part of name")
    print("4. By part of number")
    print("5. Show all")
    n = int(input())
    if n == 1:
        name = input()
        cur.execute("""SELECT * FROM contacts
                       WHERE name = %s;""", (name, ))
    elif n == 2:
        number = input()
        cur.execute("""SELECT * FROM contacts
                       WHERE number = %s;""", (number, ))
    elif n == 3:
        na = input()
        cur.execute("""SELECT * FROM contacts
                       WHERE name LIKE %s;""", (f'%{na}%', ))
    elif n == 4:
        num = input()
        cur.execute("""SELECT * FROM contacts
                       WHERE number LIKE %s;""", (f'%{num}%', ))
    elif n == 5:
        cur.execute("""SELECT * FROM contacts
                       ORDER BY ID;""")
    else:
        print("Error")
    contacts = cur.fetchall()
    print("\nID\tName\tNumber\n---------------------------")
    if contacts:
        for contact in contacts:
            print(f"{contact[0]}\t{contact[1]}\t{contact[2]}")

create_table()

run = True
while run:
    print("\nOptions:\n1. Insert\n2. Delete\n3. Update\n4. Search\n5. Quit")
    n = int(input())
    if n == 1:
        print("\n1. By console\n2. By csv")
        m = int(input())
        if m == 1:
            insert_from_console()
        elif m == 2:
            insert_from_csv()
    if n == 2:
        delete_contact()
    if n == 3:
        update_contact()
    if n == 4:
        search_contacts()
    if n == 5:
        run = False
        cur.close()
        conn.close()