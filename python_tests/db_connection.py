import mysql.connector

# change hardcoded passwords
def get_conn():
    mydb = mysql.connector.connect(
      host="localhost",
      user="mysql",
      passwd="admin"
    )