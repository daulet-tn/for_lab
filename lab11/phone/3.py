import psycopg2

conn = psycopg2.connect(
    dbname = "postgres",
    user = "postgres",
    password = "061214500802",
    host = "localhost"
)

cur = conn.cursor()

text_for_procedure = ("""
CREATE OR REPLACE PROCEDURE delete_data(dna VARCHAR, dnum VARCHAR)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM contacts as c
    WHERE (dna IS NOT NULL AND c.name = dna)
        OR (dnum IS NOT NULL AND c.number = dnum);
END;
$$;
""")

cur.execute(text_for_procedure)
conn.commit()

name = input("Введите имя пользователя (или оставьте пустым): ")
number = input("Введите номер телефона (или оставьте пустым): ")

name = name if name != "" else None
number = number if number != "" else None

if name is None and number is None:
    print("Нужно ввести хотя бы имя или номер.")
else:
    cur.execute("CALL delete_data(%s, %s);", (name, number))
    conn.commit()
    print("Контакт удалён, если он существовал.")

cur.close()
conn.close()