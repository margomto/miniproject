
class Song: 
    def __init__(self, track, artist, genre, bpm, energy, danceability, length):
        self.track = track
        self.artist = artist
        self.genre = genre
        self.bpm = int(bpm)
        self.energy = int(energy)
        self.danceability = int(danceability)
        self.length = int(length)

    def __str__(self):
        return f'{self.track},{self.artist},{self.genre},{self.bpm},{self.energy},{self.danceability},{self.length}'

    def change_speed(self, relative_bpm):
        self.bpm = self.bpm + relative_bpm
        self.energy = self.energy + relative_bpm * 2
        self.danceability = self.danceability + relative_bpm * 3
        self.length = self.length - relative_bpm

    @staticmethod
    def load_songs(path):
        songs = []
        with open(path) as f:
            for line in f:
                each_song = line.strip('()').strip().split(',')
                song = Song(each_song[0], each_song[1], each_song[2], 
                each_song[3], each_song[4], each_song[5], each_song[6])
                songs.append(song)
        return songs  

    @staticmethod
    def save_songs(songs, path):
        with open(path, 'w') as f:
            for song in songs:
                f.write(f'{song}\n')
        



        

