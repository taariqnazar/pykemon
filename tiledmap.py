import pytmx
import pygame as pg
import sys

from NewObstacle import NewObstacle


class TiledMap:
    def __init__(self, filename):
        self.tmxdata = pytmx.load_pygame(filename, pixelalpha=True)
        self.width = self.tmxdata.width * self.tmxdata.tilewidth
        self.height = self.tmxdata.height * self.tmxdata.tileheight

        self.tiles = {
            "grass": [],
            "building": [],
            "obstacles": [],
            "sign": []
        }

    def load_tiles(self):
        ti = self.tmxdata.get_tile_image_by_gid
        for layer in self.tmxdata.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid, in layer:
                    tile = ti(gid)

                    if tile:
                        _obstacle = NewObstacle(
                            tile, ((x * self.tmxdata.tilewidth, y * self.tmxdata.tileheight)))
                        self.tiles[layer.name].append(_obstacle)
            else:
                print(layer)

    def make_map(self):
        temp_surface = pg.Surface((self.width, self.height))
        self.load_tiles()
        self.blit_objects(temp_surface)
        return temp_surface

    def blit_objects(self, surface):
        for key in self.tiles:
            for obj in self.tiles[key]:
                surface.blit(obj.surface, obj.position)
