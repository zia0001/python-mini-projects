import psycopg2

hostname = 'localhost'
database = 'CRUD'
username = 'postgres'
pwd = '12345'
port_id  = 5432
conn = None
cur = None

try:

    conn = psycopg2.connect(           #return object(conn) = the pipeline to the database
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id)

    cur = conn.cursor()                # cur() is method of conn object...a worker that sends SQL through that pipeline
    def create_table():

        create_script= ''' CREATE TABLE IF NOT EXISTS employees (
                                id int PRIMARY KEY,
                                name varchar(50) NOT NULL,
                                salary int,
                                dept_id varchar(50)) '''
        cur.execute(create_script)


    def insert_in_table(cursor):

         insert_script = 'INSERT INTO employees(id, name, salary, dept_id) Values(%s, %s, %s, %s)'   # using placeholders instead of specifying all values
         insert_values = 101, 'zia', 300000, 'it101'         # Always use parameters to prevent SQL injection.
         cursor.execute(insert_script,insert_values)





    def update_table():
        update_script = "UPDATE employees SET name = %s WHERE dept_id = %s"
        update_values = ('ziauddin', 'it101')
        cur.execute(update_script, update_values)

    def delete_from_table():
        delete_script = "DELETE FROM employees WHERE id = %s"
        delete_values = (101,)
        cur.execute (delete_script, delete_values)


    insert_in_table(cur)
    conn.commit()           #save changes to database

    cur.execute("SELECT * FROM employees")
    rows = cur.fetchall()
    print("Current table data:", rows)



except Exception as error:
    print(error)
finally:
    if cur is not None:        #only if the cursor is open then close it
        cur.close()
    if conn is not None:       #only if the db connection was open then close it
        conn.close()
