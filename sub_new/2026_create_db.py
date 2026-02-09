import sqlite3

conn = sqlite3.connect("subagents.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS sub_agents (
    sl_no INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
""")

conn.commit()
conn.close()

print("Database ready.")
