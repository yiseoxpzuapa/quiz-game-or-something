import tkinter as tk
from tkinter import messagebox

quizd = [
    {
    "question": "i bought a property in egypt, then what they do for you is",
    "choices": ["dont give you the property", "gift you", "they give you the property", "AAAA"],
    "answer": "they give you the property"
    },

    {
    "question": "besting: bring me",
    "choices": ["8 year olds", "12 year olds", "14 year olds", "food"],
    "answer": "12 year olds"
    },

    {
    "question": "those who:",
    "choices": ["know", "dont know", "have fun and likes to play games", "hate fun and doesn't like to play games"],
    "answer": "know"
    },

    {
    "question": "leaked mym song?",
    "choices": ["idontcareifhes.ogg", "sak your diaz", "obey your ohiovine", "cleanse your cursie"],
    "answer": "idontcareifhes.ogg"
    },

    {
    "question": " guesss I dont know vrrrrrrfvggggggggggggggggggggggggggggg",
    "choices": ["1", "2", "3", "4"],
    "answer": "4"
    }
]

def checkanswer(selected_choice):
    global currentqu, score
    if selected_choice == quizd[currentqu]["answer"]:
        score += 1

    currentqu += 1
    if currentqu < len(quizd):
        updatequ()
    else:
        showfisc()

def updatequ():
    questionlab.config(text=quizd[currentqu]["question"])
    for i, choice in enumerate(quizd[currentqu]["choices"]):
        buttons[i].config(text=choice, command=lambda c=choice: checkanswer(c))

def showfisc():
    messagebox.showinfo("oh my god just end it all", f"you scored {score} out of {len(quizd)}")
    root.quit()
    
root = tk.Tk()
root.title("Quiz")

currentqu = 0
score = 0

questionlab = tk.Label(root, text=quizd[currentqu]["question"], font=("Arial", 14))
questionlab.pack(pady=20)

buttons = []
for i in range(4):
    btn = tk.Button(root, text="", font=("Arial", 14))
    btn.pack(pady=5, fill=tk.X)
    buttons.append(btn)

updatequ()

root.mainloop()