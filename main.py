import pygame as pg
from TiledMap import TiledMap
from Player import Player
from Obstacle import Obstacle

BLACK = 0, 0, 0
WHITE = 255, 255, 255
CYAN = 0, 255, 255

def collide_hit_rect(one, two):
    return one.hit_rect.colliderect(two.rect)

def check_collision(sprite, group):
    hits = pg.sprite.spritecollide(sprite, group, False, collide_hit_rect)
    if hits:
        print('wall')


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
            if tile_object.name == 'wall':
                Obstacle(self, tile_object.x, tile_object.y,
                        tile_object.width, tile_object.height)
    def run(self):
        clock = pg.time.Clock()
        map_img = self.map.make_map()
        self.new()

        while self.game_running:
            dt = clock.tick(60)
            for event in pg.event.get():

                # Handles Quitting window and cleanup   
                if event.type == pg.QUIT:
                    self.game_running = False



            # Handles movement and sprite changes
            self.player.move(dt)
            check_collision(self.player, self.walls)

            # Draws what should be displayed
            self.game_display.fill(WHITE)
            self.game_display.blit(map_img, self.player.adjust_camera(0, 0))
            self.game_display.blit(self.player.player_img,
                                   self.player.player_position())
                        # debug
            pg.draw.rect(self.game_display, CYAN, self.player.hit_rect, 1)
            
            for wall in self.walls:
                wall.adjust_camera(self.player.dx, self.player.dy) # actually important, updates hitbox
                pg.draw.rect(self.game_display, CYAN, wall.hit_rect, 1)
                #print(wall.hit_rect)    


            pg.display.update()
        pg.quit()
        quit()


def main():
    game = Game()
    game.run()


print(__name__)
if __name__ == "__main__":
    main()
