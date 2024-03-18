import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('restaurant.db')
c = conn.cursor()

# Create a table for products
c.execute('''CREATE TABLE IF NOT EXISTS products 
             (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, price REAL)''')

# Create a table for orders
c.execute('''CREATE TABLE IF NOT EXISTS orders 
             (id INTEGER PRIMARY KEY AUTOINCREMENT, product_id INTEGER, quantity INTEGER)''')

# Insert a product into the products table
c.execute("INSERT INTO products (name, price) VALUES (?, ?)", ('Pizza', 9.99))
conn.commit()

# Fetch all products
c.execute("SELECT * FROM products")
products = c.fetchall()
print("Products:")
for product in products:
    print(product)

# Update a product's price
c.execute("UPDATE products SET price = ? WHERE id = ?", (11.99, 1))
conn.commit()

# Fetch a specific product
c.execute("SELECT * FROM products WHERE id = ?", (1,))
product = c.fetchone()
print("Updated Product:", product)

# Delete a product
c.execute("DELETE FROM products WHERE id = ?", (1,))
conn.commit()

# Fetch all products after deletion
c.execute("SELECT * FROM products")
products = c.fetchall()
print("Products after deletion:")
for product in products:
    print(product)

# Close the connection
conn.close()
