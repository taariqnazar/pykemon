import pygame as pg
from TiledMap import TiledMap
from Player import Player
from Obstacle import Obstacle

# ALL GLOBAL VARIABLES
from config import *


class Game:
    def __init__(self, debug_mode=False):
        pg.init()
        pg.display.set_caption(CAPTION)

        self.game_display = pg.display.set_mode(DISPLAY_SIZE)

        self.player = Player()
        self.maps = {'home': ["resources/pallettown.tmx", 442, 181],
                    'pokecenter' :["resources/new.tmx", 220, 335]}
        self.map = TiledMap("resources/pallettown.tmx")
        self.map_surface = self.map.make_map()

        # self.init_obstacles()

        self.debug_mode = debug_mode
        self.game_running = False

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

            if key[pg.K_a]:
                self.fade(0, 255, 15)
                self.map.rerender_map("resources/new.tmx")
                self.fade(255,0, -15)

            if pg.key.get_pressed()[pg.K_f]:    # hold f to open debug mode
                self.debug_mode = True
            else:
                self.debug_mode = False

            # Handles movement and sprite changes
            self.adjust_camera_obstacles(self.map.tiles["obstacles"])
            player_event = self.player.move(dt, self.map.tiles["obstacles"])


            if player_event != None:
                self.fade(0, 255, 15)
                print(player_event)
                
                self.player.dx = self.maps[player_event.id][1]
                self.player.dy = self.maps[player_event.id][2]
                self.map.rerender_map(self.maps[player_event.id][0])
                
                self.fade(255, 0, -15)
                
            # Handles drawing
            
            self.game_display.fill(WHITE)
            self.render_tiles(self.map.tiles["grass"])
            self.render_tiles(self.map.tiles["sign"])
            self.render_tiles(self.map.tiles["building"])
            self.render_tiles(self.map.tiles["items"])
            self.game_display.blit(self.player.player_img,
                                   self.player.player_position())
            self.render_tiles(self.map.tiles["roof"])

            if self.debug_mode:
                pg.draw.rect(self.game_display, CYAN, self.player.hit_rect, 1)

                for wall in self.map.tiles["obstacles"]["obstacles"]:
                    if self.debug_mode:
                        pg.draw.rect(self.game_display, CYAN, wall.rect, 1)

            pg.display.update()
        pg.quit()
        quit()

    def render_tiles(self, arr_tiles):
        for tile in arr_tiles:
            self.game_display.blit(
                tile.surface, self.adjust_camera(
                    tile.position, (self.player.dx, self.player.dy))
            )

    def adjust_camera_obstacles(self, arr):
        for key in arr.keys():
            
            for obs in arr[key]:
                obs.rect.x, obs.rect.y = self.adjust_camera(
                    (obs.x, obs.y), (self.player.dx, self.player.dy))

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
    
    def fade(self, start, end , reduce):
        for opacity in range(start, end, reduce):
            
            self.render_tiles(self.map.tiles["grass"])
            self.render_tiles(self.map.tiles["sign"])
            self.render_tiles(self.map.tiles["building"])
            self.render_tiles(self.map.tiles["items"])
            self.render_tiles(self.map.tiles["roof"])
            
            s = pg.Surface((1500,1500))  # the size of your rect
            s.set_alpha(opacity)                # alpha level
            s.fill((0,0,0))           # this fills the entire surface
            self.game_display.blit(s, (0,0))   
            pg.display.flip()
            pg.time.wait(20)


def main():
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
