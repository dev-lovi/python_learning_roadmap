import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from random import shuffle
from ttkthemes import ThemedStyle

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flashcards")
        
        # Aplicar el tema "Yaru"
        style = ThemedStyle(root)
        style.set_theme("yaru")
        
        # Barajar las tarjetas
        self.flashcards = [
            {"question": "¿Cuál es la capital de Francia?", "answer": "París"},
            {"question": "¿Cuál es el símbolo químico del oxígeno?", "answer": "O"},
            {"question": "¿En qué año se descubrió América?", "answer": "1492"},
            # Agrega más tarjetas aquí
        ]
        shuffle(self.flashcards)
        
        self.total_questions = len(self.flashcards)
        self.correct_answers = 0
        
        # Configuración de la interfaz
        self.question_label = ttk.Label(root, text="", font=("Arial", 14), wraplength=300)
        self.question_label.pack(pady=20)
        
        self.answer_label = ttk.Label(root, text="", font=("Arial", 12), foreground="green")
        self.answer_label.pack(pady=10)
        
        self.show_answer_button = ttk.Button(root, text="Mostrar Respuesta", command=self.show_answer)
        self.show_answer_button.pack(pady=10)
        
        self.next_card_button = ttk.Button(root, text="Siguiente Tarjeta", command=self.next_card)
        self.next_card_button.pack(pady=10)
        
        self.score_label = ttk.Label(root, text="", font=("Arial", 12))
        self.score_label.pack(pady=10)
        
        self.index = 0
        self.show_next_card()
        
    def show_next_card(self):
        if self.index < len(self.flashcards):
            self.question_label.config(text=self.flashcards[self.index]["question"])
            self.answer_label.config(text="")
        else:
            # Calcular la puntuación como un porcentaje
            percentage_score = (self.correct_answers / self.total_questions) * 100
            self.score_label.config(text=f"Puntuación: {percentage_score:.2f}%")
        
    def show_answer(self):
        if self.index < len(self.flashcards):
            self.answer_label.config(text=self.flashcards[self.index]["answer"])
            user_answer = messagebox.askquestion("Evaluación", "¿Acertaste la respuesta?")
            if user_answer == "yes":
                self.correct_answers += 1
        self.next_card()
        
    def next_card(self):
        self.index += 1
        self.show_next_card()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x500")  # Tamaño para pantalla de dispositivo móvil
    app = FlashcardApp(root)
    root.mainloop()
