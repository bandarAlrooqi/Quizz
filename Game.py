from tkinter import *
import tkinter.font as tkFont
import tkinter as tk
import sqlite3

score = 0


def quize(root, choice, count):
    global score
    if count == 0:
        score = 0
    new = Toplevel(root)
    width = 800
    height = 500
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height,
                                (screenwidth - width) / 2, (screenheight - height) / 2)
    new.geometry(alignstr)
    new.resizable(False, False)
    new["bg"] = "white"
    if count == 5:
        R = tk.Label(new)
        ft = tkFont.Font(family='times new roman', size=24)
        R["font"] = ft
        R["fg"] = "#333333"
        R["bg"] = "white"
        R["justify"] = "center"
        R["text"] = f"Your result is {score} / 5"
        R.place(relx=0.5, rely=0.5, anchor="center")
        return
    conn = sqlite3.connect('Quizz.db')
    c = conn.cursor()
    c.execute(f"SELECT * FROM {choice}")
    result = c.fetchall()
    coorectAnswer = ""

    A = tk.Button(new)
    A["bg"] = "#efefef"
    ft = tkFont.Font(family='times new roman', size=14)
    A["font"] = ft
    A["fg"] = "#000000"
    A["justify"] = "center"
    A.place(relx=0.2, rely=0.7, width=400)
    A["command"] = lambda: answer(
        A['text'], coorectAnswer, root, new, choice, count)

    B = tk.Button(new)
    B["bg"] = "#b4c2d9"
    ft = tkFont.Font(family='times new roman', size=14)
    B["font"] = ft
    B["fg"] = "#000000"
    B["justify"] = "center"
    B.place(relx=0.2, rely=0.6, width=400)
    B["command"] = lambda: answer(
        B['text'], coorectAnswer, root, new, choice, count)

    C = tk.Button(new)
    C["bg"] = "#efefef"
    ft = tkFont.Font(family='times new roman', size=14)
    C["font"] = ft
    C["fg"] = "#000000"
    C["justify"] = "center"
    C.place(relx=0.2, rely=0.5, width=400)
    C["command"] = lambda: answer(
        C['text'], coorectAnswer, root, new, choice, count)

    D = tk.Button(new)
    D["bg"] = "#b4c2d9"
    ft = tkFont.Font(family='times new roman', size=14)
    D["font"] = ft
    D["fg"] = "#000000"
    D["justify"] = "center"
    D.place(relx=0.2, rely=0.4, width=400)
    D["command"] = lambda: answer(
        D['text'], coorectAnswer, root, new, choice, count)

    Q = tk.Label(new)
    ft = tkFont.Font(family='times new roman', size=16)
    Q["font"] = ft
    Q["bg"] = "white"
    Q["justify"] = "center"
    Q.place(relx=0.1, rely=0.1)
    coorectAnswer = loadQuestions(result, Q, A, B, C, D, count)


def loadQuestions(data, Q, A, B, C, D, count):
    Q["text"] = data[count][0]
    A["text"] = data[count][1]
    B["text"] = data[count][2]
    C["text"] = data[count][3]
    D["text"] = data[count][4]
    return data[count][5]


def answer(text, correct, root, win, choice, count):
    global score
    if text == correct:
        score += 1
    win.destroy()
    quize(root, choice, count+1)


class App:
    def __init__(self, root):
        # setting title
        root.title("Quiz Game")
        # setting window size
        width = 600
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root["bg"] = "white"
        scienceB = tk.Button(root)
        scienceB["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=14)
        scienceB["font"] = ft
        scienceB["fg"] = "#000000"
        scienceB["justify"] = "center"
        scienceB["text"] = "Science"
        scienceB.place(x=60, y=410, width=100, height=25)
        scienceB["command"] = lambda: quize(root, "science", 0)

        technologyB = tk.Button(root)
        technologyB["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=14)
        technologyB["font"] = ft
        technologyB["fg"] = "#000000"
        technologyB["justify"] = "center"
        technologyB["text"] = "Technology"
        technologyB.place(x=440, y=410, width=100, height=25)
        technologyB["command"] = lambda: quize(root, "technology", 0)

        historyB = tk.Button(root)
        historyB["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=14)
        historyB["font"] = ft
        historyB["fg"] = "#000000"
        historyB["justify"] = "center"
        historyB["text"] = "History"
        historyB.place(x=180, y=410, width=100, height=25)
        historyB["command"] = lambda: quize(root, "history", 0)

        geographyB = tk.Button(root)
        geographyB["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=14)
        geographyB["font"] = ft
        geographyB["fg"] = "#000000"
        geographyB["justify"] = "center"
        geographyB["text"] = "Geography"
        geographyB.place(x=310, y=410, width=100, height=25)
        geographyB["command"] = lambda: quize(root, "geography", 0)

        GLabel_638 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=16)
        GLabel_638["font"] = ft
        GLabel_638["fg"] = "#333333"
        GLabel_638["bg"] = "white"
        GLabel_638["justify"] = "center"
        GLabel_638["text"] = "Welcome to Today's Quiz!\nChoose your domain of interest:"
        GLabel_638.place(x=100, y=120, width=399, height=40)


root = tk.Tk()
app = App(root)
root.mainloop()
