import pygame

pygame.init()

# Define the screen size
screen_width = 800
screen_height = 600

# Create the screen

screen = pygame.display.set_mode((screen_width, screen_height))

# Set the caption of the window
pygame.display.set_caption("Dolpari5 Game")

#배경 이미지 로드
background = pygame.image.load("D:/Projects/Python/Pygame__Basic/background.png")

character = pygame.image.load("D:/Projects/Python/Pygame__Basic/character.png")
character_size = character.get_size()
character_width = character_size[0]
character_height = character_size[1]

character_x = (screen_width // 2) - (character_width // 2)

character_y = screen_height - character_height



# 이벤트 루프
    
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Background image draw
    screen.blit(background, (0, 0))
    # Character draw
    screen.blit(character, (character_x, character_y))

    # FPS 제어
    clock = pygame.time.Clock()
    clock.tick(60)  # 60 fps로 제어합니다. 30 fps = 1/30, 60 fps = 1/60

    # Drawing code here...
    pygame.display.update()  # Update the screen with all drawings

    # FPS 제어
    clock = pygame.time.Clock()
    clock.tick(60)  # 60 fps로 제어합니다. 30 fps = 1/30, 60 fps = 1/60

    # Game logic here...
    # ...   
    # Clear the screen before drawing again
    #screen.fill((0, 0, 0))  # Black background color


    # Event loop    

pygame.quit()


