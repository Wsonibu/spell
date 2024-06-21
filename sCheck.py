import tkinter as tk
from gtts import gTTS
import random
import os
import pygame

# Danh sách các từ vựng
nouns = ["dog", "cat", "book", "car", "tree", "apple", "child", "bus", "fox", "box"]

class NounCheckerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Noun Checker")
        
        # Tạo các widget
        self.label = tk.Label(root, text="Enter the word:")
        self.label.pack()
        
        self.entry = tk.Entry(root)
        self.entry.pack()
        
        self.create_button = tk.Button(root, text="Create and Read Noun", command=self.next_noun)
        self.create_button.pack()
        
        self.check_button = tk.Button(root, text="Check", command=self.check_noun)
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
            self.result_label.config(text="Correct!", fg="green")
        else:
            self.result_label.config(text=f"Wrong! The correct word is '{correct_noun}'", fg="red")
        
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = NounCheckerApp(root)
    root.mainloop()
