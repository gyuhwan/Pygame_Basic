import random
import tkinter as tk
from tkinter import ttk


def generate_lotto():
    # 로또 번호를 저장할 리스트 생성
    lotto_numbers = []
    # 1부터 45까지의 숫자 중에서 6개를 무작위로 선택
    while len(lotto_numbers) < 6:
        number = random.randint(1, 45)
        if number not in lotto_numbers:
            lotto_numbers.append(number)
    # 번호를 오름차순으로 정렬
    lotto_numbers.sort()
    # 결과 레이블 업데이트
    result_label.config(text="추천 번호: " + ", ".join(map(str, lotto_numbers)))


def copy_numbers():
    current_numbers = result_label.cget("text")
    if "추천 번호:" in current_numbers:
        # 클립보드에 복사
        window.clipboard_clear()
        window.clipboard_append(current_numbers.split(": ")[1])
        # 복사 완료 메시지 표시
        copy_status_label.config(text="번호가 클립보드에 복사되었습니다!")
    else:
        copy_status_label.config(text="복사할 번호가 없습니다.")


# GUI 윈도우 생성
window = tk.Tk()
window.title("로또 번호 생성기")
window.geometry("300x150")

# 스타일 설정
style = ttk.Style()
style.configure("TButton", padding=10, font=('맑은 고딕', 10))
style.configure("TLabel", font=('맑은 고딕', 12))

# 버튼 생성
generate_button = ttk.Button(window, text="번호 생성하기", command=generate_lotto)
generate_button.pack(pady=20)
# 복사 버튼 생성
copy_button = ttk.Button(window, text="번호 복사하기", command=copy_numbers)
copy_button.pack(pady=10)

# 결과를 표시할 레이블
result_label = ttk.Label(window, text="버튼을 클릭하여 번호를 생성하세요")
result_label.pack(pady=20)


# GUI 실행
window.mainloop()

# 창 크기 조정
window.geometry("300x250")

# 복사 상태를 표시할 레이블
copy_status_label = ttk.Label(window, text="")
copy_status_label.pack(pady=5)
