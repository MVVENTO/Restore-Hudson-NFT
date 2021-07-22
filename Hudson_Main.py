#****************************************************************************************************************************
# Title       : Hudson.py
#Auhor        : Melissa Ann Vento
#Description  : Restore the Hudson | merged video files 
#Dependencies : "2021_06_30_18_47_29.mp4" , "2021_07_06_14_25_40.mp4" , "2021_07_06_15_24_23.mp4" , "2021_07_06_15_26_42.mp4"
#Addendum     : DO NOT ALTER THIS FILE 
#****************************************************************************************************************************/
from moviepy.editor import *

# clip is the video from 00:00 to 00:31

# First video of hudson
clip = VideoFileClip("2021_06_30_18_47_29.mp4").subclip(15, 25)
clip2 = VideoFileClip("2021_06_30_18_47_29.mp4").subclip(25, 31)
clip3 = VideoFileClip("2021_06_30_18_47_29.mp4").subclip(10, 12)
clip4 = VideoFileClip("2021_06_30_18_47_29.mp4").subclip(20, 25)

# clip is the video from 00:56 to 02:48

#  second video of the Hudson
clip5 = VideoFileClip("2021_07_06_14_25_40.mp4").subclip(56, 66)
clip6 = VideoFileClip("2021_07_06_14_25_40.mp4").subclip(70, 76)
clip7 = VideoFileClip("2021_07_06_14_25_40.mp4").subclip(50, 52)
clip8 = VideoFileClip("2021_07_06_14_25_40.mp4").subclip(30, 35)

# clip is the video from 00:44 to 01:01

# Third video of Hudson
clip9 = VideoFileClip("2021_07_06_15_24_23.mp4").subclip(44, 54)
clip10 = VideoFileClip("2021_07_06_15_24_23.mp4").subclip(55, 60)
clip11 = VideoFileClip("2021_07_06_15_24_23.mp4").subclip(50, 52)
clip12 = VideoFileClip("2021_07_06_15_24_23.mp4").subclip(44, 48)

final_clip = concatenate_videoclips([clip, clip2, clip3, clip4, clip5, clip6, clip7, clip8, clip9, clip10, clip11, clip12])

final_clip.write_videofile("Hudson_edited.mp4")

