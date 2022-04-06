import random
import tkinter as tk

class TimesTableGUI:
    def __init__(self, frame):
        self.frame = frame
        self.backend = TimeTableClass()
        
        question = tk.Label(self.frame, text=self.backend.create_question()[2])
        question.grid()
        answer = tk.Entry(self.frame)
        answer.grid(column=1, row=0)
        check_answer_box = tk.Button(self.frame, text="Check Answer", command=lambda: self.backend.check_answer(question))
        check_answer_box.grid(row=1, column=0)
        next_question_box = tk.Button(self.frame, text="Next Question")
        next_question_box.grid(row=1, column=1)
        check_label = tk.Label(self.frame, text="")
        check_label.grid(row=2, column=0)

class TimeTableClass:
    def __init__(self):
        pass
    def check_answer(self, input):
        input = input.get()

    def create_question(self):
        number_1 = random.randint(1,10)
        number_2 = random.randint(1,10)
        question = f"{number_1} * {number_2}"
        return (number_1, number_2, question)



if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('250x100')
    root.title("Times Table Task")
    main_frame = tk.Frame(root)
    main_frame.pack()
    TimesTableGUI(main_frame)
    root.mainloop()