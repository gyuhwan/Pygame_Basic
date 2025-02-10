import pygame
import math

# 초기화
pygame.init()

# 화면 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("공학용 계산기")

# 색상 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
DARK_GRAY = (100, 100, 100)
BLUE = (100, 100, 255)

# 폰트 설정
font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 28)

class Calculator:
    def __init__(self):
        self.memory = 0
        self.current_expression = ""
        self.result = ""
        self.show_result = False
    
    def calculate(self, expression):
        try:
            # 특수 함수 처리
            expression = expression.replace('sin(', 'math.sin(')
            expression = expression.replace('cos(', 'math.cos(')
            expression = expression.replace('tan(', 'math.tan(')
            expression = expression.replace('log(', 'math.log10(')
            expression = expression.replace('ln(', 'math.log(')
            expression = expression.replace('π', str(math.pi))
            expression = expression.replace('e', str(math.e))
            expression = expression.replace('√(', 'math.sqrt(')
            
            result = eval(expression)
            return str(result)
        except:
            return "Error"
    
    def memory_add(self):
        try:
            if self.show_result:
                self.memory += float(self.result)
            else:
                self.memory += float(self.calculate(self.current_expression))
            return "M+ " + str(self.memory)
        except:
            return "Error"
    
    def memory_subtract(self):
        try:
            if self.show_result:
                self.memory -= float(self.result)
            else:
                self.memory -= float(self.calculate(self.current_expression))
            return "M- " + str(self.memory)
        except:
            return "Error"
    
    def memory_recall(self):
        return str(self.memory)
    
    def memory_clear(self):
        self.memory = 0
        return "Memory Cleared"

class Button:
    def __init__(self, x, y, width, height, text, color, small_text=False):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.is_hovered = False
        self.small_text = small_text

    def draw(self, surface):
        pygame.draw.rect(surface, self.color if not self.is_hovered else DARK_GRAY, self.rect)
        pygame.draw.rect(surface, BLACK, self.rect, 2)
        text_font = small_font if self.small_text else font
        text_surface = text_font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

# 버튼 생성
buttons = []
button_texts = [
    ['sin', 'cos', 'tan', 'M+', 'M-'],
    ['log', 'ln', '√', 'MR', 'MC'],
    ['(', ')', 'π', 'e', 'C'],
    ['7', '8', '9', '/', 'DEL'],
    ['4', '5', '6', '*', '**'],
    ['1', '2', '3', '-', '1/x'],
    ['0', '.', '±', '+', '=']
]

# 버튼 위치 설정
button_width = 80
button_height = 60
margin = 10
x_start = 10
y_start = 150

# 버튼 생성
for row_idx, row in enumerate(button_texts):
    for col_idx, text in enumerate(row):
        x = x_start + col_idx * (button_width + margin)
        y = y_start + row_idx * (button_height + margin)
        color = BLUE if text in ['sin', 'cos', 'tan', 'log', 'ln', '√'] else GRAY
        small = len(text) > 2
        buttons.append(Button(x, y, button_width, button_height, text, color, small))

# 계산기 인스턴스 생성
calc = Calculator()

# 게임 루프
running = True
while running:
    screen.fill(WHITE)
    
    # 결과창 그리기
    result_rect = pygame.Rect(10, 50, screen_width - 20, 70)
    pygame.draw.rect(screen, WHITE, result_rect)
    pygame.draw.rect(screen, BLACK, result_rect, 2)
    
    # 현재 수식 또는 결과 표시
    display_text = calc.result if calc.show_result else calc.current_expression
    if not display_text:
        display_text = "0"
    text_surface = font.render(display_text, True, BLACK)
    text_rect = text_surface.get_rect(midright=(result_rect.right - 10, result_rect.centery))
    screen.blit(text_surface, text_rect)

    # 메모리 표시
    if calc.memory != 0:
        memory_text = font.render("M", True, BLACK)
        screen.blit(memory_text, (result_rect.left + 10, result_rect.centery - 15))

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for button in buttons:
                if button.rect.collidepoint(mouse_pos):
                    if button.text == '=':
                        calc.result = calc.calculate(calc.current_expression)
                        calc.show_result = True
                    elif button.text == 'C':
                        calc.current_expression = ""
                        calc.result = ""
                        calc.show_result = False
                    elif button.text == 'DEL':
                        calc.current_expression = calc.current_expression[:-1]
                        calc.show_result = False
                    elif button.text == 'M+':
                        calc.memory_add()
                    elif button.text == 'M-':
                        calc.memory_subtract()
                    elif button.text == 'MR':
                        calc.current_expression = calc.memory_recall()
                    elif button.text == 'MC':
                        calc.memory_clear()
                    elif button.text == '±':
                        if calc.current_expression and calc.current_expression[0] == '-':
                            calc.current_expression = calc.current_expression[1:]
                        else:
                            calc.current_expression = '-' + calc.current_expression
                    elif button.text == '1/x':
                        if calc.show_result:
                            calc.current_expression = f"1/({calc.result})"
                        else:
                            calc.current_expression = f"1/({calc.current_expression})"
                        calc.show_result = False
                    else:
                        if calc.show_result:
                            calc.current_expression = ""
                            calc.show_result = False
                        calc.current_expression += button.text

        # 마우스 호버 효과
        mouse_pos = pygame.mouse.get_pos()
        for button in buttons:
            button.is_hovered = button.rect.collidepoint(mouse_pos)

    # 버튼 그리기
    for button in buttons:
        button.draw(screen)

    pygame.display.flip()

pygame.quit()