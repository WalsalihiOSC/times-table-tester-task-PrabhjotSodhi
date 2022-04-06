import random
import tkinter as tk

class TimesTableGUI:
    def __init__(self):
        main_frame = tk.Frame(root)
        main_frame.pack()
        self.backend = TimeTableClass()
        self.answer_var = tk.IntVar()

        self.question_label = tk.Label(main_frame, text=self.backend.create_question()[2])
        self.question_label.grid()

        self.answer = tk.Entry(main_frame, textvariable=self.answer_var)
        self.answer.grid(column=1, row=0)

        check_answer_box = tk.Button(main_frame, text="Check Answer", command=self.configure_label)
        check_answer_box.grid(row=1, column=0)

        next_question_box = tk.Button(main_frame, text="Next Question", command=self.next)
        next_question_box.grid(row=1, column=1)

        check_label = tk.Label(main_frame, text="")
        check_label.grid(row=2, column=0)

        self.answer_label = tk.Label(main_frame, text="")
        self.answer_label.grid(row=3, column=0)

    def configure_label(self):
        bool_a = self.backend.check_answer(self.answer_var)
        if bool_a == 1:
            self.answer_label.configure(text="Correct")
        elif bool_a == 0:
            self.answer_label.configure(text=f"Incorrect the answer is {self.backend.get_answer()}")
        else:
            self.answer_label.configure(text="")
    
    def next(self):
        self.question_label.configure(text=self.backend.create_question()[2])
        self.answer.delete(0, tk.END)

class TimeTableClass:
    def __init__(self):
        pass
    def check_answer(self, input):
        if int(input.get()) == self.answer:
            return 1
        else:
            return 0

    def create_question(self):
        self.number_1 = random.randint(1,10)
        self.number_2 = random.randint(1,10)
        self.answer = self.number_1 * self.number_2
        question = f"{self.number_1} * {self.number_2}"
        return (self.number_1, self.number_2, question)
    def get_answer(self):
        return self.answer

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('250x100')
    root.title("Times Table Task")
    TimesTableGUI()
    root.mainloop()