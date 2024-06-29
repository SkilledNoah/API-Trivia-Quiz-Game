from tkinter import *
from tkinter import ttk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class OptionsInterface:

    def __init__(self):

        self.window = Tk()
        self.window.title("Quiz Trivia")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=200, height=150, bg="gray12", highlightthickness=0)
        logo_img = PhotoImage(file="quiz_img.png.png")
        self.canvas.create_image(100, 75, image=logo_img)
        self.canvas.grid(column=0, row=0, columnspan=2)

        self.text_label = Label(text="Select the quiz settings: ", bg=THEME_COLOR, fg="white")
        self.text_label.config(pady=5, padx=5)
        self.text_label.grid(row=1, column=0)

        self.questions = Entry()
        self.questions.grid(row=2, column=1, pady=5, padx=5)
        self.questions.config(width=53)
        self.questions.focus()
        self.question_label = Label(text="Number of questions", bg=THEME_COLOR, fg="white")
        self.question_label.grid(row=2, column=0)

        self.category = ttk.Combobox(self.window, width=50)
        self.category['values'] = (
            "Any Category",
            "General Knowledge",
            "Entertainment: Books",
            "Entertainment: Film")

        self.category.grid(row=3, column=1, pady=5)
        self.category.current(0)
        self.category_label = Label(text="Select Category", bg=THEME_COLOR, fg="white")
        self.category_label.grid(row=3, column=0)

        self.difficulty = ttk.Combobox(self.window, width=50)
        self.difficulty['values'] = ("Any Difficulty", "easy", "medium", "hard")
        self.difficulty.grid(row=4, column=1, pady=5)
        self.difficulty.current(0)
        self.difficulty_label = Label(text="Select difficulty", bg=THEME_COLOR, fg="white")
        self.difficulty_label.grid(row=4, column=0)

        self.save_button = Button(text="Save Settings", command=self.save_settings)
        self.save_button.grid(row=5, column=0, columnspan=2)

        self.next_ui_flag = False
        self.get_difficulty = ""
        self.get_number = 10
        self.get_category = ""

        self.window.mainloop()

    def save_settings(self):
        self.save_choices()

        self.next_ui_flag = True
        self.window.destroy()

    def next_ui(self):
        return self.next_ui_flag

    def save_choices(self):
        self.get_difficulty = self.difficulty.get()
        self.get_number = self.questions.get()
        self.get_category = self.category.get()


