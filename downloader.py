# importing packages
from pytube import YouTube
import os

# url input from user
yt = YouTube(
    str(input("Escreva a URL do video que quer baixar e aperte Enter: \n>> ")))


# extract only audio
video = yt.streams.filter(only_audio=True).first()

# check for destination to save file
destination = str('./Musica')

# download the file
out_file = video.download(output_path=destination)

# save the file
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)

# result of success
print(yt.title + " Foi baixado com Sucesso.")
print('Está na pasta "Musica".')
