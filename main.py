import random
import tkinter as tk

class TimesTableGUI:
    def __init__(self):
        main_frame = tk.Frame(root)
        main_frame.pack()
        self.backend = TimeTableClass()
        question_label = tk.Label(main_frame, text=self.backend.create_question()[2])
        question_label.grid()
        answer = tk.Entry(main_frame)
        answer.grid(column=1, row=0)
        check_answer_box = tk.Button(main_frame, text="Check Answer", command=lambda: self.backend.check_answer(answer))
        check_answer_box.grid(row=1, column=0)
        next_question_box = tk.Button(main_frame, text="Next Question")
        next_question_box.grid(row=1, column=1)
        check_label = tk.Label(main_frame, text="")
        check_label.grid(row=2, column=0)

class TimeTableClass:
    def __init__(self):
        pass
    def check_answer(self, input):
        if input.get() == self.answer:
            return "Correct"
        else:
            return f"Incorrect the answer is {self.answer}"

    def create_question(self):
        self.number_1 = random.randint(1,10)
        self.number_2 = random.randint(1,10)
        self.answer = self.number_1 * self.number_2
        question = f"{self.number_1} * {self.number_2}"
        return (self.number_1, self.number_2, question)

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('250x100')
    root.title("Times Table Task")
    TimesTableGUI()
    root.mainloop()