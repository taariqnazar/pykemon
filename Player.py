import pygame as pg
#PLAYER_HIT_RECT = pg.Rect(0, 0, 100, 100)

class Player(pg.sprite.Sprite):
    """ Player class """

    def __init__(self, display_width, display_height):
        self.player = pg.sprite.Group()
        pg.sprite.Sprite.__init__(self, self.player)

        self.player_width = 50
        self.player_height = 50
        self.x = (display_width * 0.5 - self.player_width*0.5)
        self.y = (display_height * 0.5 - self.player_height*0.5)
        

        self.dx = 0
        self.dy = 0

        self.deltax = 0
        self.deltay = 0

        self.velocity = 0.25
        self.player_img = pg.image.load("resources/images/ash_front_stand.png")
        # rect
        #self.rect = self.player_img.get_rect()
        self.hit_rect = pg.Rect(self.x+ 7.5, self.y + 7.5, self.player_height, self.player_height)
        #self.hit_rect.center = self.rect.center
        print(self.hit_rect)

        self.player_sprites = {
            "left": {
                "idle": ["resources/images/ash_left_stand.png"],
                "moving": [
                    "resources/images/ash_left_walk_left.png",
                    # "resources/images/ash_left_stand.png",
                    "resources/images/ash_left_walk_right.png"
                ]},
            "right": {
                "idle": ["resources/images/ash_right_stand.png"],
                "moving": [
                    "resources/images/ash_right_walk_left.png",
                    # "resources/images/ash_right_stand.png",
                    "resources/images/ash_right_walk_right.png"
                ]},
            "up": {
                "idle": ["resources/images/ash_back_stand.png"],
                "moving": [
                    "resources/images/ash_back_walk_left.png",
                    # "resources/images/ash_back_stand.png",
                    "resources/images/ash_back_walk_right.png"
                ]},
            "down": {
                "idle": ["resources/images/ash_front_stand.png"],
                "moving": [
                    "resources/images/ash_front_walk_left.png",
                    # "resources/images/ash_front_stand.png",
                    "resources/images/ash_front_walk_right.png"
                ]}
        }
        self.counter = 0

        self.direction = 'down'
        self.moving = False

    def player_position(self):
        """ Returns the player position coordinates """
        return self.x, self.y

    def adjust_camera(self, x, y):
        """ Shifts object by change in direction"""
        return x-self.dx, y-self.dy

    def change_direction(self):
        FPS = 60
        if self.moving:
            l = len(self.player_sprites[self.direction]["moving"])
            
            img = self.player_sprites[self.direction]["moving"][int(
                l*self.counter / FPS)]
            self.counter += 1
            self.player_img = pg.image.load(img)

        else:
            l = len(self.player_sprites[self.direction]["idle"])
            img = self.player_sprites[self.direction]["idle"][int(
                l*self.counter / FPS)]
            self.player_img = pg.image.load(img)
            self.counter += 1

        self.counter = self.counter % 60

    def move(self, dt):
        """ Updates player position """
        key = pg.key.get_pressed()

        if self.velocity == 0:
            if self.direction == 'right':
                if key[pg.K_RIGHT] == 1:
                   return 1
                elif key[pg.K_RIGHT] == 0 :
                    self.velocity = 0.25                

            if self.direction == 'left':
                if key[pg.K_LEFT] == 1:
                    return 1
                elif key[pg.K_LEFT] == 0 :
                    self.velocity = 0.25  

            if self.direction == 'up':
                if key[pg.K_UP] == 1:
                    return 1
                elif key[pg.K_UP] == 0 :
                    self.velocity = 0.25  

            if self.direction == 'down':
                if key[pg.K_DOWN] == 1:
                   return 1
                elif key[pg.K_DOWN] == 0 :
                    self.velocity = 0.25  
    

        self.deltax = self.velocity*dt
        self.deltay = self.velocity*dt

        if key[pg.K_RIGHT]:
            self.dx += self.deltax
            self.moving = True
            self.direction = "right"

        elif key[pg.K_LEFT]:
            self.dx -= self.deltax
            self.moving = True
            self.direction = "left"

        elif key[pg.K_DOWN]:
            self.dy += self.deltay
            self.moving = True
            self.direction = "down"

        elif key[pg.K_UP]:
            self.dy -= self.deltay
            self.moving = True
            self.direction = "up"

        else:
            self.moving = False

        self.change_direction()
        
  