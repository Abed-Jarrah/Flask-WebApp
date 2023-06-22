from flask import Flask, render_template, request
import pyodbc
import os

app = Flask(__name__)

# Retrieve the ODBC driver from the application settings
odbc_driver = os.environ.get('ODBC_DRIVER', 'ODBC Driver 18 for SQL Server')

# Replace the connection string with your Azure SQL Database connection string
conn_str = f"Driver={odbc_driver};Server=tcp:bfisql.database.windows.net,1433;Database=HRList;Uid=abed;Pwd=P@$$w0rd.123;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"

def get_database_connection():
    try:
        conn = pyodbc.connect(conn_str)
        return conn
    except pyodbc.Error as e:
        app.logger.error("Error connecting to the database: %s", e)
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        emp_number = request.form['emp_number']
        training_id = request.form['training_id']
        date = request.form['date']
        
        conn = get_database_connection()
        
        if conn:
            try:
                cursor = conn.cursor()
                query = "INSERT INTO dbo.[Table] ([Emp Number], [Training ID], [Date]) VALUES (?, ?, ?)"
                cursor.execute(query, (emp_number, training_id, date))
                conn.commit()
                return render_template('success.html')
            except pyodbc.Error as e:
                app.logger.error("Error executing SQL query: %s", e)
                return render_template('error.html')
            finally:
                cursor.close()
                conn.close()
        else:
            return render_template('error.html')
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
