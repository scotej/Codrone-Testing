# Import and initialize the pygame library
import pygame
from codrone_edu import *

pygame.init()

# Set up the drawing    window
screen = pygame.display.set_mode([500, 500])

# Initial position of the circle
x, y = 250, 250

# Set initial velocities
velocity_x, velocity_y = 0, 0
speed = 5  # Speed of the circle when an arrow key is pressed

# Run until the user asks to quit
running = True
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check for key down event
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocity_x = speed
            if event.key == pygame.K_UP:
                velocity_y = -speed
        # Check for key up event
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                velocity_x = 0
            if event.key == pygame.K_UP:
                velocity_y = 0
    x += velocity_x
    y += velocity_y
    # Fill the background with blue
    screen.fill((116, 197, 212))

    # Draw a solid purple circle at the new position
    pygame.draw.circle(screen, (157, 84, 196), (x, y), 75)

    # Flip the display
    pygame.display.flip()

    # Limit frames per second
    pygame.time.Clock().tick(30)

# Done! Time to quit.
pygame.quit()
