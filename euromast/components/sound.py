import pygame as pg



class LoadSound:
    def __init__(self, file, type, volume=1.0, loop=0):
        self.file = file
        self.type = type
        self.volume = volume
        self.loop = loop
        self.music = pg.mixer.Sound(self.file)
        self.is_playing = False

    def play(self):
        if self.is_playing is False:
            self.music.set_volume(self.volume)
            self.music.play(self.loop)
            self.is_playing = True

    def stop(self):
        self.music.stop()
        self.is_playing = False
