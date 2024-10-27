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
background = pygame.image.load("D:/Projects/Python/Pygame_Basic/background.png")
character = pygame.image.load("D:/Projects/Python/Pygame_Basic/character.png")

character_size = character.get_size()
character_width = character_size[0]
character_height = character_size[1]

character_x = (screen_width // 2) - (character_width // 2)

character_y = screen_height - character_height

# 이벤트 루프
   
running = True
to_x = 0
to_y = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= 5
            elif event.key == pygame.K_RIGHT:
                to_x += 5
            elif event.key == pygame.K_UP:
                to_y -= 5
            elif event.key == pygame.K_DOWN:
                to_y += 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x += to_x
    character_y += to_y

    # Character boundary check
    if character_x < 0:
        character_x = 0
    elif character_x > screen_width - character_width:
        character_x = screen_width - character_width

    if character_y < 0:
        character_y = 0
    elif character_y > screen_height - character_height:
        character_y = screen_height - character_height

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































