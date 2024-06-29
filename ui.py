from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain, difficulty, category, number):
        self.number_of_questions = number
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz Trivia")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=10, highlightbackground="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="some question",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_img = PhotoImage(file="true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.true_pressed, bd=0)
        self.true_button.grid(column=0, row=2)

        false_img = PhotoImage(file="false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_pressed, bd=0)
        self.false_button.grid(column=1, row=2)

        self.score_label = Label(text=f"Score: 0/{self.number_of_questions}", fg="white", bg=THEME_COLOR, font=("Arial", 25, "bold"))
        self.score_label.grid(column=0, row=0, columnspan=2)

        # self. is used to turn into a property so that
        # it can be accessed anywhere in the class
        # false_img does not need to be accessed again so no self.

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(highlightbackground="white")
        if self.quiz.still_has_questions():
            self.reactivate_buttons()
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.config(highlightbackground="white")
            self.disable_buttons()
            self.canvas.itemconfig(self.question_text, text="End of game")

    def true_pressed(self):
        user_answer = "True"
        is_right = self.quiz.check_answer(user_answer)
        if is_right:
            score = self.quiz.score
            self.score_label.config(text=f"Score: {score}/{self.number_of_questions}")
            self.canvas.config(highlightthickness=10, highlightbackground="green")
        else:
            self.canvas.config(highlightthickness=10, highlightbackground="red")
        self.disable_buttons()
        self.window.after(1000, self.get_next_question)

    def false_pressed(self):
        user_answer = "False"
        is_right = self.quiz.check_answer(user_answer)
        if is_right:
            score = self.quiz.score
            self.score_label.config(text=f"Score: {score}/{self.number_of_questions}")
            self.canvas.config(highlightthickness=10, highlightbackground="green")
        else:
            self.canvas.config(highlightthickness=10, highlightbackground="red")
        self.disable_buttons()
        self.window.after(1000, self.get_next_question)

    def disable_buttons(self):
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")

    def reactivate_buttons(self):
        self.true_button.config(state="normal")
        self.false_button.config(state="normal")
