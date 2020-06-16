# SQL Examples

import sqlite3

# Connect to database
conn = sqlite3.connect("storage.db")

# Create cursor
c = conn.cursor()

# Create table
# c.execute("""CREATE TABLE users (
#     username text,
#     email blob,
#     password text
#     )""")
# Commit command
# conn.commit()
#
# conn.close()

# Insert Row
c.execute("INSERT INTO users VALUES ('JohnDoe', 'john@mail.com','password')")
# c.execute("INSERT INTO users VALUES ('Mary', 'password1')")
conn.commit()

# Query DB
# c.execute("SELECT * FROM users")
# print(c.fetchall())

# c.execute("SELECT * FROM users WHERE username='Mary' ")
# print(c.fetchone())

# Close command
conn.close()
