# SQL Examples

import sqlite3

# Connect to database
conn = sqlite3.connect("storage.db")

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
# c.execute("SELECT * FROM users")
# print(c.fetchall())
# conn.close()

# c.execute("SELECT * FROM users WHERE username='Mary' ")
# print(c.fetchone())
# conn.close()
