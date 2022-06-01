from fastapi import FastAPI
import pyodbc

app = FastAPI()
driver = '[ODBC 13 driver]'
server = 'tcp:komal1.database.windows.net'
database = 'komal1'
username = 'komal'
password = 'Bhagavan@123'
eat = {1: "komal"}


@app.get("/get/{mess}")
def select(mess):
    with pyodbc.connect(
            'DRIVER=' + driver + '; SERVER=tcp:' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM dbo.username WHERE id = ?", mess)
            row = cursor.fetchall()
            a = row[0][1]

    return {"here you go": a}


@app.post("/post/{mess}")
def rr(mess):
    with pyodbc.connect(
            'DRIVER=' + driver + '; SERVER=tcp:' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password) as conn:
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO dbo.username(name) VALUES(?)", mess)
            cursor.execute("SELECT MAX(id) FROM dbo.username")
            row = cursor.fetchall()
            i = row[0][0]
    return {"status": "successfully posted the id is: " + str(i)}