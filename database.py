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
#     selling_price real,
#     cost_price real,
#     category text,
#     status text
#     )""")
# conn.commit()
# conn.close()
# print('table created')

# c.execute("""CREATE TABLE paymentdetails (
#     username text,
#     name text,
#     ccnumber text,
#     expiry text,
#     cvv integer
#     )""")
# conn.commit()
# conn.close()
# print('table created')

# Insert Row
# c.execute("INSERT INTO products VALUES ('Olympic Barbell', 'products/barbell.PNG', '2.2m Olympic Barbell', 130, 50, 'barbell', 'active')")
# c.execute("INSERT INTO products VALUES ('Bench', 'products/bench.PNG', 'Incline Bench', 60, 20, 'bench', 'active')")
# c.execute("INSERT INTO products VALUES ('Half Rack', 'products/halfrack.PNG', 'Half Rack. Good for squat.', 500, 400, 'racks', 'active')")
# c.execute("INSERT INTO products VALUES ('Bumper Plates', 'products/rouge.PNG', 'Expensive bumper plates', 100, 20, 'plates', 'active')")
# c.execute("INSERT INTO products VALUES ('Squat Rack', 'products/squat.PNG', 'Cheap and good', 130, 80, 'racks', 'active')")
# c.execute("INSERT INTO products VALUES ('Flat Bench', 'products/bench2.PNG', 'Flat bench. Good for benching', 90, 45, 'bench', 'active')")
# c.execute("INSERT INTO products VALUES ('Tri-grip Plates', 'products/nyp.PNG', 'Budget plates', 100, 40, 'plates', 'active')")
# c.execute("INSERT INTO products VALUES ('Trap Bar', 'products/trap.PNG', 'Good stuff', 200, 90, 'barbell', 'inactive')")
# conn.commit()
# conn.close()
# print('rows created')

# JoO SeNg #ok
# c.execute("INSERT INTO paymentdetails VALUES (username, name, ccnumber, expiry, cvv)")
# conn.commit()
# conn.close()
# print('rows created')

# Drop Table
# c.execute("DROP TABLE products")
# conn.commit()
# conn.close()
# print('table dropped')

# Query DB
# c.execute("SELECT rowid, * FROM products WHERE name LIKE '%{}%'".format("' UNION SELECT '1', sql, '3', '4', '5', '6' FROM sqlite_master--"))
# c.execute("SELECT rowid, * FROM products WHERE name LIKE '%''%' UNION SELECT * FROM x--")
# print(c.fetchall())
# conn.close()

# c.execute("SELECT * FROM users WHERE username='JohnDoe' ")
# user = c.fetchone()

# c.execute("SELECT rowid, * FROM products")
# print(c.fetchall())

# To see table names
# c.execute(" SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
# print(c.fetchone())

# c.execute("SELECT name FROM (SELECT * FROM sqlite_master UNION ALL SELECT * FROM sqlite_temp_master) WHERE type='table' ORDER BY name")
# print(c.fetchone())

# See all tables created in sqlite db
# c.execute("SELECT * FROM users WHERE username='' UNION SELECT sql, '2', '3', '4', '5' FROM sqlite_master-- ")
# print(c.fetchone())

conn.close()
