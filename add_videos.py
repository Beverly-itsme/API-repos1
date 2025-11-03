import requests
import os

# API endpoint
BASE_URL = "http://192.168.43.81:8000"
VIDEOS_ENDPOINT = f"{BASE_URL}/videos/"

# Get list of video files
video_dir = "media/videos"
video_files = [f for f in os.listdir(video_dir) if f.endswith('.mp4')]

print(f"Found {len(video_files)} video files")

# Register each video
for video_file in video_files:
    # Create a simple title from filename
    title = os.path.splitext(video_file)[0]
    
    if '_' in title and len(title) > 20:
        title = f"Video {title[:8]}"
    
    # Video data
    video_data = {
        "titulo": title,
        "descricao": f"Video file: {video_file}",
        "arquivo": video_file
    }
    
    try:
        response = requests.post(VIDEOS_ENDPOINT, json=video_data)
        if response.status_code == 200:
            print(f"Successfully registered: {video_file}")
        else:
            print(f"Failed to register {video_file}: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Error registering {video_file}: {str(e)}")

print("Finished registering videos")