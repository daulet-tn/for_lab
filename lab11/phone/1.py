import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="061214500802",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

create_function_sql = """
CREATE OR REPLACE FUNCTION search_contacts(pattern TEXT)
RETURNS TABLE(id INTEGER, name VARCHAR, number VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT c.id, c.name, c.number
    FROM contacts as c
    WHERE c.name ILIKE '%' || pattern || '%' OR c.number ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;
"""

cur.execute(create_function_sql)
conn.commit()

pattern = input("Введите имя или часть номера: ")
cur.execute("SELECT * FROM search_contacts(%s);", (pattern,))
results = cur.fetchall()
if results:
    print("\nНайденные контакты:\n---------------------------")
    print("id\tname\tnumber\n---------------------------")
    for row in results:
        print(f"{row[0]}\t{row[1]}\t{row[2]}")
    print("---------------------------")
else:
    print("Совпадений не найдено.")

cur.close()
conn.close()