from pytube import YouTube

link = str(input('video: '))
#print(link)
yt = YouTube(link)
ys = yt.streams.get_highest_resolution()
ys.download()