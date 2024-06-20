import mysql.connector

# Database connection details
dbconfig = {
    'host': 'ich-db.ccegls0svc9m.eu-central-1.rds.amazonaws.com',
    'user': 'ich1',
    'password': 'password',
    'database': 'sakila'
}
def connect_to_db(config):
    connection = mysql.connector.connect(**config)
    return connection

def disconnect_from_db(conn):
    conn.close()

connection = connect_to_db(dbconfig)
cursor = connection.cursor()
cursor.execute("SELECT category_id, name FROM category LIMIT 10")
categories = cursor.fetchall()
print(categories)
cursor.close()
disconnect_from_db(connection)