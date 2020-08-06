import pygame as pg

TILESIZE = 30


class Map:
    def __init__(self, filename):
        with open(filename, "rt") as f:
            for line in f:
                self.data.append(line)

        self.tile_width = len(self.data[0])
        self.tile_height = len(self.data)

        self.width = self.tile_width + TILESIZE
        self.height = self.tile_height + TILESIZE


class Camera:
    def __init__(self, width, height):
        self.camera = pg.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entitiy):
        return entitiy.rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.x + int(WIDTH/2)
        y = -target.rect.y + int(WIDTH/2)

        self.camera = pg.Rect(x, y, self.width, self.height)
