from pytubefix import YouTube

link = input("Cole o link do video aqui: ")
yt = YouTube(link)

print(f"Baixando: {yt.title}...")
yt.streams.get_highest_resolution().download()
print("Pronto! Video baixado.")