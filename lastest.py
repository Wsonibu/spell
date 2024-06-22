import tkinter as tk
import os
import random
import string
import pygame
from gtts import gTTS


class SpellerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Speller")
        self.root.geometry("500x500")
        self.root.configure(bg='mintcream')
        self.frame = tk.Frame(root, bg='mintcream')
        self.frame.pack(pady=20)

        self.number_button = tk.Button(self.frame, text="Đọc số", command=self.speak_number, font=("Helvetica", 14),
                                       width=20,bg='aqua')
        self.number_button.pack(pady=5)

        self.word_button = tk.Button(self.frame, text="Đọc chữ", command=self.speak_word, font=("Helvetica", 14),
                                     width=20,bg='aquamarine')
        self.word_button.pack(pady=5)

        self.code_button = tk.Button(self.frame, text="Đọc mã lẫn lộn", command=self.read_code, font=("Helvetica", 14),
                                     width=20,bg='ivory')
        self.code_button.pack(pady=5)

        self.result_label = tk.Label(self.frame, text="", font=("Helvetica", 16),bg='mintcream')
        self.result_label.pack(pady=10)

        self.exit_button = tk.Button(self.frame, text="Thoát", command=root.quit, font=("Helvetica", 14), width=20,bg='lavender')
        self.exit_button.pack(pady=5)

    def text_to_speech(self, text, lang='en', slow=False):
        tts = gTTS(text=text, lang=lang, slow=slow)
        filename = 'output.mp3'
        tts.save(filename)
        return filename

    def play_sound(self, file):
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue
        pygame.mixer.quit()

    def random_number(self):
        length = random.randint(2, 5)
        number = random.randint(10 ** (length - 1), 10 ** length - 1)
        return number

    def speak_number(self):
        number = self.random_number()
        self.result_label.config(text=f"Số ngẫu nhiên: {number}")
        tts_file = self.text_to_speech(str(number), lang='en')
        self.play_sound(tts_file)
        os.remove(tts_file)

    def random_word(self):
        letters = 'abcdefghijklmnopqrstuvwxyz'
        length = random.randint(3, 8)
        word = ''.join(random.choice(letters) for _ in range(length))
        return word

    def speak_word(self):
        word = self.random_word()
        self.result_label.config(text=f"Chữ ngẫu nhiên: {word}")

        for letter in word:
            tts_file = self.text_to_speech(letter, lang='en')
            self.play_sound(tts_file)
            os.remove(tts_file)

    def read_code(self):
        code = ''.join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(6, 10)))
        self.result_label.config(text=f"Mã lẫn lộn: {code}")

        for char in code:
            tts_file = self.text_to_speech(char, lang='en')
            self.play_sound(tts_file)
            os.remove(tts_file)

nouns = ["dog", "cat", "book", "car", "tree", "apple", "child", "bus", "fox", "box","people","children",'rock','house','box','roof','chef','belief','student','rose','thing']
class NounCheckerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SPELLER MAX")

        self.frame = tk.Frame(root)
        self.frame.pack(pady=20)
        # Tạo các widget
        self.label = tk.Label(root, text="Enter the word:",bg='azure')
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.create_button = tk.Button(root, text="Create", command=self.next_noun,bg='lavenderblush')
        self.create_button.pack()

        self.check_button = tk.Button(root, text="Check", command=self.check_noun,bg='snow')
        self.check_button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

        pygame.mixer.init()
        self.current_noun = None

    def next_noun(self):
        self.current_noun = random.choice(nouns)
        self.singular = random.choice([True, False])
        self.read_noun()

    def read_noun(self):
        if not self.current_noun:
            return
        text = self.current_noun if self.singular else self.current_noun + "s"
        if not os.path.exists(f"{text}.mp3"):
            tts = gTTS(text)
            tts.save(f"{text}.mp3")
        pygame.mixer.music.load(f"{text}.mp3")
        pygame.mixer.music.play()

    def check_noun(self):
        user_input = self.entry.get().strip().lower()
        correct_noun = self.current_noun if self.singular else self.current_noun + "s"

        if user_input == correct_noun:
            self.result_label.config(text="Correct!", fg="green",bg='mintcream')
        else:
            self.result_label.config(text=f"Wrong! The correct word is '{correct_noun}'", fg="red",bg='mintcream')

        self.entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    speller_app = SpellerApp(root)
    noun_checker_app = NounCheckerApp(root)
    root.mainloop()
