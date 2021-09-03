import pygame
import os.path
import random

class Sound:

    def __init__(self):
        self.play = False
        self.sounds = {
            "Music": [
                self.getSound("sons", "01.wav")
            ]
        }

    def getSound(self, sound, filename):
        try:
            a = pygame.mixer.Sound(os.path.join("../Several Spaces/", sound, filename))
        except:
            a = pygame.mixer.Sound(os.path.join("Several Spaces/", sound, filename))
        return a

    def playMusic(self):
        self.s = random.choice(self.sounds["Music"])
        self.s.set_volume(.5)
        self.s.play(loops=-1)
