import pandas as pd
import yt_dlp
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox, ttk, scrolledtext

class CSVtoMP3App:
    def __init__(self, root):
        self.root = root
        self.root.title("CSV Playlist to MP3")
        self.root.geometry("600x430")
        self.root.configure(bg="#1e1e1e")
        self.root.resizable(False, False)

        self.set_style()
        self.setup_gui()

    def set_style(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TButton", foreground="white", background="#3c3c3c", padding=6, relief="flat")
        style.map("TButton", background=[("active", "#5a5a5a")])
        style.configure("TProgressbar", foreground="#0078D7", background="#0078D7")
        style.configure("Vertical.TScrollbar", background="#333")

    def setup_gui(self):
        tk.Label(self.root, text="🎵 CSV Playlist to Local Library", font=("Helvetica", 16),
                 bg="#1e1e1e", fg="#ffffff").pack(pady=10)

        self.upload_btn = ttk.Button(self.root, text="Upload Exportify CSV", command=self.select_csv)
        self.upload_btn.pack(pady=10)

        self.progress = ttk.Progressbar(self.root, length=400, mode='determinate')
        self.progress.pack(pady=10)

        self.status_box = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, height=12, width=70,
                                                    font=("Consolas", 9), bg="#2d2d2d", fg="#ffffff",
                                                    insertbackground="white", borderwidth=0)
        self.status_box.pack(pady=10)

    def log(self, text):
        self.status_box.insert(tk.END, text + "\n")
        self.status_box.see(tk.END)
        self.root.update_idletasks()

    def select_csv(self):
        csv_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if not csv_path:
            return

        csv_file = Path(csv_path)
        playlist_name = csv_file.stem
        base_dir = csv_file.parent.parent
        downloads_dir = base_dir / "Downloads" / playlist_name
        downloads_dir.mkdir(parents=True, exist_ok=True)

        df = pd.read_csv(csv_file)
        track_artist_pairs = list(zip(df["Track Name"], df["Artist Name(s)"]))
        total_tracks = len(track_artist_pairs)

        self.log(f"📂 Playlist: {playlist_name}")
        self.log(f"🎶 Tracks: {total_tracks}")
        self.log(f"📥 Output Folder: {downloads_dir}\n")

        self.progress["maximum"] = total_tracks
        self.progress["value"] = 0

        for index, (track, artist) in enumerate(track_artist_pairs, 1):
            self.log(f"🔽 {index}/{total_tracks} - {artist} - {track}")
            self.download_track(track, artist, downloads_dir)
            self.progress["value"] = index
            self.root.update_idletasks()

        self.log("\n✅ Done!")
        messagebox.showinfo("Complete", f"Playlist downloaded to:\n{downloads_dir}")

    def download_track(self, title, artist, output_dir):
        search_query = f"{title} {artist} audio"
        output_template = str(output_dir / f"{artist} - {title}.%(ext)s")

        ydl_opts = {
            'format': 'bestaudio/best',
            'noplaylist': True,
            'default_search': 'ytsearch1',
            'outtmpl': output_template,
            'cookiefile': r'C:\Users\Desktop\CSV Playlist to Local Library\cookies.txt', #edit this line with the proper directory of your coockies file
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '0',
            }],
            'quiet': True,
            'no_warnings': True,
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([search_query])
        except Exception as e:
            self.log(f"❌ Failed: {title} by {artist} — {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CSVtoMP3App(root)
    root.mainloop()
