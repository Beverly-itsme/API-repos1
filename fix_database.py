import sqlite3
import os

# Connect to the database
db_path = os.path.join(os.path.dirname(__file__), 'media.db')
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

try:
    # Get all music records
    cursor.execute('SELECT id, titulo, arquivo, imagem FROM musicas')
    rows = cursor.fetchall()
    
    # Get actual files in directories
    media_dir = os.path.join(os.path.dirname(__file__), 'media')
    musicas_dir = os.path.join(media_dir, 'musicas')
    images_dir = os.path.join(media_dir, 'images')
    
    # Get list of actual files
    musicas_files = os.listdir(musicas_dir) if os.path.exists(musicas_dir) else []
    images_files = os.listdir(images_dir) if os.path.exists(images_dir) else []
    
    print(f"Found {len(musicas_files)} music files and {len(images_files)} image files")
    
    # Fix database entries
    for row in rows:
        id, titulo, arquivo, imagem = row
        
        # Fix audio file path
        if arquivo:
            # Extract the filename from the URL
            audio_filename = arquivo.split('/')[-1]
            
            # Check if this file actually exists
            if audio_filename not in musicas_files:
                # Try to find a matching file
                matching_files = [f for f in musicas_files if str(id) in f]
                if matching_files:
                    new_audio_url = f"http://192.168.43.81:8000/media/musicas/{matching_files[0]}"
                    cursor.execute('UPDATE musicas SET arquivo = ? WHERE id = ?', (new_audio_url, id))
                    print(f"Fixed audio path for '{titulo}': {audio_filename} -> {matching_files[0]}")
                else:
                    print(f"No matching audio file found for '{titulo}' (ID: {id})")
        
        # Fix image file path
        if imagem:
            # Extract the filename from the URL
            image_filename = imagem.split('/')[-1]
            
            # Check if this file actually exists
            if image_filename not in images_files:
                # Try to find a matching file
                matching_files = [f for f in images_files if str(id) in f]
                if matching_files:
                    new_image_url = f"http://192.168.43.81:8000/media/images/{matching_files[0]}"
                    cursor.execute('UPDATE musicas SET imagem = ? WHERE id = ?', (new_image_url, id))
                    print(f"Fixed image path for '{titulo}': {image_filename} -> {matching_files[0]}")
                elif images_files:  # If there are any image files, use the first one
                    new_image_url = f"http://192.168.43.81:8000/media/images/{images_files[0]}"
                    cursor.execute('UPDATE musicas SET imagem = ? WHERE id = ?', (new_image_url, id))
                    print(f"Fixed image path for '{titulo}': {image_filename} -> {images_files[0]}")
                else:
                    print(f"No matching image file found for '{titulo}' (ID: {id})")
    
    # Commit changes
    conn.commit()
    print("\nDatabase fix completed!")
        
except Exception as e:
    print(f"Error: {e}")
finally:
    conn.close()