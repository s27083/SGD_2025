import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300
DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)
catImg = pygame.image.load('cat.png')

# Create a flipped version for the second cat
cat2Img = pygame.transform.flip(catImg, True, False)  # Flip horizontally

# First cat settings
cat1x = 10
cat1y = 10
cat1_direction = 'right'

# Second cat settings
cat2x = WINDOW_WIDTH - 74  
cat2y = WINDOW_HEIGHT - 74 
cat2_speed_x = 3
cat2_speed_y = 4

# Get the dimensions of the cat image
cat_width = catImg.get_width()
cat_height = catImg.get_height()

while True: # the main game loop
    DISPLAYSURF.fill(WHITE)

    # First cat movement (following predetermined path)
    if cat1_direction == 'right':
        cat1x += 5
        if cat1x == 280:
            cat1_direction = 'down'
    elif cat1_direction == 'down':
        cat1y += 5
        if cat1y == 220:
            cat1_direction = 'left'
    elif cat1_direction == 'left':
        cat1x -= 5
        if cat1x == 10:
            cat1_direction = 'up'
    elif cat1_direction == 'up':
        cat1y -= 5
        if cat1y == 10:
            cat1_direction = 'right'

    # Second cat movement (bouncing off edges)
    cat2x += cat2_speed_x
    cat2y += cat2_speed_y
    
    # Bounce off the edges with proper boundary checking
    if cat2x <= 0:
        cat2x = 0
        cat2_speed_x = abs(cat2_speed_x)  # Move right
    elif cat2x >= WINDOW_WIDTH - cat_width:
        cat2x = WINDOW_WIDTH - cat_width
        cat2_speed_x = -abs(cat2_speed_x)  # Move left
        
    if cat2y <= 0:
        cat2y = 0
        cat2_speed_y = abs(cat2_speed_y)  # Move down
    elif cat2y >= WINDOW_HEIGHT - cat_height:
        cat2y = WINDOW_HEIGHT - cat_height
        cat2_speed_y = -abs(cat2_speed_y)  # Move up

    # Draw both cats
    DISPLAYSURF.blit(catImg, (cat1x, cat1y))
    DISPLAYSURF.blit(cat2Img, (cat2x, cat2y))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)