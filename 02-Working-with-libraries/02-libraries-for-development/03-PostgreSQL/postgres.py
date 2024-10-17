import psycopg2


def print_table():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clubs")
    print(cursor.fetchone())



conn = psycopg2.connect(database="football",
                        host="localhost",
                        user="football",
                        password="football",
                        port="30001")

print_table()