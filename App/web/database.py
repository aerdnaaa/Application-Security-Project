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
#     password text
#     )""")
# Commit command
# conn.commit()

# conn.close()

# Insert Row
# email = 'john@mail.com'
# c.execute("INSERT INTO users VALUES ('JohnDoe', '{}','password')".format(email))
# c.execute("INSERT INTO users VALUES ('Mary', 'password1')")
# conn.commit()
# print('done')

# Query DB
c.execute("SELECT * FROM users")
print(c.fetchall())

# c.execute("SELECT * FROM users WHERE username='Mary' ")
# print(c.fetchone())

# Close command
conn.close()
