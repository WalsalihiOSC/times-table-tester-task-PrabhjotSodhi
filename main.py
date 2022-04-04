import tkinter as tk

class TimesTableGUI:
    def __init__(self, frame):
        self.frame = frame
        self.display()
    def display(self):
        question = tk.Label(self.frame, text="9 * 3")
        question.grid()
        answer = tk.Entry(self.frame)
        answer.grid(column=1, row=0)
        check_answer_box = tk.Button(self.frame, text="Check Answer")
        check_answer_box.grid(row=1, column=0)
        next_question_box = tk.Button(self.frame, text="Next Question")
        next_question_box.grid(row=1, column=1)

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('250x100')
    root.title("Times Table Task")
    main_frame = tk.Frame(root)
    main_frame.pack()
    TimesTableGUI(main_frame)
    root.mainloop()