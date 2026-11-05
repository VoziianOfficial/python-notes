import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()


# create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER
)
""")


# add user
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Anna", 25))

connection.commit()


# get all users
cursor.execute("SELECT * FROM users")

users = cursor.fetchall()

print("All users:", users)


# update user
cursor.execute("UPDATE users SET age = ? WHERE name = ?", (26, "Anna"))

connection.commit()


# get Anna
cursor.execute("SELECT * FROM users WHERE name = ?", ("Anna",))

user = cursor.fetchall()

print("Anna after update:", user)


# delete Anna
cursor.execute("DELETE FROM users WHERE name = ?", ("Anna",))

connection.commit()


# check users after delete
cursor.execute("SELECT * FROM users")

users = cursor.fetchall()

print("After delete:", users)


connection.close()
