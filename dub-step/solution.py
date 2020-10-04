def song_decoder(song):
    new_song = song.replace("WUB", " ").strip()

    return " ".join(new_song.split())
