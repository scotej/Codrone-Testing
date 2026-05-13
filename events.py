# Import and initialize the pygame library
import pygame
from codrone_edu.drone import *

pygame.init()

# Set up a small window so pygame can read the keyboard
screen = pygame.display.set_mode([500, 500])
pygame.display.set_caption("Drone Keyboard Control")

# Connect to the drone
drone = Drone()
drone.pair()

speed = 8  # how strong each movement is

clock = pygame.time.Clock()

# Run until the user asks to quit
running = True
while running:
    # Check the events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # key pressed down
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_t:
                drone.takeoff()
            if event.key == pygame.K_l:
                drone.land()
            if event.key == pygame.K_SPACE:
                drone.emergency_stop()
            if event.key == pygame.K_h:
                # hover / stop all movement
                drone.set_pitch(0)
                drone.set_roll(0)
                drone.set_throttle(0)
                drone.set_yaw(0)

            # wasd - fly forward/back/left/right
            if event.key == pygame.K_w:
                drone.set_pitch(speed)
            if event.key == pygame.K_s:
                drone.set_pitch(-speed)
            if event.key == pygame.K_a:
                drone.set_roll(-speed)
            if event.key == pygame.K_d:
                drone.set_roll(speed)

            # arrows - up/down and rotate
            if event.key == pygame.K_UP:
                drone.set_throttle(speed)
            if event.key == pygame.K_DOWN:
                drone.set_throttle(-speed)
            if event.key == pygame.K_LEFT:
                drone.set_yaw(speed)
            if event.key == pygame.K_RIGHT:
                drone.set_yaw(-speed)

        # key let go - stop that movement
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                drone.set_pitch(0)
            if event.key == pygame.K_a or event.key == pygame.K_d:
                drone.set_roll(0)
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                drone.set_throttle(0)
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                drone.set_yaw(0)

    # send the current movement values to the drone
    drone.move()

    # Fill the background with blue
    screen.fill((116, 197, 212))

    # Flip the display
    pygame.display.flip()

    # Limit frames per second
    clock.tick(30)

# Done! Land the drone and quit.
drone.land()
drone.close()
pygame.quit()
