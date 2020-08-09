import pygame as pg
from config import DISPLAY_SIZE


class Player(pg.sprite.Sprite):
    """ Player class """

    def __init__(self):
        self.player = pg.sprite.Group()
        pg.sprite.Sprite.__init__(self, self.player)

        self.player_width = 20
        self.player_height = 20

        display_width, display_height = DISPLAY_SIZE

        self.x = (display_width * 0.5 - self.player_width*0.5)
        self.y = (display_height * 0.5 - self.player_height*0.5)

        self.dx = 0
        self.dy = 0
        # deltax/y = distance to move
        self.deltax = 0
        self.deltay = 0

        self.velocity = 0.25
        self.player_img = pg.image.load("resources/images/ash_front_stand.png")

        self.hit_rect = pg.Rect(
            self.x, self.y, self.player_width, self.player_height)  # hitbox

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
            self.player_img = pg.image.load(img)

        else:
            l = len(self.player_sprites[self.direction]["idle"])
            img = self.player_sprites[self.direction]["idle"][int(
                l*self.counter / FPS)]
            self.player_img = pg.image.load(img)

        self.counter = (self.counter + 1) % 60

    def move(self, dt, obstacles):
        """ Updates player position """
        key = pg.key.get_pressed()
        keydict = {
            'right': pg.K_RIGHT,
            'left': pg.K_LEFT,
            'up': pg.K_UP,
            'down': pg.K_DOWN
        }

        if self.velocity == 0:
            for dir in ['right', 'left', 'up', 'down']:
                if self.direction == dir:
                    if key[keydict[dir]] == 1:
                        self.change_direction()
                        return 1
                    elif key[keydict[dir]] == 0:
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
        self.check_collision(obstacles)

    def check_collision(self, group):
        evn = ""
        for key in group.keys():
            obstacles = []
            for obstacle in group[key]:
                obstacles.append(obstacle.rect)

            hit = self.hit_rect.collidelist(obstacles)
            #print(hit)
            #(print(obstacles))
            hits = False if hit == -1 else True
            
            if hits: 
                
                evn = key
                print(evn)
                break

        
    
        if evn == 'obstacles':
            
            #
            obstacles = []
            for obstacle in group[evn]:
                obstacles.append(obstacle.rect)

            hit = self.hit_rect.collidelist(obstacles)
            hits = False if hit == -1 else True

            
            
            obstacles = []
            for obstacle in group[evn]:
                obstacles.append(obstacle.rect)

            hit = self.hit_rect.collidelist(obstacles)
            hits = False if hit == -1 else True
            
            #
            
            if self.direction == 'left' or self.direction == 'right':
                if hits:
                    if obstacles[hit].centerx > self.hit_rect.centerx:
                        if self.direction == 'right':
                            if self.hit_rect.bottomright[0] >= obstacles[hit].bottomleft[0]:
                                overlap = self.hit_rect.bottomright[0] - \
                                    obstacles[hit].bottomleft[0]
                                if self.moving == False:
                                    self.dx -= overlap
                                    self.moving = True
                                else:
                                    self.dx -= self.deltax + overlap
                                    self.velocity = 0

                    elif obstacles[hit].centerx < self.hit_rect.centerx:
                        if self.direction == 'left':
                            if self.hit_rect.bottomleft[0] <= obstacles[hit].bottomright[0]:
                                overlap = self.hit_rect.bottomleft[0] - \
                                    obstacles[hit].bottomright[0]
                                if self.moving == False:
                                    self.dx -= overlap
                                    self.moving = True
                                else:
                                    self.dx += (self.deltax - overlap)
                                    self.velocity = 0

            elif self.direction == 'up' or self.direction == 'down':
                if hits:
                    if obstacles[hit].centery < self.hit_rect.centery:
                        if self.direction == 'up':
                            if self.hit_rect.topright[1] <= obstacles[hit].bottomright[1]:
                                overlap = self.hit_rect.topright[1] - \
                                    obstacles[hit].bottomright[1]
                                if self.moving == False:
                                    self.dy -= overlap
                                    self.moving = True

                                else:
                                    self.dy -= (-self.deltay + overlap)
                                    self.velocity = 0

                    if obstacles[hit].centery >= self.hit_rect.centery:
                        if self.direction == 'down':
                            if self.hit_rect.bottomright[1] >= obstacles[hit].topright[1]:
                                overlap = self.hit_rect.bottomright[1] - \
                                    obstacles[hit].topright[1]
                                if self.moving == False:
                                    self.dy -= overlap
                                    self.moving = True
                                else:
                                    self.dy -= (self.deltay + overlap)
                                    self.velocity = 0
        
        elif evn == "door":
            if self.direction == 'up':
                
                print(self.direction)
                return True
                
            
            obstacles = []
            for obstacle in group[evn]:
                obstacles.append(obstacle.rect)

            hit = self.hit_rect.collidelist(obstacles)
            hits = False if hit == -1 else True
            