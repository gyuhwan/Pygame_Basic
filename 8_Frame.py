import pygame
############################################################################
## 초기화
pygame.init()

# Define the screen size
screen_width = 800
screen_height = 600

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the caption of the window
pygame.display.set_caption("Dolpari5 Game")

# FPS 제어
clock = pygame.time.Clock()

############################################################################
#      사용자 게임 초기화( 배경, 게임 이미지 로딩 등)

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

    ##########################################
    #  4. 충돌 처리

    ##########################################
    #  5. 화면 그리기

    pygame.display.update()  # Update the screen with all drawings


pygame.quit()
