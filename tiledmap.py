import pytmx
import pygame as pg
import sys

from NewObstacle import NewObstacle
from Obstacle import Obstacle


class TiledMap:
    def __init__(self, filename):
        self.tmxdata = pytmx.load_pygame(filename, pixelalpha=True)
        self.width = self.tmxdata.width * self.tmxdata.tilewidth
        self.height = self.tmxdata.height * self.tmxdata.tileheight

        self.tiles = {
            "grass": [],
            "building": [],
            "sign": [],
            "items": [],
            "roof": [],
            "obstacles": {"obstacles": [],
                          "door": []
                          }
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
                        
        for tile_group in self.tmxdata.objectgroups:
            for tile_object in tile_group:
                _obstacle = Obstacle(tile_object.x, tile_object.y,
                                    tile_object.width, tile_object.height, tile_group.name)
                self.tiles["obstacles"][tile_group.name].append(_obstacle)

    def make_map(self):
        temp_surface = pg.Surface((self.width, self.height))
        self.load_tiles()
       
        return temp_surface

    def blit_objects(self, surface, arr):
        for obj in arr:
            surface.blit(
                obj.surface, obj.pos
            )

    def rerender_map(self, filename):
        self.tiles = {
            "grass": [],
            "building": [],
            "sign": [],
            "items": [],
            "roof": [],
            "obstacles": {"obstacles": [],
                          "door": []
                          }
        }

        self.tmxdata = pytmx.load_pygame(filename, pixelalpha=True)
        self.make_map()
            
