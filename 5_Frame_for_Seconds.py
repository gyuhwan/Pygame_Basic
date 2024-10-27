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
enemy = pygame.image.load("D:/Projects/Python/Pygame_Basic/enemy.png")

character_size = character.get_size()
character_width = character_size[0]
character_height = character_size[1]
character_x = (screen_width // 2) - (character_width // 2)
character_y = screen_height - character_height


enemy_size = enemy.get_size()
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x = (screen_width // 2) - (enemy_width // 2)
enemy_y = (screen_height // 2) - (enemy_height // 2)

# 이벤트 루프
   
running = True
to_x = 0
to_y = 0
dt = 0
fps = 0
clock = pygame.time.Clock()
charater_speed = 0.3
while running:

    dt = clock.tick(30)
    fps = clock.get_fps()
  #  print("FPS : {:.2f} fps".format(fps))
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= charater_speed  
            elif event.key == pygame.K_RIGHT:
                to_x += charater_speed
            elif event.key == pygame.K_UP:
                to_y -= charater_speed
            elif event.key == pygame.K_DOWN:
                to_y += charater_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x += to_x * dt
    character_y += to_y * dt

    # Character boundary check
    if character_x < 0:
        character_x = 0
    elif character_x > screen_width - character_width:
        character_x = screen_width - character_width

    if character_y < 0:
        character_y = 0
    elif character_y > screen_height - character_height:
        character_y = screen_height - character_height

    character_rect = character.get_rect()
    character_rect.x = character_x
    character_rect.y = character_y

    # Enemy boundary check
    enemy_rect = enemy.get_rect()
    enemy_rect.x = enemy_x
    enemy_rect.y = enemy_y

    if character_rect.colliderect(enemy_rect) :
        print("충돌하였습느다!!!!\n")
        running = False
        
    # Background image draw
    screen.blit(background, (0, 0))
    # Character draw
    screen.blit(character, (character_x, character_y))

    screen.blit(enemy, (enemy_x, enemy_y))

    # FPS 제어
    clock = pygame.time.Clock()
    clock.tick(60)  # 60 fps로 제어합니다. 30 fps = 1/30, 60 fps = 1/60

    # Drawing code here...
    pygame.display.update()  # Update the screen with all drawings

    # Game logic here...
    


    # Clear the screen before drawing again
    #screen.fill((0, 0, 0))  # Black background color


    # Event loop    

pygame.quit()































