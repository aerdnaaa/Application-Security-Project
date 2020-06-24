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

# c.execute("""CREATE TABLE products (
#     name text,
#     image text,
#     description text,
#     price real,
#     category text
#     )""")
# conn.commit()
# conn.close()
# print('table created')

# Insert Row
# c.execute("INSERT INTO products VALUES ('Olympic Barbell', 'barbell.PNG', '2.2m Olympic Barbell', 130, 'barbell')")
# c.execute("INSERT INTO products VALUES ('Bench', 'bench.PNG', 'Incline Bench', 60, 'bench')")
# c.execute("INSERT INTO products VALUES ('Half Rack', 'halfrack.PNG', 'Half Rack. Good for squat.', 500, 'racks')")
# c.execute("INSERT INTO products VALUES ('Bumper Plates', 'rouge.PNG', 'Expensive bumper plates', 100, 'plates')")
# c.execute("INSERT INTO products VALUES ('Squat Rack', 'squat.PNG', 'Cheap and good', 130, 'racks')")
# c.execute("INSERT INTO products VALUES ('Flat Bench', 'bench2.PNG', 'Flat bench. Good for benching', 90, 'bench')")
# c.execute("INSERT INTO products VALUES ('Tri-grip Plates', 'nyp.PNG', 'Budget plates', 100, 'plates')")
# c.execute("INSERT INTO products VALUES ('Trap Bar', 'trap.PNG', 'Good stuff', 200, 'barbell')")
# conn.commit()
# conn.close()
# print('rows created')

# Drop Table
# c.execute("DROP TABLE products")
# conn.commit()
# conn.close()
# print('table dropped')

# Query DB
# c.execute("SELECT * FROM users WHERE username='' ")
# print(c.fetchall())
# conn.close()

# c.execute("SELECT * FROM users WHERE username='JohnDoe' ")
# user = c.fetchone()

c.execute("SELECT rowid, * FROM products")
print(c.fetchall())

# To see table names
# c.execute(" SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
# print(c.fetchone())

# c.execute("SELECT name FROM (SELECT * FROM sqlite_master UNION ALL SELECT * FROM sqlite_temp_master) WHERE type='table' ORDER BY name")
# print(c.fetchone())

# See all tables created in sqlite db
# c.execute("SELECT * FROM users WHERE username='' UNION SELECT sql, '2', '3', '4', '5' FROM sqlite_master-- ")
# print(c.fetchone())

conn.close()
