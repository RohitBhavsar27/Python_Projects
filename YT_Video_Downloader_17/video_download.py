from pytubefix import YouTube
from pytubefix.cli import on_progress
import tkinter as tk
from tkinter import filedialog

def download_video(url,save_path):
    try:
        yt = YouTube(url,on_progress_callback = on_progress)
        print(f"Title: {yt.title}")
        highest_res_stream = yt.streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)
        print("\nVideo Downloaded Successfully.")
    except Exception as e:
        print(e)
        
def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected Folder: {folder}")
    return folder
        
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    video_url = input("Please enter a YouTube url: ")
    save_dir = open_file_dialog()
    
    if save_dir:
        print("Downloading Started...")
        download_video(video_url,save_dir)
    else:
        print("Invalid save location!")