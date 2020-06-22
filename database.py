# SQL Examples
from flaskr import file_directory
import sqlite3, os

# Connect to database
conn = sqlite3.connect(os.path.join(file_directory, "storage.db"))

# Create cursor
c = conn.cursor()

# Create table
# c.execute("""CREATE TABLE users (
#     username text,
#     email text,
#     password text,
#     question text,
#     answer text
#     )""")
# conn.commit()
# conn.close()
# print('table created')

# Insert Row
# c.execute("INSERT INTO users VALUES ('Admin', 'Admin@mail.com','password', 'What is the middle name of your mother?', 'test')")
# c.execute("INSERT INTO users VALUES ('JohnDoe', 'John@mail.com','password', 'Where was the first place you went to on a plane?', 'singapore')")
# c.execute("INSERT INTO users VALUES ('Mary', 'Mary@mail.com', 'password1', 'What is the name of your favourite teacher?', 'bro')")
# conn.commit()
# conn.close()
# print('rows created')

# Drop Table
# c.execute("DROP TABLE users")
# conn.commit()
# conn.close()

# Query DB
# c.execute("SELECT * FROM users WHERE username='' ")
# print(c.fetchall())
# conn.close()

# c.execute("SELECT * FROM users WHERE username='JohnDoe' ")
# user = c.fetchone()

# To see table names
# c.execute(" SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
# print(c.fetchone())

# c.execute("SELECT name FROM (SELECT * FROM sqlite_master UNION ALL SELECT * FROM sqlite_temp_master) WHERE type='table' ORDER BY name")
# print(c.fetchone())

# c.execute("SELECT * FROM users WHERE username='' UNION SELECT sql, '2', '3', '4', '5' FROM sqlite_master-- ")
# print(c.fetchone())

conn.close()
