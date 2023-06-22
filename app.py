from flask import Flask, render_template, request
import pyodbc
from datetime import date

app = Flask(__name__)

# Establish connection to Azure database
server = 'bfisql.database.windows.net'
database = 'HRList'
username = 'abed'
password = 'P@$$w0rd.123'
driver = '{ODBC Driver 18 for SQL Server}'  # Use the appropriate driver

def get_database_connection():
    conn = pyodbc.connect(
        f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'
    )
    return conn

@app.route('/submit', methods=['POST'])
def submit_form():
    # Retrieve form data
    emp_number = request.form['emp_number']
    training_id = request.form['training_id']
    current_date = date.today().strftime('%Y-%m-%d')

    # Establish connection to Azure database
    conn = get_database_connection()

    # Insert data into the database
    cursor = conn.cursor()
    query = "INSERT INTO YourTable (EmpNumber, TrainingID, Date) VALUES (?, ?, ?)"

    cursor.execute(query, emp_number, training_id, current_date)
    conn.commit()

    # Close the database connection
    cursor.close()
    conn.close()

    # Redirect or render a success page
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
