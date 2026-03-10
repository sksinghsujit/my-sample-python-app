import os
import mysql.connector
from flask import Flask, render_template

app = Flask(__name__)

def get_db_connection():
    # Reading variables from your OpenShift environment
    return mysql.connector.connect(
        host=os.environ['MYSQL_HOSTNAME'],
        user=os.environ['MYSQL_USER'],
        password=os.environ['MYSQL_PASSWORD'],
        database=os.environ['MYSQL_DATABASE']
    )

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM employees')
    employees = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', employees=employees)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
