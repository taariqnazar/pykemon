import pygame as pg


class Obstacle(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        self.rect = pg.Rect(x, y, w, h)

        self.position = self.x, self.y = x, y

        self.rect.x = x
        self.rect.y = y
