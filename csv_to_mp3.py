import os
import pandas as pd
import yt_dlp
from pathlib import Path

# Paths (adjust if needed)
base_dir = Path.home() / "CSV Playlist to Local Library"
csv_dir = base_dir / "CSV Playlists"
downloads_dir = base_dir / "Downloads"

# Choose your CSV
csv_file = csv_dir / "oi.csv"  # Replace with the actual file you want
df = pd.read_csv(csv_file)

# Create folder for that playlist
playlist_name = csv_file.stem
playlist_folder = downloads_dir / playlist_name
playlist_folder.mkdir(parents=True, exist_ok=True)

# Read track and artist info
track_artist_pairs = list(zip(df["Track Name"], df["Artist Name(s)"]))

# yt-dlp config
def download_track(title, artist, output_dir):
    search_query = f"{title} {artist} audio"
    ydl_opts = {
        'format': 'bestaudio/best',
        'noplaylist': True,
        'default_search': 'ytsearch',
        'outtmpl': str(output_dir / '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '0',
        }],
        'quiet': False,
        'no_warnings': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([search_query])
        except Exception as e:
            print(f"❌ Failed: {title} by {artist}\n  Reason: {e}")

# Download loop (remove [:3] to do full list)
for track, artist in track_artist_pairs[:3]:  # TEMP limit for testing
    print(f"🔽 Downloading: {track} - {artist}")
    download_track(track, artist, playlist_folder)
