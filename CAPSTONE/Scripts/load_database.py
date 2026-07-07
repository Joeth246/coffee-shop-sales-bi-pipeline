from pathlib import Path
import sqlite3
import pandas as pd

# Project Paths

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_FILE = PROJECT_ROOT / "data" / "cleaned_sales.csv"

DATABASE_FOLDER = PROJECT_ROOT / "database"
DATABASE_FOLDER.mkdir(exist_ok=True)

DATABASE_FILE = DATABASE_FOLDER / "coffee_sales.db"

# Load Clean Dataset

df = pd.read_csv(DATA_FILE)

print(f"Loaded {len(df)} cleaned records.")

# Connect to SQLite

connection = sqlite3.connect(DATABASE_FILE)

print("Connected to SQLite.")

# Export DataFrame to SQL

df.to_sql(
    "Sales",
    connection,
    if_exists="replace",
    index=False
)

print("Sales table created successfully.")

# Verify Import

cursor = connection.cursor()

cursor.execute("SELECT COUNT(*) FROM Sales")

row_count = cursor.fetchone()[0]

print(f"Rows in Sales table: {row_count}")

cursor.execute("""
SELECT *
FROM Sales
LIMIT 5
""")

rows = cursor.fetchall()

print("\nFirst Five Rows\n")

for row in rows:
    print(row)

# Close Connection

connection.close()

print("\nDatabase connection closed.")