from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("Ops! An error has occurred downloading your youtube video")
    print("Download Complete 👍")
    
link = input("Paste youtube link here!! URL: ")
Download(link)

