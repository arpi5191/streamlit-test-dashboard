import sqlite3

# 1. Connect to a database (or create one if it doesn't exist)
conn = sqlite3.connect("test_database.db")
cursor = conn.cursor()

# 2. Create a table
cursor.execute("""
CREATE TABLE IF NOT EXISTS cell_counts (
    sample_id TEXT,
    b_cell INTEGER,
    cd8_t_cell INTEGER,
    cd4_t_cell INTEGER,
    nk_cell INTEGER,
    monocyte INTEGER
)
""")

# 3. Insert some sample data
data = [
    ("sample001", 100, 200, 150, 80, 50),
    ("sample002", 90, 210, 130, 70, 60),
    ("sample003", 120, 190, 160, 85, 55)
]

cursor.executemany("INSERT INTO cell_counts VALUES (?, ?, ?, ?, ?, ?)", data)

# Commit the changes
conn.commit()

# 4. Query the data
cursor.execute("SELECT * FROM cell_counts")
rows = cursor.fetchall()

# Print the results
print("Sample Data from SQLite Database:")
for row in rows:
    print(row)

# 5. Close the connection
conn.close()
