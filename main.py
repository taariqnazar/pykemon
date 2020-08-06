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


class player():
    """ Player class """

    def __init__(self):
        self.player_width = 100
        self.player_height = 100
        self.x = (display_width * 0.45)
        self.y = (display_height * 0.8)
        self.x_change = 0
        self.y_change = 0

        self.speed = 0.25
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
        self.foot = 'left'

    def change_direction(self):
        if self.direction == 'down':
            if self.y_change == 0:
                self.player_img = pygame.image.load(
                    self.player_sprites['front_stand'])
            elif self.foot == 'left':
                self.player_img = pygame.image.load(
                    self.player_sprites['front_walk_l'])
                self.foot = 'right'
            elif self.foot == 'right':
                self.player_img = pygame.image.load(
                    self.player_sprites['front_walk_r'])
                self.foot = 'left'

        if self.direction == 'up':
            if self.y_change == 0:
                self.player_img = pygame.image.load(
                    self.player_sprites['back_stand'])
            elif self.foot == 'left':
                self.player_img = pygame.image.load(
                    self.player_sprites['back_walk_l'])
                self.foot = 'right'
            elif self.foot == 'right':
                self.player_img = pygame.image.load(
                    self.player_sprites['back_walk_r'])
                self.foot = 'left'

        if self.direction == 'right':
            if self.x_change == 0:
                self.player_img = pygame.image.load(
                    self.player_sprites['right_stand'])
            elif self.foot == 'left':
                self.player_img = pygame.image.load(
                    self.player_sprites['right_walk_l'])
                self.foot = 'right'
            elif self.foot == 'right':
                self.player_img = pygame.image.load(
                    self.player_sprites['right_walk_r'])
                self.foot = 'left'

        if self.direction == 'left':
            if self.x_change == 0:
                self.player_img = pygame.image.load(
                    self.player_sprites['left_stand'])
            elif self.foot == 'left':
                self.player_img = pygame.image.load(
                    self.player_sprites['left_walk_l'])
                self.foot = 'right'
            elif self.foot == 'right':
                self.player_img = pygame.image.load(
                    self.player_sprites['left_walk_r'])
                self.foot = 'left'

    def player_position(self):
        """ Returns the player position coordinates """
        return self.x, self.y

    def move(self, dt):
        """ Updates player position """

        # Handles keyevents, i.e moving etc.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ash.x_change = -ash.speed * dt
                ash.y_change = 0
                ash.direction = 'left'
            elif event.key == pygame.K_RIGHT:
                ash.x_change = ash.speed * dt
                ash.y_change = 0
                ash.direction = "right"
            elif event.key == pygame.K_UP:
                ash.y_change = -ash.speed * dt
                ash.x_change = 0
                ash.direction = "up"
            elif event.key == pygame.K_DOWN:
                ash.y_change = ash.speed * dt
                ash.x_change = 0
                ash.direction = 'down'

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                ash.x_change = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                ash.y_change = 0


ash = player()


quit_game = False
clock = pygame.time.Clock()

dt = 0  # deltatime
# Game Loop

#screen.fill(white)
map = TiledMap('poke.tmx')

map_img =map.make_map()
while not quit_game:
    dt = clock.tick(60)  # fps 30 ?
    for event in pygame.event.get():

        # Handles Quitting window and cleanup
        if event.type == pygame.QUIT:
            quit_game = True
        ash.move(dt)

    # Added change direction logic here and it works, since KEYDOWN only runs once when the key is pressed down
    ash.change_direction()

    ash.x += ash.x_change
    ash.y += ash.y_change
    game_display.blit(map_img,(0,0))

    
    game_display.blit(ash.player_img, ash.player_position())

    pygame.display.update()


pygame.quit()
quit()
