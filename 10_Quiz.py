import random
import pygame
############################################################################
# 초기화
pygame.init()
charater_speed = 5
# Define the screen size
screen_width = 600
screen_height = 800

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the caption of the window
pygame.display.set_caption("똥 Game")

# FPS 제어
clock = pygame.time.Clock()

############################################################################
#      사용자 게임 초기화( 배경, 게임 이미지 로딩 등)
background = pygame.image.load(
    "D:/Projects/Python/Pygame_Basic/background.png"
)
character = pygame.image.load("D:/Projects/Python/Pygame_Basic/character.png")
ddong_img = pygame.image.load("D:/Projects/Python/Pygame_Basic/ddong.png")

charater_size = character.get_size()
ddong_size = ddong_img.get_size()

to_x = int((screen_width / 2)) - int((charater_size[0] / 2))
to_y = int((screen_height)) - int((charater_size[1]))
ddong_x = random.randint(0, screen_width - ddong_size[1])
ddong_y = 0

ddong_list = [[ddong_x, 0, ddong_size[0], ddong_size[1]]]
# 똥 낙하 간격
delay = 50
delay_cnt = 0

# 이벤트 루프
running = True

while running:

    dt = clock.tick(30)

    fps = clock.get_fps()
    ################################
    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ##########################################
    #  3. 게임 케릭터 위치 이동
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            to_x -= charater_speed
        elif event.key == pygame.K_RIGHT:
            to_x += charater_speed

    ##########################################
    #  4. 똥 낙하
    delay_cnt += 1
    if delay_cnt >= delay:
        delay_cnt = 0
        ddong_list.append([
            random.randint(0, screen_width - ddong_size[0]),
            0,
            ddong_size[0],
            ddong_size[1]
        ])

    for ddong in ddong_list:
        if ddong[1] < screen_height - ddong_size[1]:
            ddong[1] = ddong[1] + 5
        else:
            ddong_list.remove(ddong)
            delay -= 5    
        ##########################################
        #  5. 충돌 처리
        if (
            to_x <= ddong[0] + ddong_size[0] and
            to_x + charater_size[0] >= ddong[0] and
            to_y <= ddong[1] + ddong_size[1] and
            to_y + charater_size[1] >= ddong_y
        ):
            print("Game Over!")
            running = False

    ##########################################
    #  6. 화면 그리기
    screen.blit(background, (0, 0))
    screen.blit(character, (to_x, to_y))
    for ddong in ddong_list:
        screen.blit(ddong_img, (ddong[0], ddong[1]))

    pygame.display.update()  # Update the screen with all drawings

pygame.quit()
