import mysql.connector

# change hardcoded passwords
def get_conn():
    mydb = mysql.connector.connect(
      host="db",
      user="root",
      passwd="admin"
    )