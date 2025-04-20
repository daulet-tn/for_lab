import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="061214500802",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

text_for_procedure = ("""
CREATE OR REPLACE PROCEDURE add_or_update_contact(p_name VARCHAR, p_number VARCHAR)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM contacts WHERE name = p_name) THEN
        UPDATE contacts
        SET number = p_number
        WHERE name = p_name;
    ELSIF EXISTS (SELECT 1 FROM contacts WHERE number = p_number) THEN
        UPDATE contacts
        SET name = p_name
        WHERE number = p_number;
    ELSE
        INSERT INTO contacts(name, number)
        VALUES (p_name, p_number);
    END IF;
END;
$$;

""")

cur.execute(text_for_procedure)
conn.commit()

name = input("Введите имя: ")
number = input("Введите номер: ")

cur.execute("CALL add_or_update_contact(%s, %s);", (name, number))
conn.commit()

cur.close()
conn.close()