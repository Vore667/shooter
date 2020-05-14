import pygame as py

class Projectile(py.sprite.Sprite):

    def __init(self):
        super().__init__()
        self.velocity = 5
        self.image = py.image.load('assets/projectile.png')
        self.rect = self.image.get_rect()
