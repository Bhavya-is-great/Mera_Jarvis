import tkinter as tk
from tkinter import ttk
from pytube import YouTube

def download_video():
    video_url = url_entry.get()
    yt = YouTube(video_url)
    stream = yt.streams.get_highest_resolution()
    stream.download()
    status_label.config(text="Video downloaded successfully!")

# Create a tkinter window
window = tk.Tk()
window.title("YouTube Video Downloader")
window.geometry("360x360")

# Add a label and an entry field for the video URL
url_label = tk.Label(window, text="Enter YouTube Video URL:")
url_label.pack()

url_entry = tk.Entry(window, width=50)
url_entry.pack()

# Add a button to trigger the video download
download_button = tk.Button(window, text="Download", command=download_video)
download_button.pack()

# Add a label to display download status
status_label = tk.Label(window, text="")
status_label.pack()

# Run the tkinter event loop
window.mainloop()