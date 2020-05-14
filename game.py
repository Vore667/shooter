import pygame as py
from player import Player

#Class Game
class Game:
    def __init__(self):
        #generer Player
        self.player = Player()
        self.pressed = {}