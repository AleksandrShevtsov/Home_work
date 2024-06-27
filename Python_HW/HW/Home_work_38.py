# В базе данных ich_edit три таблицы. Users с полями (id, name, age), Products с полями
# (pid, prod, quantity) и Sales с полями (sid, id, pid). Написать мини-интерфейс к базе
# данных, который умеет выполнять разные команды.
# 1. Выбрать таблицу для запроса. Предусмотреть возможность выбрать
# несколько таблиц. Вывести результат их соединения, если это возможно, или
# сообщение об ошибке.
# 2. Выбрать одно поле из выбранной таблицы и искомое значение этого поля.
# Вывести все подходящие строки
import tabulate
import mysql.connector

dbconfig = {'host': 'ich-db.ccegls0svc9m.eu-central-1.rds.amazonaws.com',
            'user': 'ich1',
            'password': 'password',
            'database': 'ich_edit'}


def connect_to_db(config):
    connection = mysql.connector.connect(**config)
    return connection


def disconnect_from_db(conn):
    conn.close()


def execute_query(query):
    connection = connect_to_db(dbconfig)
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    disconnect_from_db(connection)
    return result


def query_dict(filter):
    _query_dict = {
        'table': 'SELECT {field} FROM {table_name} {join} {filter}',
        'sales_join': 'JOIN sales s ON sales.pid = product.pid',
        'users_join': 'JOIN users u ON users.id = sales.id',
        
    }
    query = _query_dict.get(filter)
    return query


def table_list():
    query = 'SELECT table_name FROM information_schema.tables WHERE table_schema = "ich_edit" and table is not null'
    return execute_query(query)


def user_choice(choice):
    if '1' in choice:
        menu_one(table_name())
    if '2' in choice:
        pass  # выбор двойной таблицы
    if '3' in choice:
        pass  # применить фильтр


def menu_one(table_name):
    query = query_dict('table').format(field='*', table_name=table_name, join='', filter='')
    query = execute_query(query)
    table_name_query = query_dict('table').format(field='COLUMN_NAME',
                                                  table_name='INFORMATION_SCHEMA.COLUMNS',
                                                  join='',
                                                  filter='WHERE TABLE_NAME = {}'.format(table_name))
    headers = execute_query(table_name_query)
    print(headers)
    print(tabulate.tabulate(query, headers=headers))


def table_name():
    print('1 - users\n2 - products\n3 - sales')
    table_name = int(input('Enter table number: '))
    if table_name == 1:
        return 'users'
    if table_name == 2:
        return 'products'
    if table_name == 3:
        return 'sales'


def main():
    print('доступные таблицы:')
    print('Выберете один из следующих вариантов:')
    choice = input('1 - одна таблица\n2 - несколько таблиц\n3 - условие для поля\n')
    user_choice(choice)


if __name__ == '__main__':
    main()
