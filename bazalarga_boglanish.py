# sqlite3 ma'lumotlar bazasi bilan ishlash
# import sqlite3

# # Ulanish
# conn = sqlite3.connect('my_database.db')

# # Cursor olish
# cursor = conn.cursor()

# # Jadval yaratish
# cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")

# # Ma'lumot qo‘shish
# cursor.execute("INSERT INTO users (name) VALUES (?)", ('Ali',))

# # Saqlash va yopish
# conn.commit()
# conn.close()





# MySQL / MariaDB

# import mysql.connector

# # Ulanish
# conn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="your_password",
#     database="test_db"
# )

# # Cursor
# cursor = conn.cursor()

# # Ma'lumot olish
# cursor.execute("SELECT * FROM users")
# results = cursor.fetchall()
# for row in results:
#     print(row)

# conn.close()






# PostgreSQL
# import psycopg2

# # Ulanish
# conn = psycopg2.connect(
#     host="localhost",
#     database="test_db",
#     user="postgres",
#     password="your_password"
# )

# cursor = conn.cursor()

# # Jadval yaratish
# cursor.execute("CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, name TEXT)")
# conn.commit()

# conn.close()















# pip install pymongo
# MongoDB Atlas
# from pymongo import MongoClient

# # MongoDB Atlas URI orqali ulanish
# uri = ""
# client = MongoClient(uri)

# # Ma'lumotlar bazasi nomi (misol uchun 'test') va kolleksiya (masalan 'users')
# db = client['test']            # o‘zingizdagi bazani shu yerga yozing
# collection = db['chats']       # o‘zingizdagi kolleksiyani shu yerga yozing

# # Ma’lumotlarni o‘qish
# documents = collection.find()

# # Ekranga chiqarish
# for doc in documents:
#     print(doc)
