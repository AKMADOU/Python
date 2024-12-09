import pygame     
import time

## https://learnpythontherightway.com/chapter/chapter-17.html

def main():

    pygame.init()    # Prepare the PyGame module for use
    main_surface = pygame.display.set_mode((480, 240))

    # Load an image to draw. Substitute your own.
    # PyGame handles gif, jpg, png, etc. image types.
    ball = pygame.image.load("ball.png")  

    # Create a font for rendering text
    my_font = pygame.font.SysFont("Courier", 16)

    frame_count = 0
    frame_rate = 0
    t0 = time.process_time()
    
    ximgstart=100
    yimgstart=70

    while True:

        # Look for an event from keyboard, mouse, joystick, etc.
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:   # Window close button clicked?
            break                    # Leave game loop

        # Do other bits of logic for the game here
      
        # Completely redraw the surface, starting with background
        main_surface.fill((0, 200, 255))

        # Put a red rectangle somewhere on the surface
        main_surface.fill((255,0,0), (300, 100, 150, 90))

    
      
        # Copy our image to the surface, at this (x,y) posn
        main_surface.blit(ball, (ximgstart, yimgstart))
        #ximgstart = ximgstart + 1
        #yimgstart = yimgstart + 10
            
        # Now that everything is drawn, put it on display!
        pygame.display.flip()
        
       

    pygame.quit()   


main()