# pip install pytube
from pytube import YouTube
link = input("Enter the link of Youtube Video: ")
yt = YouTube(link)  # creating an object
ys = yt.streams.get_highest_resolution()   
# to get the highest resolution
print("Downloading...") 
# Shows the message until Downloading the video
ys.download("Downloads\Youtube Downloader")  
# specifying location for the video
print("Download Completed!!")

