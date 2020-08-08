import pygame as pg
from TiledMap import TiledMap
from Player import Player
from Obstacle import Obstacle

BLACK = 0, 0, 0
WHITE = 255, 255, 255
CYAN = 0, 255, 255


class Game:
    def __init__(self, display_size=(800, 600), caption="Pokemon"):
        pg.init()

        self.display_size = display_size

        self.game_display = pg.display.set_mode(display_size)
        pg.display.set_caption(caption)

        self.player = Player(
            display_width=display_size[0], display_height=display_size[1])
        self.map = TiledMap("resources/pallettown.tmx")

        self.game_running = True


    def new(self):
        #initialize variables
        self.walls = pg.sprite.Group()
        for tile_object in self.map.tmxdata.objects:
            if (tile_object.name == 'wall' or tile_object.name == 'item'or
                tile_object.name == 'rock' or tile_object.name == 'water'):
                Obstacle(self, tile_object.x, tile_object.y,
                        tile_object.width, tile_object.height)

    def run(self):
        clock = pg.time.Clock()
        map_img = self.map.make_map()
        self.new()
        debugmode = False
        while self.game_running:
            dt = clock.tick(60)
            for event in pg.event.get():

                # Handles Quitting window and cleanup   
                if event.type == pg.QUIT:
                    self.game_running = False
            
            key = pg.key.get_pressed()
            if pg.key.get_pressed()[pg.K_f]:    # hold f to open debug mode
                debugmode = True
            else:
                debugmode = False

            # Handles movement and sprite changes

            self.player.move(dt, self.walls)
            

            self.game_display.fill(WHITE)
            self.game_display.blit(map_img, self.player.adjust_camera(0, 0))
            self.game_display.blit(self.player.player_img,
                                   self.player.player_position())
            
            # draws the hitboxes for player and wall for debugging purposes and updates hitboxes
            if debugmode:
                pg.draw.rect(self.game_display, CYAN, self.player.hit_rect, 1)

            for wall in self.walls:
                if self.player.moving:
                    wall.adjust_camera(self.player.dx, self.player.dy) # (important) updates hitbox for walls
                if debugmode:
                    pg.draw.rect(self.game_display, CYAN, wall.rect, 1)    


            pg.display.update()
        pg.quit()
        quit()


def main():
    game = Game()
    game.run()


print(__name__)
if __name__ == "__main__":
    main()
