import sqlite3


connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)


users = [
    (1, 'jose', '1234'),
    (2, 'bob', 'asdf'),
    (3, 'anne', 'xyz')]

insert_query = "INSERT INTO users VALUEs (?, ?, ?)"
cursor.executemany(insert_query, users)

select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)

connection.commit()
connection.close()
