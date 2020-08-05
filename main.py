import pygame

pygame.init()

# Initialize size variables
display_size = display_width, display_height = 800, 600

# Sets display size
game_display = pygame.display.set_mode(display_size)
# Sets window title
pygame.display.set_caption("Pokemon")

# Inititalize color variables
black = 0, 0, 0
white = 255, 255, 255

player_img = pygame.image.load("images/ash_front_stand.png")

player_position = x, y = 1, 1

quit_game = False

# Player class


class player():

    def __init__(self):
        self.x = (display_width * 0.45)
        self.y = (display_height * 0.8)
        self.x_change = 0
        self.y_change = 0

        self.speed = 0

        self.player_width = 100
        self.player_height = 100

    def player_position(self):
        """ Returns the player position coordinates """

        return self.x, self.y


# Game Loop
ash = player()
while not quit_game:

    for event in pygame.event.get():
        # Handles Quitting window and cleanup
        if event.type == pygame.QUIT:
            quit_game = True

        # Handles keyevents, i.e moving etc.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ash.x_change = -1
            elif event.key == pygame.K_RIGHT:
                ash.x_change = 1
            elif event.key == pygame.K_UP:
                ash.y_change = -1
            elif event.key == pygame.K_DOWN:
                ash.y_change = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                ash.x_change = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                ash.y_change = 0

    # Looks at the boundaries, cannot move outside of boundaries, Issue gets stuck on edge
    if ash.x > display_width - ash.player_width or ash.x < 0:
        ash.x_change = 0

    if ash.y > display_height - ash.player_height or ash.y < 0:
        ash.y_change = 0

    ash.x += ash.x_change
    ash.y += ash.y_change

    game_display.fill(white)
    game_display.blit(player_img, ash.player_position())

    pygame.display.update()

pygame.quit()
quit()
