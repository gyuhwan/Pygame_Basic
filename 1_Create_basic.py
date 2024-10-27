import pygame

pygame.init()

# Define the screen size
screen_width = 800
screen_height = 600

# Create the screen

screen = pygame.display.set_mode((screen_width, screen_height))

# Set the caption of the window
pygame.display.set_caption("Dolpari5 Game")

# 이벤트 루프

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Event loop    

pygame.quit()


