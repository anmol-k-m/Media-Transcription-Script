# Media-Transcription-Script

A lightweight Python utility that automatically scans a directory for media files and generates speech-to-text transcriptions using OpenAI's Whisper model. The script recursively searches for supported media formats and saves the generated transcripts as JSON files.

# Features

  Recursively scans directories for media files
  
  Supports multiple formats: mp3, mp4, wav, mkv, m4v, mpeg, m4a, webm
  
  Uses the Whisper speech recognition model for transcription
  
  Automatically generates structured JSON transcripts
  
  Creates a results directory if it does not exist
  
  Handles errors gracefully and continues processing other files

# How It Works

  The script scans the current working directory for supported media files.
  
  Each file is passed to the Whisper model for transcription.
  
  The resulting text is stored in a JSON file inside a results/ directory.

Each JSON output contains:

  Source file path
  
  Transcribed text
  
  Example output:
  
  {
    "file": "example_audio.mp3",
    "transcription": "This is the generated transcript of the audio."
  }
# Installation

  Clone the repository and install the required dependencies.
  
  pip install openai-whisper
  pip install torch
  
  Ensure FFmpeg is installed since Whisper relies on it.
  
  sudo apt install ffmpeg
  Usage
  
  Run the script from the directory containing the media files.
  
  python media.py
  
  The script will:
  
  Scan the current directory
  
  Transcribe supported media files
  
  Save results in a results/ folder

# Project Structure
  .
  ├── media.py
  ├── results/
  │   ├── audio1.mp3.json
  │   └── video1.mp4.json
# Supported Media Formats

  .mp3
  
  .mp4
  
  .wav
  
  .mkv
  
  .m4v
  
  .mpeg
  
  .m4a
  
  .webm

# Notes

The script currently uses the Whisper "small" model for transcription.

Larger models may improve accuracy but require more compute resources.

Processing time depends on the length of the media files.

# License

This project is intended for educational and experimentation purposes.
