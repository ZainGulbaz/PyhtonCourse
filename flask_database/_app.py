from flask import Flask;
import mysql.connector;

app= Flask(__name__);


# Database Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'school'

# Create a MySQL connection
mysql = mysql.connector.connect(
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD'],
    database=app.config['MYSQL_DB']
)

# Create a cursor
cursor = mysql.cursor(dictionary=True)

cursor.execute("SHOW DATABASES");
result=cursor.fetchall();
print(result);


