import pygame as pg
from TiledMap import TiledMap
from Player import Player
from Obstacle import Obstacle

# ALL GLOBAL VARIABLES
from config import *


class Game:
    def __init__(self, debug_mode=False):
        pg.init()
        self.game_display = pg.display.set_mode(DISPLAY_SIZE)
        pg.display.set_caption(CAPTION)

        self.player = Player()

        self.map = TiledMap("resources/pallettown.tmx")
        self.map_surface = self.map.make_map()
        self.init_obstacles()

        self.debug_mode = debug_mode

        self.game_running = False

    def init_obstacles(self):
        # initialize variables
        self.walls = pg.sprite.Group()
        for tile_object in self.map.tmxdata.objects:
            if (tile_object.name == 'wall' or tile_object.name == 'item'or
                    tile_object.name == 'rock' or tile_object.name == 'water'):
                Obstacle(self.walls, tile_object.x, tile_object.y,
                         tile_object.width, tile_object.height)

    def run(self):
        clock = pg.time.Clock()

        self.game_running = True
        while self.game_running:
            dt = clock.tick(60)
            for event in pg.event.get():
                # Handles Quitting window and cleanup
                if event.type == pg.QUIT:
                    self.game_running = False

            key = pg.key.get_pressed()

            if pg.key.get_pressed()[pg.K_f]:    # hold f to open debug mode
                self.debug_mode = True
            else:
                self.debug_mode = False

            # Handles movement and sprite changes
            self.player.move(dt, self.walls)

            self.game_display.fill(WHITE)
            self.game_display.blit(
                self.map_surface, self.adjust_camera((0, 0), (self.player.dx, self.player.dy)))
            self.game_display.blit(self.player.player_img,
                                   self.player.player_position())

            # draws the hitboxes for player and wall for debugging purposes and updates hitboxes
            if self.debug_mode:
                pg.draw.rect(self.game_display, CYAN, self.player.hit_rect, 1)

            for wall in self.walls:
                if self.player.moving:
                    # (important) updates hitbox for walls
                    wall.rect.x, wall.rect.y = self.adjust_camera(
                        (wall.x, wall.y), (self.player.dx, self.player.dy))
                if self.debug_mode:
                    pg.draw.rect(self.game_display, CYAN, wall.rect, 1)

            pg.display.update()
        pg.quit()
        quit()

    def adjust_camera(self, pos, player_pos):
        x, y = pos
        player_x, player_y = player_pos
        return x-player_x, y - player_y

    def handle_keypress(self):
        """
        Might implement a keypress handler, mayber
        """
        key = pg.key.get_pressed()
        if pg.key.get_pressed()[pg.K_f]:    # hold f to open debug mode
            self.debug_mode = True
        else:
            self.debug_mode = False
        pass


def main():
    game = Game()
    game.run()


print(__name__)
if __name__ == "__main__":
    main()
