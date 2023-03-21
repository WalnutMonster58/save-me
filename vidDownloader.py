from pytube import YouTube 
from pytube import Playlist
  
#where to save 
SAVE_PATH = "vids" 
  
#link of the video to be downloaded 

def downloadVid(link):


    if 'watch' in str(link):
        yt = YouTube(str(link))
        mp4_files = yt.streams.filter(file_extension="mp4")
        mp4_720p_files = mp4_files.get_by_resolution("720p")
        mp4_720p_files.download(SAVE_PATH) 
        print('video ' + link + ' has been downloaded')
        exit()

    elif 'playlist' in str(link):
        p = Playlist(link)
        for vid in p.videos:
            mp4_files = vid.streams.filter(file_extension="mp4")
            mp4_720p_files = mp4_files.get_by_resolution("720p")
            mp4_720p_files.download(SAVE_PATH) 
    

while True:
    downloadVid(input('Place Link here: '))