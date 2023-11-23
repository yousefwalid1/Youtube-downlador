from tkinter import *
from tkinter import filedialog
from pytube import YouTube
import threading

def browse():
    directory = filedialog.askdirectory(title="Save Video")
    folder_link.delete(0, END)
    folder_link.insert(0, directory)

def download_yt():
    status.config(text="Status: Downloading...")
    video_link = yt_link.get()
    download_folder = folder_link.get()
    video_quality = quality_var.get()  # Get the selected video quality
    download_as_mp3 = mp3_var.get()  # Get the selected MP3 option

    def on_complete_callback(stream=None, chunk=None, file_handle=None, remaining=None):
        status.config(text="Status: Complete")

    yt = YouTube(video_link, on_complete_callback=on_complete_callback)

    if download_as_mp3:
        audio_stream = yt.streams.filter(only_audio=True).first()
        if audio_stream:
            audio_stream.download(download_folder)
        else:
            status.config(text="Status: MP3 Download not available for this video.")
    else:
        video_stream = yt.streams.filter(progressive=True, file_extension="mp4", resolution=video_quality).first()
        if video_stream:
            video_stream.download(download_folder)
        else:
            status.config(text=f"Status: {video_quality} not available for this video.")

# Root window
root = Tk()
root.title("YouTube Downloader")
root.geometry("600x400")  # Adjusted the height
root.resizable(FALSE, FALSE)

# YouTube Logo Text
youtube_logo_text = Label(root, text="YouTube", font=("Arial", 20, "bold"))
youtube_logo_text.place(relx=0.5, rely=0.05, anchor="center")

# Entry and Label for YouTube Link
yt_label = Label(root, text="YouTube Link")
yt_label.place(x=25, y=150)
yt_link = Entry(root, width=60)
yt_link.place(x=140, y=150)

# Entry and Label for Download Folder
folder_label = Label(root, text="Download Folder")
folder_label.place(x=25, y=183)
folder_link = Entry(root, width=50)
folder_link.place(x=140, y=183)

# Quality Options
quality_label = Label(root, text="Video Quality:")
quality_label.place(x=25, y=220)

quality_options = ["360p", "480p", "720p", "1080p"]
quality_var = StringVar(root)
quality_var.set(quality_options[2])  # Default quality is 720p
quality_menu = OptionMenu(root, quality_var, *quality_options)
quality_menu.place(x=140, y=215)

# MP3 Option
mp3_var = BooleanVar(root)
mp3_checkbox = Checkbutton(root, text="Download as MP3", variable=mp3_var)
mp3_checkbox.place(x=280, y=215)

# Browse Button
browse_button = Button(root, text="Browse", command=browse)
browse_button.place(x=455, y=180)

# Download Button
download_button = Button(root, text="Download", command=lambda: threading.Thread(target=download_yt).start())
download_button.place(x=280, y=250)

# Status bar
status = Label(root, text="Status: Ready", font="Calibre 10 italic", fg="black", bg="white", anchor="w")
status.place(rely=1, anchor="sw", relwidth=1)

# Bottom Right Labels
bottom_right_label_yousef = Label(root, text="Yousef Walid", font="Calibre 10 italic", fg="black", bg="white", anchor="e")
bottom_right_label_yousef.place(relx=1, rely=0.95, anchor="se")

bottom_right_label_cs50 = Label(root, text="CS50", font="Calibre 10 italic", fg="black", bg="white", anchor="e")
bottom_right_label_cs50.place(relx=1, rely=1, anchor="se")

root.mainloop()
