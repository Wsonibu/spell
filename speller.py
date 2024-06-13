import os
import random
import string
import pygame
from gtts import gTTS
import tkinter as tk


def text_to_speech(text, lang='en', slow=False):
    tts = gTTS(text=text, lang=lang, slow=slow)
    filename = 'output.mp3'
    tts.save(filename)
    return filename


def play_sound(file):
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue
    pygame.mixer.quit()


def random_number():
    length = random.randint(2, 5)
    number = random.randint(10 ** (length - 1), 10 ** length - 1)
    return number


def speak_number():
    number = random_number()
    result_label.config(text=f"Số ngẫu nhiên: {number}")
    tts_file = text_to_speech(str(number), lang='en')
    play_sound(tts_file)
    os.remove(tts_file)


def random_word():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    length = random.randint(3, 8)
    word = ''.join(random.choice(letters) for _ in range(length))
    return word


def speak_word():
    word = random_word()
    result_label.config(text=f"Chữ ngẫu nhiên: {word}")

    # Đọc từng chữ cái một
    for letter in word:
        tts_file = text_to_speech(letter, lang='en')
        play_sound(tts_file)
        os.remove(tts_file)


def read_code():
    # Tạo mã lẫn lộn gồm chữ số và chữ cái, tối đa 8 ký tự
    code = ''.join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(6, 10)))
    result_label.config(text=f"Mã lẫn lộn: {code}")

    # Phát âm từng ký tự trong mã
    for char in code:
        tts_file = text_to_speech(char, lang='en')
        play_sound(tts_file)
        os.remove(tts_file)


# Tạo giao diện người dùng
root = tk.Tk()
root.title("Speller")

frame = tk.Frame(root)
frame.pack(pady=20)

number_button = tk.Button(frame, text="Đọc số", command=speak_number, font=("Helvetica", 14), width=20)
number_button.pack(pady=5)

word_button = tk.Button(frame, text="Đọc chữ", command=speak_word, font=("Helvetica", 14), width=20)
word_button.pack(pady=5)

code_button = tk.Button(frame, text="Đọc mã lẫn lộn", command=read_code, font=("Helvetica", 14), width=20)
code_button.pack(pady=5)
result_label = tk.Label(frame, text="", font=("Helvetica", 16))
result_label.pack(pady=10)
exit_button = tk.Button(frame, text="Thoát", command=root.quit, font=("Helvetica", 14), width=20)
exit_button.pack(pady=5)
root.mainloop()
