import pygame

pygame.init()

# Initialize size variables
display_size = display_width, display_height = 320, 240

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

# Game Loop
while not quit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True

    game_display.fill(white)
    game_display.blit(player_img, player_position)

    pygame.display.update()

pygame.quit()
quit()
