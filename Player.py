import pygame as pg


class Player:
    """ Player class """

    def __init__(self, display_width, display_height):
        self.player_width = 100
        self.player_height = 100
        self.x = (display_width * 0.5 - self.player_width*0.5)
        self.y = (display_height * 0.5 - self.player_height*0.5)

        self.dx = 0
        self.dy = 0

        self.velocity = 0.25
        self.player_img = pg.image.load("images/ash_front_stand.png")
        self.player_sprites = {
            "front_stand": "images/ash_front_stand.png",
            "front_walk_r": "images/ash_front_walk_right.png",
            "front_walk_l": "images/ash_front_walk_left.png",
            "back_stand": "images/ash_back_stand.png",
            "back_walk_r": "images/ash_back_walk_right.png",
            "back_walk_l": "images/ash_back_walk_left.png",
            "left_stand": "images/ash_left_stand.png",
            "left_walk_r": "images/ash_left_walk_right.png",
            "left_walk_l": "images/ash_left_walk_left.png",
            "right_stand": "images/ash_right_stand.png",
            "right_walk_r": "images/ash_right_walk_right.png",
            "right_walk_l": "images/ash_right_walk_left.png",
        }
        self.direction = 'down'
        self.moving = False
        self.foot = 'left'

    def player_position(self):
        """ Returns the player position coordinates """
        return self.x, self.y

    def adjust_camera(self, x, y):
        """ Shifts object by change in direction"""
        return x-self.dx, y-self.dy

    def change_direction(self):
        if self.direction == 'down':
            if not self.moving:
                self.player_img = pg.image.load(
                    self.player_sprites['front_stand'])
            else:
                if self.foot == 'left':
                    self.player_img = pg.image.load(
                        self.player_sprites['front_walk_l'])
                    self.foot = 'right'
                elif self.foot == 'right':
                    self.player_img = pg.image.load(
                        self.player_sprites['front_walk_r'])
                    self.foot = 'left'

        if self.direction == 'up':
            if not self.moving:
                self.player_img = pg.image.load(
                    self.player_sprites['back_stand'])
            else:
                if self.foot == 'left':
                    self.player_img = pg.image.load(
                        self.player_sprites['back_walk_l'])
                    self.foot = 'right'
                elif self.foot == 'right':
                    self.player_img = pg.image.load(
                        self.player_sprites['back_walk_r'])
                    self.foot = 'left'

        if self.direction == 'right':
            if not self.moving:
                self.player_img = pg.image.load(
                    self.player_sprites['right_stand'])
            else:
                if self.foot == 'left':
                    self.player_img = pg.image.load(
                        self.player_sprites['right_walk_l'])
                    self.foot = 'right'
                elif self.foot == 'right':
                    self.player_img = pg.image.load(
                        self.player_sprites['right_walk_r'])
                    self.foot = 'left'

        if self.direction == 'left':
            if not self.moving:
                self.player_img = pg.image.load(
                    self.player_sprites['left_stand'])
            else:
                if self.foot == 'left':
                    self.player_img = pg.image.load(
                        self.player_sprites['left_walk_l'])
                    self.foot = 'right'
                elif self.foot == 'right':
                    self.player_img = pg.image.load(
                        self.player_sprites['left_walk_r'])
                    self.foot = 'left'

    def move(self, dt):
        """ Updates player position """

        dx = self.velocity*dt
        dy = self.velocity*dt

        key = pg.key.get_pressed()
        if key[pg.K_RIGHT]:
            self.dx += dx
            self.moving = True
            self.direction = "right"

        elif key[pg.K_LEFT]:
            self.dx -= dx
            self.moving = True
            self.direction = "left"

        elif key[pg.K_DOWN]:
            self.dy += dy
            self.moving = True
            self.direction = "down"

        elif key[pg.K_UP]:
            self.dy -= dy
            self.moving = True
            self.direction = "up"

        else:
            self.moving = False

        self.change_direction()
