import pyexcel
from youtube_dl import YoutubeDL

songs = pyexcel.get_records(file_name='top100_itunes.xlsx')

for song in songs:
    title = song['Title']
    artist = song['Artist']
    search = title + " " + artist
    search_list = [search]
    options = {
        'default_search': 'ytsearch',
        'max_downloads': 1,
        'format': 'bestaudio/audio'
    }
    dl = YoutubeDL(options)
    dl.download(search_list)
