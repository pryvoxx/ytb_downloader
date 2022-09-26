# coded by pryvox


# faire un downloadder de video youtube

# importer les modules nécaissaires
import os
from pytube import YouTube
from pystyle import Colors, Write
import youtube_dl

os.system('cls') # clear le terminal

# creer la banière
banner = """"
██╗   ██╗████████╗██████╗     ██████╗  ██████╗ ██╗    ██╗███╗   ██╗██╗      ██████╗  █████╗ ██████╗ ███████╗██████╗ 
╚██╗ ██╔╝╚══██╔══╝██╔══██╗    ██╔══██╗██╔═══██╗██║    ██║████╗  ██║██║     ██╔═══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
 ╚████╔╝    ██║   ██████╔╝    ██║  ██║██║   ██║██║ █╗ ██║██╔██╗ ██║██║     ██║   ██║███████║██║  ██║█████╗  ██████╔╝
  ╚██╔╝     ██║   ██╔══██╗    ██║  ██║██║   ██║██║███╗██║██║╚██╗██║██║     ██║   ██║██╔══██║██║  ██║██╔══╝  ██╔══██╗
   ██║      ██║   ██████╔╝    ██████╔╝╚██████╔╝╚███╔███╔╝██║ ╚████║███████╗╚██████╔╝██║  ██║██████╔╝███████╗██║  ██║
   ╚═╝      ╚═╝   ╚═════╝     ╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝

"""
print(Colors.green, banner)  # afficher la banière
print()  # saut de ligne
print("Coded by pryvox")
print()  # saut de ligne
print()  # saut de ligne

# demander a l'uttilisateur le lien de la vidéo
url = Write.Input("[*] Entrez le lien ->", Colors.green_to_yellow, interval=0.02)

# faire les choix
choix = int(Write.Input("\n[1] MP3 / [2] MP4 ->", Colors.green_to_yellow, interval=0.04))

# afficher le chargement
def on_download_progress(stream, chunk, bytes_remaining):
    bytes_downloaded = stream.filesize - bytes_remaining
    percent = bytes_downloaded * 100 / stream.filesize

    print(f"Downloading... {int(percent)}%")

# telecharger l'audio
def download_mp3():
    video_url = url
    video_info = youtube_dl.YoutubeDL().extract_info(url=video_url, download = False)
    file = f"{video_info['title']}.mp3"
    options = {
        'format': 'bestvideo+bestaudio',
        'keepvideo': False,
        'outtmpl': file,
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['\nwebpage_url']])
    print(Colors.green, "\nDownload Sucess!")


# télécharger la vidéo
def download_mp4():
    download = YouTube(url)
    download.register_on_progress_callback(on_download_progress)
    print(Colors.green, "Title :" + download.title) # afficher le titre de la vidéo
    print(Colors.green, "Views :" + str(download.views)) # afficher les vues de la vidéo
    print(Colors.green, "Url de la vignette :" + download.thumbnail_url) # afficher l'URL de la vignette

    stream = download.streams.get_highest_resolution()
    print(Colors.green, "Downloading...")
    stream.download()
    print(Colors.green, "\nDownload Sucess!")

# faire les choix
if (choix == 1):
    download_mp3()
elif (choix == 2):
    download_mp4()
else:
    print("mauvais choix !")
