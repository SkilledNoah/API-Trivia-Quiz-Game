"""
---------------------------------------
    * Course: 100 Days of Code - Dra. Angela Yu
    * Author: Noah Louvet
    * Day: 34
    * Subject: Quiz Game - API - Tkinter
---------------------------------------
"""

from tkinter import messagebox

from question_model import Question
from data import Data
from quiz_brain import QuizBrain
from options import OptionsInterface
from ui import QuizInterface


quiz_options = OptionsInterface()

difficulty = quiz_options.get_difficulty
category = quiz_options.get_category
number = quiz_options.get_number

data = Data(category, difficulty, number)

question_bank = []
for question in data.question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

if quiz_options.next_ui_flag:
    quiz_ui = QuizInterface(quiz, difficulty, category, number)

# -------------------------------------------------------#
# More features:
# -DONE - possibility to choose quiz questions options (number, category, difficulty)
# -DONE - fix any difficulty error
# -when not enough questions: use try and warning box, retry if error (send user back to settings page)
# -restart new game

# -------------------------------------------------------#
