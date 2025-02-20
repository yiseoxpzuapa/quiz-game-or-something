import tkinter as tk
import sys
import os

class MainWindow(tk.Frame):
    def __init__(self, root=None, **kwargs):
        super().__init__(root, **kwargs)

        self.options_toplevel = None

        tk.Label(self, text="uhh fun quiz or. whatever").pack(pady=20)

        tk.Button(self, text='Enter', command=self.enter).pack()
        tk.Button(self, text='skip a stage in the quiz', command=self.idiot1).pack()
        tk.Button(self, text='About', command=self.about).pack()

        tk.Label(self, text="sylvia :-)").pack(pady=5)

    def enter(self):
        os.system('quiz.py')

    def about(self):
        os.system('about.py')

    def idiot1(self):
        os.system('idiot.py')   


root = tk.Tk()
root.title(" ")
gui = MainWindow(root)
gui.pack(pady=20, padx=20)
root.mainloop()