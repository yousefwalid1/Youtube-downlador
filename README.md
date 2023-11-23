# Youtube Downloader

## Description: YouTube Downloader with GUI

# YouTube Downloader with GUI

## Overview

This Python application provides a user-friendly graphical interface for downloading YouTube videos. The project utilizes the Tkinter library to create an intuitive interface where users can input a YouTube video link, choose download options, and initiate the download process.

## Features

1. **User-Friendly Interface:**
   - The Tkinter library is used for creating a simple and intuitive graphical user interface.
   - Displays YouTube and CS50 logos for visual appeal.

2. **Download Options:**
   - Users can input a YouTube video link and choose various download options.
   - Options include selecting the desired video quality (360p, 480p, 720p, 1080p) and downloading videos as MP3 audio files.

3. **Download Folder Selection:**
   - A "Browse" button allows users to choose the download folder.

4. **Threading for Responsiveness:**
   - Threading is implemented to ensure the GUI remains responsive during the download process.

5. **Error Handling:**
   - Handles scenarios where the chosen video quality is unavailable for the given video.
   - Informs the user if MP3 download is not available for the video.

6. **Status Display:**
   - Provides a status bar to display the current status of the download process (Ready, Downloading, Complete).

7. **Bottom Right Labels:**
   - Displays labels at the bottom right, indicating the creator's name ("Yousef Walid") and acknowledgment to CS50 ("This was CS50").

## Usage

1. Input the YouTube video link.
2. Choose the desired video quality or select MP3 download.
3. Specify the download folder using the "Browse" button.
4. Click the "Download" button to initiate the download process.

**Note:** Ensure compliance with YouTube's terms of service and local regulations when using application. Downloading copyrighted material without permission may infringe on intellectual property rights.

## Dependencies

- Python 3.x
- Tkinter
- Pytube

## this Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yousefwalid1/Youtube-downlador

   Install the required dependencies:

```bash
pip install pytube

## Run the Application
## Navigate to the project directory and run:

```bash
python main.py

## Author
#- Yousef Walid
## Acknowledgments
## This project was inspired by the CS50 course.
##Special thanks to the developers of the Pytube library.
## Feel free to contribute or report issues. Happy downloading!

