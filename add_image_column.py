import sqlite3
import os

# Connect to the database
db_path = os.path.join(os.path.dirname(__file__), 'media.db')
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

try:
    # Add the imagem column to the musicas table
    cursor.execute("ALTER TABLE musicas ADD COLUMN imagem VARCHAR")
    conn.commit()
    print("Column 'imagem' added successfully to 'musicas' table!")
except sqlite3.OperationalError as e:
    if "duplicate column name" in str(e):
        print("Column 'imagem' already exists in 'musicas' table.")
    else:
        print(f"Error adding column: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
finally:
    conn.close()