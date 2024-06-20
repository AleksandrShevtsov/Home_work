import mysql.connector

dbconfig = {'host': 'ich-db.ccegls0svc9m.eu-central-1.rds.amazonaws.com',
            'user': 'ich1',
            'password': 'password',
            'database': 'ich_edit'}
connection = mysql.connector.connect(**dbconfig)

cursor = connection.cursor()
cursor.execute('SELECT * FROM users')
users = cursor.fetchall()
for user in users:
    print(f"{user[0]}: {user[1]}")
user_id = int(input('Enter user ID: '))
query = f'''
        SELECT users.name, product.prod, product.quantity
        FROM users
        JOIN sales ON users.id = sales.id
        JOIN product ON product.pid = sales.pid
        WHERE users.id IN ({user_id})
        '''

cursor.execute(query)
result = cursor.fetchall()
if result:
    for res in result:
        print(f'{res[0]} | {res[1].center(10)} | {res[2]}')
else:
    print('Information not found')

cursor.close()
connection.close()
