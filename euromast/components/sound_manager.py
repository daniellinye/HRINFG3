import pygame as pg

class Manager(object):
    def __init__(self, sounds):
        self.ambiances = sounds['ambiances']
        self.effects = sounds['effects']
        self.sounds = {}
        self.now_playing = []
        self.now_playing_effects = []
        self.sounds.update(sounds['ambiances'])
        self.sounds.update(sounds['effects'])

    def get_effect(self, effect):
        return self.effects[effect]

    def play(self, sound, force=False):
        self.now_playing.append(sound)
        self.sounds[sound].play(force)

    def stop(self, sound, force=False):
        if type(sound) == list:
            for s in sound:
                self.now_playing.remove(s)
                self.sounds[s].stop(force)
            return
        if sound in self.now_playing:
            self.now_playing.remove(sound)
        self.sounds[sound].stop(force)

    def stop_effects(self):
        for now_playing_effects in self.now_playing_effects:
            self.sounds[now_playing_effects].stop()
            self.now_playing_effects.remove(now_playing_effects)

        for key, sound in self.effects.items():
            sound.force_stop()

    def play_effects(self):
        for now_playing_effects in self.now_playing_effects:
            self.sounds[now_playing_effects].start()
        for key, sound in self.effects.items():
            sound.force_play()

    def stop_music(self):
        for now_playing in self.now_playing:
            self.sounds[now_playing].stop()
        for key, sound in self.ambiances.items():
            sound.force_stop()

    def play_music(self):
        for now_playing in self.now_playing:
            self.sounds[now_playing].play(True)

        for key, ambiance in self.ambiances.items():
            ambiance.force_play()

class LoadSound:
    def __init__(self, file, type, volume=1.0, loop=0):
        self.file = file
        self.type = type
        self.volume = volume
        self.loop = loop
        self.music = pg.mixer.Sound(self.file)
        self.is_playing = False
        self.never_start = False

    def force_stop(self):
        self.never_start = True

    def force_play(self):
        self.never_start = False

    def play(self, enforce=False):
        if enforce: self.never_start = False
        if self.is_playing is False and not self.never_start:
            self.music.set_volume(self.volume)
            self.music.play(self.loop)
            if self.loop != 0:
                self.is_playing = True

    def stop(self, enforce=False):
        if enforce: self.never_start = True
        self.music.stop()
        self.is_playing = False
