import pygame as pg
from utilities import *

class PlayScreen:
    def __init__(self, parent, levelImage):
        self.parent = parent
        self.createMapFromImage(levelImage)
    
    def createMapFromImage(self, levelImage):
        # TO DO FILL IN
        self.map = None
        self.startLocation = [1, 1]
        self.endLocation = [2, 2]
    
    def draw(self, screen):
        screen.fill((255, 100, 100))
    
    def update(self):
        self.running = True
    
    def handleEvents(self, event):
        self.running = True