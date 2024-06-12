import random
import pyttsx3
import tkinter as tk

# Khởi tạo engine pyttsx3
engine = pyttsx3.init()

# Điều chỉnh tốc độ nói (tăng tốc độ)
engine.setProperty('rate', 250)  # Giá trị mặc định thường là 200, tăng lên 250

def random_number():
    # Sinh ngẫu nhiên độ dài của số từ 2-5 chữ số
    length = random.randint(2, 5)
    # Sinh số ngẫu nhiên với độ dài xác định
    number = random.randint(10**(length-1), 10**length - 1)
    return number

def speak_number():
    number = random_number()
    result_label.config(text=f"Số ngẫu nhiên: {number}")
    engine.say(str(number))
    engine.runAndWait()

def random_word():
    # Danh sách các chữ cái tiếng Anh
    letters = 'abcdefghijklmnopqrstuvwxyz'
    # Sinh ngẫu nhiên độ dài của chữ từ 3-8 chữ cái
    length = random.randint(3, 8)
    # Sinh chữ ngẫu nhiên
    word = ''.join(random.choice(letters) for _ in range(length))
    return word

def speak_word():
    word = random_word()
    result_label.config(text=f"Chữ ngẫu nhiên: {word}")
    for letter in word:
        engine.say(letter)
    engine.runAndWait()

# Tạo giao diện người dùng
root = tk.Tk()
root.title("Speller IETLS")

frame = tk.Frame(root)
frame.pack(pady=20)

label = tk.Label(frame, text="Chọn chức năng:", font=("Helvetica", 16))
label.pack(pady=10)

number_button = tk.Button(frame, text="Đọc số", command=speak_number, font=("Helvetica", 14), width=20)
number_button.pack(pady=5)

word_button = tk.Button(frame, text="Đọc chữ", command=speak_word, font=("Helvetica", 14), width=20)
word_button.pack(pady=5)

result_label = tk.Label(frame, text="", font=("Helvetica", 16))
result_label.pack(pady=10)

exit_button = tk.Button(frame, text="Thoát", command=root.quit, font=("Helvetica", 14), width=20)
exit_button.pack(pady=5)

root.mainloop()
