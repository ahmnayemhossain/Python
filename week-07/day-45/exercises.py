class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist


class Playlist:
    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)


print("Day 45 practice exercises")

print("\nExercise 1: Composition setup")
playlist = Playlist()
playlist.add_song(Song("Track One", "Artist A"))
print(playlist.songs[0].title)

print("\nExercise 2: Add second object")
playlist.add_song(Song("Track Two", "Artist B"))
print(len(playlist.songs))

print("\nExercise 3: Loop child objects")
for song in playlist.songs:
    print(song.title)

print("\nExercise 4: Object inside object")
print(playlist.songs[1].artist)

print("\nExercise 5: User song")
title = input("Enter song title: ")
artist = input("Enter artist name: ")
playlist.add_song(Song(title, artist))
print(playlist.songs[-1].title)
