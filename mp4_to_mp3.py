import os
from moviepy.editor import *

video = VideoFileClip("Seni Kalbimden Kovdum.mp4")
video.audio.write_audiofile(os.path.join("Seni Kalbimden Kovdum.mp3"))