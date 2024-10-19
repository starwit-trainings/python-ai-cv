import psycopg2

def connect():
    global conn;
    conn = psycopg2.connect(database="football",
                            host="localhost",
                            user="football",
                            password="football",
                            port="15432")

def get_all_clubs():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clubs")
    return cursor.fetchall()

def search_club_by_name(name):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clubs WHERE name LIKE %(name)s", { 'name': '%{}%'.format(name)})
    result = cursor.fetchone()
    return result

def disconnect():
    conn.commit()
    conn.close()
