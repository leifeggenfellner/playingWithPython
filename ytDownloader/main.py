from pytube import YouTube


def download(link, path):
    YouTube(str(link)).streams.first().download(
        str(path))
