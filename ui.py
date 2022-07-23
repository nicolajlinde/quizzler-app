from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, background=THEME_COLOR)

        self.score = Label(text="Score: 0", background=THEME_COLOR, anchor="center", foreground="white")
        self.score.grid(row=0, column=1, pady=20)

        self.canvas = Canvas(width=300, height=250, background="white")
        self.canvas.grid(row=1, column=0, columnspan=2)
        self.question_text = self.canvas.create_text(
            150,
            125,
            text=f"lol",
            font=("Arial", 20, "italic"),
            width=280)

        # --- Yes button --- #
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, border=0, command=self.question_true)
        self.true_button.grid(row=2, column=0, pady=50)

        # --- False button --- #
        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, border=0, command=self.question_false)
        self.false_button.grid(row=2, column=1, pady=50)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfigure(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def question_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def question_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def change_color(self, color: str):
        self.canvas.configure(bg=color)

    def give_feedback(self, is_right: bool):
        if is_right:
            self.change_color("green")
        else:
            self.change_color("red")

        self.window.after(1000, func=self.get_next_question)







