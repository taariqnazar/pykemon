import pygame as pg
from TiledMap import TiledMap
from Player import Player

BLACK = 0, 0, 0
WHITE = 255, 255, 255


class Game:
    def __init__(self, display_size=(800, 600), caption="Pokemon"):
        pg.init()

        self.display_size = display_size

        self.game_display = pg.display.set_mode(display_size)
        pg.display.set_caption(caption)

        self.player = Player(
            display_width=display_size[0], display_height=display_size[1])
        self.map = TiledMap("resources/town.tmx")

        self.game_running = True

    def run(self):
        clock = pg.time.Clock()
        map_img = self.map.make_map()

        while self.game_running:
            dt = clock.tick(60)
            for event in pg.event.get():

                # Handles Quitting window and cleanup
                if event.type == pg.QUIT:
                    self.game_running = False

            # Handles movement and sprite changes
            self.player.move(dt)

            # Draws what should be displayed
            self.game_display.fill(WHITE)
            self.game_display.blit(map_img, self.player.adjust_camera(0, 0))
            self.game_display.blit(self.player.player_img,
                                   self.player.player_position())

            # Testiong moving rectangle
            r_x, r_y = self.player.adjust_camera(0, 0)
            pg.draw.rect(self.game_display, BLACK, [r_x, r_y, 50, 50])

            pg.display.update()

        pg.quit()
        quit()


def main():
    game = Game()
    game.run()


print(__name__)
if __name__ == "__main__":
    main()
