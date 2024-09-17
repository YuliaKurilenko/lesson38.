import sqlite3
import asyncio
connection = sqlite3.connect('database.db')
cursor= connection.cursor()

def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INT,
    title TEXT,
    description TEXT,
    price INT
    )
    '''),
    connection.commit()

initiate_db()

# вариант 1
def get_all_products():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    products=cursor.execute('SELECT * FROM Products').fetchall()
    connection.commit()
    return products


connection.commit()
connection.close()



def add_user(username, email, age):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM Users")
    total_us = cursor.fetchone()[0] + 1
    cursor.execute(f'''
     INSERT INTO Users VALUES('{total_us}', '{username}', '{email}', '{age}', '1000')
     ''')
    connection.commit()
    connection.close()
def is_included(username):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    is_inc = True
    check_user = cursor.execute('SELECT * FROM Users WHERE username = ?', (username,))
    if check_user.fetchone() is None:
        is_inc = False
    connection.commit()
    connection.close()
    return is_inc




