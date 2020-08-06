import pygame as pg

class Obstacle(pg.sprite.Sprite):
    def __init__(self, game , x, y, w, h):
        self.groups = game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.rect = pg.Rect(x, y, w, h)
       
        self.x= x
        self.y =y
        self.rect.x = x
        self.rect.y= y
        self.hit_rect = pg.Rect(self.x, self.y, 100, 100)
        #print(self.hit_rect)
    
    def adjust_camera(self, x, y):
        self.rect.x -= x 
        self.rect.y -= y
        self.hit_rect = pg.Rect(self.rect.x, self.rect.y, 100, 100)

