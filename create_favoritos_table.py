import sqlite3
import os

# Connect to the database
db_path = os.path.join(os.path.dirname(__file__), 'media.db')
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

try:
    # Create the favoritos table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS favoritos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            musica_id INTEGER NOT NULL,
            FOREIGN KEY (musica_id) REFERENCES musicas (id)
        )
    ''')
    
    # Commit changes
    conn.commit()
    print("✅ Favoritos table created successfully")
    
except Exception as e:
    print(f"❌ Error creating favoritos table: {e}")
finally:
    conn.close()