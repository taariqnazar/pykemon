import pygame as pg


class Obstacle(pg.sprite.Sprite):
    def __init__(self, walls, x, y, w, h):
        self.groups = walls
        pg.sprite.Sprite.__init__(self, self.groups)

        self.rect = pg.Rect(x, y, w, h)
        self.x = x
        self.y = y

        self.rect.x = x
        self.rect.y = y
