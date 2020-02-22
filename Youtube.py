import pytube as pt

while True:
    link = input("Enter the Video link from youtube you want to download: ")
    try:
        yt = pt.YouTube(link)
        break
    except pt.exceptions.RegexMatchError:
        print("URL Not Found")
title = yt.title

print(title)
age_restracted = yt.age_restricted
if age_restracted:
    while True:
        age = input("This video is age restricated do you want to continue for yes press 'y' and for no press 'n': ").lower()
        if age == 'y':
            break
        elif age == 'n':
            print("Thanks for using Youtube video downloader :)")
            exit()
        else:
            print("Enter a correct choice")
            continue
resol = input("Enter the resolution in the form for 1080p, 720p, 480p, 360p, 144p: ")
qulatiy_list = yt.streams.filter(adaptive=True, mime_type="video/mp4")
qulatiy_list = qulatiy_list.filter(fps=30)
qulatiy_list = qulatiy_list.filter(res=resol)
qulatiy_list = qulatiy_list.first()

print("Starting Downloading")
print("Be Petient video is downloading!!!!!!")
qulatiy_list.download()
print("Downloading Complete")

