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

x_change = 0
y_change = 0

# Game Loop
while not quit_game:
    for event in pygame.event.get():
        # Handles Quitting window and cleanup
        if event.type == pygame.QUIT:
            quit_game = True

        # Handles moving logic
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            if event.key == pygame.K_RIGHT:
                x_change = 5
            if event.key == pygame.K_UP:
                y_change = -5
            if event.key == pygame.K_DOWN:
                y_change = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_change = 0

    # Updates palyer position values
    x += x_change
    y += y_change

    game_display.fill(white)
    game_display.blit(player_img, player_position)

    pygame.display.update()

pygame.quit()
quit()
