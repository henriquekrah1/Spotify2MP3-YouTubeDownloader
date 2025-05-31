import pandas as pd
import yt_dlp
import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path
import os

# Setup GUI
root = tk.Tk()
root.withdraw()  # Hide main window

# Ask user for CSV file
csv_path = filedialog.askopenfilename(
    title="Select your Exportify CSV",
    filetypes=[("CSV files", "*.csv")]
)

if not csv_path:
    messagebox.showinfo("Cancelled", "No file selected.")
    exit()

csv_file = Path(csv_path)
playlist_name = csv_file.stem

# Set up Downloads folder in the same root
base_dir = csv_file.parent.parent  # Go back one level from "CSV Playlists" or wherever it was
downloads_dir = base_dir / "Downloads" / playlist_name
downloads_dir.mkdir(parents=True, exist_ok=True)

# Read CSV
df = pd.read_csv(csv_file)
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

# Start downloading
for track, artist in track_artist_pairs:
    print(f"🔽 Downloading: {track} - {artist}")
    download_track(track, artist, downloads_dir)

messagebox.showinfo("Done", f"Download complete! Files saved to:\n{downloads_dir}")
