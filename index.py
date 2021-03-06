# pip install youtube-dl

import youtube_dl

class YTD2MP3:
    def __init__(self) -> None:
        self.ydl = youtube_dl.YoutubeDL(self.getOptions())
    
    def hook(self, d):
        if d['status'] == 'finished':
            print("Done downloading, Converting Now ...")

    def getOptions(self):
        return {
            'format' : 'bestaudio/best',
            'postprocessors' : [{
            'preferredcodec' : 'mp3',
            'preferredquality' : '192',
        }],
        'progress_hooks' : [self.hook],
        }

    def startDownload(self, url):
        self.ydl.download([url]);

downloader = YTD2MP3()
url = input("Enter Youtbe URL:")
downloader.startDownload(url)

