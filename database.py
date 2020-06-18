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
#     password text
#     )""")
# conn.commit()
# conn.close()

# Insert Row
# c.execute("INSERT INTO users VALUES ('Admin', 'Admin@mail.com','password')")
# c.execute("INSERT INTO users VALUES ('JohnDoe', 'John@mail.com','password')")
# c.execute("INSERT INTO users VALUES ('Mary', 'Mary@mail.com', 'password1')")
# conn.commit()
# conn.close()

# Drop Table
# c.execute("DROP TABLE users")
# conn.commit()
# conn.close()

# Query DB
c.execute("SELECT * FROM users")
print(c.fetchall())
conn.close()

# c.execute("SELECT * FROM users WHERE username='Mary' ")
# print(c.fetchone())
# conn.close()
