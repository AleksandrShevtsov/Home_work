# Задача: порекомендовать фильмы в определенной категории.
# Напишите программу, которая запрашивают информацию у пользователя, делает
# запросы в базу данных и выводит результат. Работаем с базой данных фильмов
# Sakila.


# 1. При запуске программы выводится список категорий (номер и название
# категории)

# 2. Пользователь может ввести номер категории

# 3. Программа выводит все фильмы в данной категории, но не более 10 фильмов.
# О фильме выводится следующая информация: название, год выпуска,
# описание. Опционально - список актеров.

# 4. Опционально, если останется время: поменяйте программу так, чтобы на шаге

# 1 пользователь мог выбрать поиск по категории или по имени актера. Если
# выбирается поиск по категории, то выводится список категории и уже
# описанный поиск по категории. Если выбирается поиск по актеру, то сначала
# пользователь вводит имя пользователя и делается поиск по базе актеров.
# Если указанный пользователем актер существует, то можно выбрать имя из
# предложенных вариантов и найти все фильмы с участием этого актера. В
# запросе для поиска по указанному имени актера можно пользоваться
# select/like чтобы убедиться, что актер(ы) с таким или похожим именем
# существуют в базе, прежде чем искать фильмы по имени актера.
# Рекомендации:
# 1. Сначала продумайте все запросы к базе данных, напишите их и проверьте, что
# они работают и возвращают результат.
# 2. Спроектируйте ваше Python-приложение, определив, какие функции
# выполняют запросы в базу, какие запрашивают информацию у пользователя, а
# какие - отображают результат на экране.
# 3. Убедитесь, что каждая функция выполняет одно действие, например, делает
# запрос в базу или считывает ответ пользователя с клавиатуры. Вы не
# помещаете текст sql запроса и логику печати результатов на экран в одну
# функцию.

import mysql.connector

dbconfig = {'host': 'ich-db.ccegls0svc9m.eu-central-1.rds.amazonaws.com',
            'user': 'ich1',
            'password': 'password',
            'database': 'sakila'}


def dbconnect(config):
    connection = mysql.connector.connect(**config)
    return connection


def dbdiscionnect(connection):
    connection.close()

def query():
    
    films_query = '''
                SELECT film.title, film.release_year, film.description FROM category
                JOIN film_category
                on category.category_id = film_category.category_id
                join film
                on film.film_id = film_category.film_id
                WHERE category.category_id in (%s)
                LIMIT 10
                '''
    actor_query = '''
                SELECT first_name, last_name FROM actor
                where first_name in (%s) and last_name in (%s);
                '''
    actor_name_query = '''
                SELECT first_name, last_name FROM actor
                where first_name in (%s);
                '''
    actor_last_name_query = '''
                SELECT first_name, last_name FROM actor
                where last_name in (%s);
                '''
    
    
def search_by_category():
    user_choice = input('Enter category number: ')
    
    cursor.execute(query(), (user_choice,))
    return cursor.fetchall()

def search_by_actor():
    user_choice = input('Enter actor name and last name: ').split()
    
    if len(user_choice) == 2:

        cursor.execute(actor_query, (user_choice[0].upper(), user_choice[1].upper()))
        actor = cursor.fetchall()
    elif len(user_choice) == 1:
        
        cursor.execute(actor_query, (user_choice[0].upper(),))
        actor = cursor.fetchall()
    else:
        print('wrong input')
        exit()
        
    if actor == []:
        print('actor not found')
        exit()
    
    film_list_query = '''
        SELECT film.title, film.release_year, film.description FROM film
        JOIN film_actor
        on film.film_id = film_actor.film_id
        join actor
        on actor.actor_id = film_actor.actor_id
        WHERE actor.first_name in (%s) and actor.last_name in (%s)
        LIMIT 10
        '''

    cursor.execute(film_list_query, (user_choice[0].upper(), user_choice[1].upper()))
    return cursor.fetchall()
    


def output(films):
    for film in films:
        print(f'{film[0].ljust(25)}| {str(film[1]).ljust(4)} | {film[2]}')
    

connection = dbconnect(dbconfig)
cursor = connection.cursor()
user_choice = input('serch by category - 1 or actor - 2: ')

if user_choice == '1' or user_choice.lower() == 'category':
    query = 'SELECT category_id, name FROM category'
    cursor.execute(query)
    categories = cursor.fetchall()
    for category in categories:
        print(f'{category[0]}: {category[1]}')
    films =search_by_category()
    output(films)

elif user_choice == '2' or user_choice.lower() == 'actor':
    films = search_by_actor()
    output()

else:
    print('wrong input')
    exit()

cursor.close()
dbdiscionnect(connection)
