import sqlite3

conn = sqlite3.connect("lootify.db", check_same_thread=False)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS posted_products(
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_id TEXT UNIQUE,
title TEXT,
posted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()
