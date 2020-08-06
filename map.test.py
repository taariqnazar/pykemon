import pygame as pg

import sys

W = 0  # Water
S = 1  # Sand
G = 2  # Grass
F = 3  # Forest

BLUE = 0, 0, 255
SANDYELLOW = 194, 178, 128
GRASSGREEN = 124, 252, 0
FORESTGREEN = 0, 100, 0


# Assign color to tile
tile_colour = {
    W: BLUE,
    S: SANDYELLOW,
    G: GRASSGREEN,
    F: FORESTGREEN
}

""" Create Map """
map1 = [[W, S, G, F, F, F, G, S, W, W, W, W],
        [W, S, G, F, F, F, G, S, W, W, W, W],
        [W, S, G, F, F, F, G, S, W, W, W, S],
        [W, S, G, F, F, F, G, S, G, G, W, S],
        [W, S, G, F, F, F, G, S, W, W, W, W],
        [W, S, G, F, F, F, G, S, W, W, W, S],
        [W, S, G, F, F, F, G, S, S, W, W, S],
        [W, S, G, F, F, F, G, S, W, W, W, W],
        [W, S, G, F, F, F, G, S, W, W, W, W],
        [W, S, G, F, F, F, G, S, W, W, W, W],
        [W, S, G, F, F, F, G, S, W, W, W, W],
        [W, S, G, F, F, F, G, S, W, W, W, W]
        ]

tile_size = 30
map_width = 12
map_height = 12


pg.init()

display = pg.display.set_mode((tile_size*map_width, tile_size*map_height))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    for row in range(map_height):
        for col in range(map_width):
            pg.draw.rect(display, tile_colour[map1[row][col]],
                         (col*tile_size, row*tile_size, tile_size, tile_size))

    pg.display.update()
