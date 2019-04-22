import pygame as pg
from utilities import *

class PlayScreen:
    def __init__(self, parent):
        self.parent = parent
    
    def draw(self, screen):
        screen.fill((255, 100, 100))
    
    def update(self):
        self.running = True
    
    def handleEvents(self, event):
        self.running = True