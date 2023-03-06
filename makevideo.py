from os import listdir
from moviepy.editor import *
import tkinter as tk
from tkVideoPlayer import TkinterVideo

def mergeVids(foldername, speed):
    clipnames = listdir(foldername)
    clips = []
    for clipname in clipnames:
        print("Adding " + clipname)
        clip = VideoFileClip(foldername +"/" + clipname)
        clip.resize(width=800)
        clip = clip.subclip(0.2, clip.duration - 0.2)  #trim .2 off the edges
        clips.append(clip)  # add to list of clips

    final = concatenate_videoclips(clips, method="compose")

    if speed != 1:
        final = clip.fx( vfx.speedx, factor=speed)
    final.write_videofile(foldername+"/merged.mp4")

    return foldername+"/merged.mp4"

def playVid(finalvid):
    root = tk.Tk()

    videoplayer = TkinterVideo(master=root, scaled=True, height=900, width=900)

    videoplayer.load(finalvid)
    videoplayer.pack(expand=True, fill="both")

    videoplayer.play() # play the video

    root.mainloop()
