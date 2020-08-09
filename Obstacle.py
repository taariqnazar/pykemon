import pygame as pg


class Obstacle():
    def __init__(self, x, y, w, h, type):
        self.type= type
        self.rect = pg.Rect(x, y, w, h)

        self.position = self.x, self.y = x, y

        self.rect.x = x
        self.rect.y = y
