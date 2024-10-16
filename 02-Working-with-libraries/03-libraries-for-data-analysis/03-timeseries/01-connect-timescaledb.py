import psycopg2

CONNECTION = "postgres://postgres:password@localhost:5432/sampledata"

conn = psycopg2.connect(CONNECTION)
cursor = conn.cursor()
# use the cursor to interact with your database
cursor.execute("SELECT * FROM public.responsetimes")
print(cursor.fetchone())