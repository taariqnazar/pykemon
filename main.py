import pygame
from tiledmap import TiledMap

pygame.init()

# Initialize window size variables
display_size = display_width, display_height = 800, 600

# Sets window display size
game_display = pygame.display.set_mode(display_size)

# Sets window title
pygame.display.set_caption("Pokemon")

# Inititalize color variables
black = 0, 0, 0
white = 255, 255, 255


class Player:
    """ Player class """

    def __init__(self):
        self.player_width = 100
        self.player_height = 100
        self.x = (display_width * 0.5 - self.player_width*0.5)
        self.y = (display_height * 0.5 - self.player_height*0.5)

        self.dx = 0
        self.dy = 0

        self.velocity = 0.25
        self.player_img = pygame.image.load("images/ash_front_stand.png")
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
                self.player_img = pygame.image.load(
                    self.player_sprites['front_stand'])
            else:
                if self.foot == 'left':
                    self.player_img = pygame.image.load(
                        self.player_sprites['front_walk_l'])
                    self.foot = 'right'
                elif self.foot == 'right':
                    self.player_img = pygame.image.load(
                        self.player_sprites['front_walk_r'])
                    self.foot = 'left'

        if self.direction == 'up':
            if not self.moving:
                self.player_img = pygame.image.load(
                    self.player_sprites['back_stand'])
            else:
                if self.foot == 'left':
                    self.player_img = pygame.image.load(
                        self.player_sprites['back_walk_l'])
                    self.foot = 'right'
                elif self.foot == 'right':
                    self.player_img = pygame.image.load(
                        self.player_sprites['back_walk_r'])
                    self.foot = 'left'

        if self.direction == 'right':
            if not self.moving:
                self.player_img = pygame.image.load(
                    self.player_sprites['right_stand'])
            else:
                if self.foot == 'left':
                    self.player_img = pygame.image.load(
                        self.player_sprites['right_walk_l'])
                    self.foot = 'right'
                elif self.foot == 'right':
                    self.player_img = pygame.image.load(
                        self.player_sprites['right_walk_r'])
                    self.foot = 'left'

        if self.direction == 'left':
            if not self.moving:
                self.player_img = pygame.image.load(
                    self.player_sprites['left_stand'])
            else:
                if self.foot == 'left':
                    self.player_img = pygame.image.load(
                        self.player_sprites['left_walk_l'])
                    self.foot = 'right'
                elif self.foot == 'right':
                    self.player_img = pygame.image.load(
                        self.player_sprites['left_walk_r'])
                    self.foot = 'left'

    def move(self, dt):
        """ Updates player position """

        dx = self.velocity*dt
        dy = self.velocity*dt

        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            #ash.x += self.velocity*dt
            ash.dx += dx
            ash.moving = True
            ash.direction = "right"

        elif key[pygame.K_LEFT]:
            #ash.x -= self.velocity*dt
            ash.dx -= dx
            ash.moving = True
            ash.direction = "left"

        elif key[pygame.K_DOWN]:
            #ash.y += self.velocity*dt
            ash.dy += dy
            ash.moving = True
            ash.direction = "down"

        elif key[pygame.K_UP]:
            #ash.y -= self.velocity*dt
            ash.dy -= dy
            ash.moving = True
            ash.direction = "up"

        else:
            ash.moving = False


ash = Player()


clock = pygame.time.Clock()
dt = 0  # deltatime
# Game Loop

map = TiledMap('poke.tmx')
map_img = map.make_map()

quit_game = False
while not quit_game:
    dt = clock.tick(60)  # fps 30 ?
    for event in pygame.event.get():

        # Handles Quitting window and cleanup
        if event.type == pygame.QUIT:
            quit_game = True

    ash.move(dt)

    # Added change direction logic here and it works, since KEYDOWN only runs once when the key is pressed down
    ash.change_direction()

    game_display.fill(white)
    game_display.blit(map_img, ash.adjust_camera(0, 0))
    game_display.blit(ash.player_img, ash.player_position())

    r_x, r_y = ash.adjust_camera(0, 0)
    pygame.draw.rect(game_display, black, [r_x, r_y, 50, 50])

    pygame.display.update()


pygame.quit()
quit()
