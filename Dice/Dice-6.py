import random
import tkinter
currentNum = 1
numfont = ['Atkinson Hyperlegible', 50]
textfont = ['Atkinson Hyperlegible', 40]

class Dice():
    def __init__(self):
        self.window = tkinter.Tk(screenName='Dice')
        self.frame = tkinter.Frame(self.window, bg='Black', height=200, width=200)
        self.frame.pack_propagate(False)
        self.frame.pack()

    def createNumDisplay(self):
        global currentNum
        global font
        self.box = tkinter.Label(master=self.frame, text=currentNum, anchor='center', bg='Grey', font=numfont, height=1, width=2)
        self.box.pack(anchor='center')
    
    def createRollButton(self):
        global font
        self.button = tkinter.Button(master=self.frame, text='Roll', anchor='s', bg='grey', font=textfont, command=self.rollLogic, height=1, width=5)
        self.button.pack(anchor='s', side=tkinter.BOTTOM)
    
    def rollLogic(self):
        global currentNum
        newNum = random.randint(1, 6)
        self.box.config(text=newNum)
        self.box.update()
        self.box.update_idletasks()

def Run():
    wd = Dice()
    wd.createNumDisplay()
    wd.createRollButton()
    wd.window.mainloop()

if __name__ == '__main__':
    Run()