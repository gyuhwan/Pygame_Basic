import tkinter as tk
from tkinter import ttk
import random
from datetime import datetime

class PowerballViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Powerball Number Viewer")
        
        # 메인 프레임
        self.main_frame = ttk.Frame(root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.E, tk.W))
        
        # 왼쪽 프레임 (번호 표시)
        self.left_frame = ttk.LabelFrame(self.main_frame, text="Generated Numbers", padding="5")
        self.left_frame.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.E, tk.W), padx=(0, 5))
        
        # 오른쪽 프레임 (히스토리)
        self.right_frame = ttk.LabelFrame(self.main_frame, text="Number History", padding="5")
        self.right_frame.grid(row=0, column=1, sticky=(tk.N, tk.S, tk.E, tk.W), padx=(5, 0))
        
        # 번호 표시 레이블들
        self.number_labels = []
        for i in range(5):
            label = ttk.Label(
                self.left_frame,
                text="--",
                width=3,
                style='Number.TLabel',
                background='white',
                relief='solid'
            )
            label.grid(row=0, column=i, padx=5, pady=10)
            self.number_labels.append(label)
        
        # Powerball 번호 레이블
        self.powerball_label = ttk.Label(
            self.left_frame,
            text="--",
            width=3,
            style='Powerball.TLabel',
            background='red',
            foreground='white',
            relief='solid'
        )
        self.powerball_label.grid(row=0, column=5, padx=5, pady=10)
        
        # 생성 버튼
        self.generate_button = ttk.Button(
            self.left_frame,
            text="Generate Numbers",
            command=self.generate_numbers
        )
        self.generate_button.grid(row=1, column=0, columnspan=6, pady=10)
        
        # 히스토리 텍스트 영역
        self.history_text = tk.Text(
            self.right_frame,
            wrap=tk.WORD,
            width=40,
            height=20
        )
        self.history_scroll = ttk.Scrollbar(
            self.right_frame,
            orient=tk.VERTICAL,
            command=self.history_text.yview
        )
        
        # 스크롤바 연결
        self.history_text.configure(yscrollcommand=self.history_scroll.set)
        
        # 히스토리 위젯 배치
        self.history_text.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.E, tk.W))
        self.history_scroll.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        # 그리드 가중치 설정
        self.main_frame.columnconfigure(1, weight=1)
        self.main_frame.rowconfigure(0, weight=1)
        self.right_frame.columnconfigure(0, weight=1)
        self.right_frame.rowconfigure(0, weight=1)
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        
        # 스타일 설정
        self.setup_styles()
        
    def setup_styles(self):
        style = ttk.Style()
        style.configure('Number.TLabel', font=('Arial', 14, 'bold'), anchor='center')
        style.configure('Powerball.TLabel', font=('Arial', 14, 'bold'), anchor='center')
        
    def generate_numbers(self):
        # 흰 공 번호 생성 (1-69, 중복 없이 5개)
        white_balls = sorted(random.sample(range(1, 70), 5))
        
        # Powerball 번호 생성 (1-26)
        powerball = random.randint(1, 26)
        
        # 레이블 업데이트
        for i, num in enumerate(white_balls):
            self.number_labels[i].configure(text=f"{num:02d}")
        
        self.powerball_label.configure(text=f"{powerball:02d}")
        
        # 히스토리에 추가
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        numbers_str = " ".join(f"{num:02d}" for num in white_balls)
        history_entry = f"[{timestamp}]\n{numbers_str} | {powerball:02d}\n\n"
        self.history_text.insert("1.0", history_entry)

def main():
    root = tk.Tk()
    app = PowerballViewer(root)
    
    # 테마 설정
    try:
        style = ttk.Style()
        style.theme_use('clam')
    except:
        pass
    
    root.mainloop()

if __name__ == "__main__":
    main()