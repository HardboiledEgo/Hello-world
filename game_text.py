import pygame

pygame.init()

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

size = (500, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Professor Craven's Cool Game")

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
    # --- Game logic should go here
 
    # --- Drawing code should go here
    # Select the font to use, size, bold, italics
    font = pygame.font.SysFont('Calibri', 25, True, False)
 
    # Render the text. "True" means anti-aliased text.
    text = font.render("My text",True,BLACK)
    screen.blit(text, [200, 250])

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
    
pygame.quit()