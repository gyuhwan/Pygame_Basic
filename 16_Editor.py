import pygame

# 초기화
pygame.init()

# 화면 설정
screen_width = 400
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("텍스트박스 with 스크롤바")

# 색상 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
DARK_GRAY = (150, 150, 150)

# 폰트 설정
font = pygame.font.Font(None, 32)

class ScrollBar:
    def __init__(self, x, y, width, height, content_height, visible_height):
        self.rect = pygame.Rect(x, y, width, height)
        self.content_height = content_height
        self.visible_height = visible_height
        self.scroll_position = 0
        self.is_dragging = False
        self.scroll_height = min(height, height * (visible_height / content_height))
        self.scroll_rect = pygame.Rect(x, y, width, self.scroll_height)
        
    def update(self, content_height):
        self.content_height = content_height
        self.scroll_height = min(self.rect.height, self.rect.height * (self.visible_height / content_height))
        self.scroll_rect.height = self.scroll_height
        
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.scroll_rect.collidepoint(event.pos):
                self.is_dragging = True
            elif event.button == 4:  # 마우스 휠 위로
                self.scroll_position = max(0, self.scroll_position - 20)
            elif event.button == 5:  # 마우스 휠 아래로
                max_scroll = self.content_height - self.visible_height
                self.scroll_position = min(max_scroll, self.scroll_position + 20)
                
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.is_dragging = False
                
        elif event.type == pygame.MOUSEMOTION and self.is_dragging:
            rel_y = event.pos[1] - self.rect.y
            scroll_ratio = rel_y / self.rect.height
            self.scroll_position = (self.content_height - self.visible_height) * scroll_ratio
            self.scroll_position = max(0, min(self.scroll_position, 
                                            self.content_height - self.visible_height))
    
    def draw(self, surface):
        # 스크롤바 배경
        pygame.draw.rect(surface, GRAY, self.rect)
        
        # 스크롤 위치 계산
        if self.content_height > self.visible_height:
            scroll_ratio = self.scroll_position / (self.content_height - self.visible_height)
            scroll_y = self.rect.y + (self.rect.height - self.scroll_height) * scroll_ratio
            self.scroll_rect.y = scroll_y
            
        # 스크롤바 그리기
        pygame.draw.rect(surface, DARK_GRAY, self.scroll_rect)

class TextBox:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = []
        self.visible_lines = height // font.get_height()
        self.scroll_bar = ScrollBar(x + width - 20, y, 20, height, 
                                  0, self.visible_lines * font.get_height())
        self.active = False
        
    def add_text(self, text):
        self.text.append(text)
        content_height = len(self.text) * font.get_height()
        self.scroll_bar.update(content_height)
        
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False
                
        self.scroll_bar.handle_event(event)
        
    def draw(self, surface):
        # 텍스트박스 배경
        pygame.draw.rect(surface, WHITE, self.rect)
        pygame.draw.rect(surface, BLACK, self.rect, 2)
        
        # 텍스트 표시
        visible_start = int(self.scroll_bar.scroll_position / font.get_height())
        visible_end = visible_start + self.visible_lines
        
        for i, line in enumerate(self.text[visible_start:visible_end]):
            text_surface = font.render(line, True, BLACK)
            surface.blit(text_surface, (self.rect.x + 5, 
                                      self.rect.y + i * font.get_height()))
        
        # 스크롤바 그리기
        self.scroll_bar.draw(surface)

# 텍스트박스 생성
text_box = TextBox(50, 50, 300, 400)

# 샘플 텍스트 추가
for i in range(30):
    text_box.add_text(f"Line {i+1}: Sample text")

# 게임 루프
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(GRAY)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        text_box.handle_event(event)
    
    text_box.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()