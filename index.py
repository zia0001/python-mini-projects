<<<<<<< HEAD
from fastapi import FastAPI         # framework to build apis
from pydantic import BaseModel      # helps in data validation
from typing import List


app = FastAPI()                     # an app instance of FastAPI class

class Tea(BaseModel):               #a schema/model of tea data (with validation)
  id: int
  name: str
  origin: str

teas: List[Tea] =[]                 # will store multiple Tea objects


@app.get("/")
def read_root():
   return("welcome here")

@app.get("/teas")
def get_teas():
  return teas

@app.post("/teas")
def add_tea(tea: Tea):                   # the request must have all Tea fields now
    teas.append(tea)                     # expect that the request sender will send tea
    return tea
                  

@app.put("/teas/{tea_id}")
def update_tea(tea_id: int, updated_tea: Tea):
    for index, tea in enumerate(teas):
       if tea.id == tea_id:
          teas[index] = updated_tea
          return updated_tea
    return{"error":"Tea not found"}

@app.delete("/teas/{tea_id}")
def delete_tea(tea_id: int):
   for index, tea in enumerate(teas):
      if tea.id ==tea_id:
         deleted = teas.pop(index)
         return deleted
   return {"error": "Tea is not "}
   
=======
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
>>>>>>> caa0ab81b6b7f6a0cd7cdca1a6346796c8fd8487
