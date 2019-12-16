# Import a library of functions called 'pygame'
import pygame
import random
 
# Initialize the game engine
pygame.init()
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
PI = 3.141592653
 
# Set the height and width of the screen

done = False
backdoor = BLACK
height_x = 800
width_y = 600
size = (height_x, width_y)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Snow!")
 
# Loop until the user clicks the close button.
clock = pygame.time.Clock()
 
# Loop as long as done == False
while not done:
    
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
 
    # All drawing code happens after the for loop and but
    # inside the main while not done loop.
 
    # Clear the screen and set the screen background
    screen.fill(backdoor)
    
    for i in range(50):
        x=random.randrange(0,height_x)
        y=random.randrange(0,width_y)
        pygame.draw.circle(screen, WHITE, [x,y], 2)
 
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()
 
    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(60)
 
# Be IDLE friendly
pygame.quit()