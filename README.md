# Spotify2MP3-YouTubeDownloader
Turn your Spotify playlists into local files

# 🎵 Spotify2MP3 YouTube Downloader

A lightweight Python GUI app that lets you export your Spotify playlists via [Exportify](https://watsonbox.github.io/exportify/) and automatically downloads each song as an MP3 from YouTube — with zero fuss.

## ✅ Features

- Upload any CSV exported from Exportify
- Automatically searches for each song on YouTube
- Downloads best quality audio and converts to `.mp3`
- Organizes files into folders by playlist
- Skips bot checks and CAPTCHA using your real YouTube cookies

## 🖥️ Requirements

- Python 3.8+
- `yt-dlp`
- `ffmpeg` (must be in your system PATH)
- `pandas`
- `tkinter`
- YouTube cookies exported via [cookies.txt Firefox extension](https://addons.mozilla.org/en-US/firefox/addon/cookies-txt/)

## 📦 Setup

1. Install dependencies:

```bash
pip install yt-dlp pandas
```

2. Make sure `ffmpeg` is installed:  
[FFmpeg Download](https://ffmpeg.org/download.html)

3. Export your YouTube cookies:
   - Log into YouTube using Firefox (or your prefered Browser)
   - Use [cookies.txt extension](https://addons.mozilla.org/en-US/firefox/addon/cookies-txt/)
   - Save the file as `cookies.txt` to the app folder

4. Export your playlists via [Exportify](https://watsonbox.github.io/exportify/)

5. Run the app:

```bash
python csv_gui_app.pyw
```

## 📂 Output

Downloaded songs are saved to:
```
<CSV Folder>/Downloads/<Playlist Name>/
```

Each song is named: `Artist - Track Name.mp3`

## ⚠️ Legal Notice

This tool is for **educational use only**.  
Respect copyright laws in your region.

---


