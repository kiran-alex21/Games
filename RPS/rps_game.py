import tkinter as tk
import random as ran
from PIL import Image, ImageTk
import os

##CONSTANTS
WIDTH: int = 275
HEIGHT: int = 300
LABELWIDTH: int = 10
BGCOLOUR: str = "medium purple"
BUTTONCOLOUR: str = "grey25"

##Set directory
script_dir = os.path.dirname(os.path.abspath(__file__))
images_dir = os.path.join(script_dir, "images")

##Main window
window = tk.Tk()
window.config(bg=BGCOLOUR)
window.title("Rock Paper Scissors")
window.geometry(f"{WIDTH}x{HEIGHT}")

##Open images
rockImg = Image.open(os.path.join(images_dir, "rock.png"))
rockPht = ImageTk.PhotoImage(rockImg)
paperImg = Image.open(os.path.join(images_dir, "paper.png"))
paperPht = ImageTk.PhotoImage(paperImg)
scissorsImg = Image.open(os.path.join(images_dir, "scissors.png"))
scissorsPht = ImageTk.PhotoImage(scissorsImg)
winImg = Image.open(os.path.join(images_dir, "win.png"))
winPht = ImageTk.PhotoImage(winImg)
loseImg = Image.open(os.path.join(images_dir, "lose.png"))
losePht = ImageTk.PhotoImage(loseImg)
drawImg = Image.open(os.path.join(images_dir, "draw.png"))
drawPht = ImageTk.PhotoImage(drawImg)
#starting placeholder
square = Image.open(os.path.join(images_dir, "square.png"))
squarePht = ImageTk.PhotoImage(square)

##Image choices
choicePht = {
    "Rock": rockPht,
    "Paper": paperPht,
    "Scissors": scissorsPht
}
resultPht = {
    "You Win!": winPht,
    "You Lose!": losePht,
    "You Draw": drawPht
}

##Labels
title = tk.Label(master=window, bg=BGCOLOUR, text="Welcome to Rock Paper Scissors")
instruction = tk.Label(master=window, bg=BGCOLOUR, text="Pick Your Choice! (choose wisely)")
playerChoice = tk.Label(master=window, bg=BGCOLOUR, text="Your Choice: \n NULL", width=LABELWIDTH)
playerImg = tk.Label(master=window, bg=BGCOLOUR, image=squarePht, width=LABELWIDTH)
computerChoice = tk.Label(master=window, bg=BGCOLOUR, text="Bot Choice: \n NULL", width=LABELWIDTH)
compImg = tk.Label(master=window, bg=BGCOLOUR, image=squarePht, width=LABELWIDTH)
showResult = tk.Label(master=window, bg=BGCOLOUR, text="Result: \n NULL", width=LABELWIDTH)
resultImg = tk.Label(master=window, bg=BGCOLOUR, image=squarePht, width=LABELWIDTH)

##Winning logic
def determine_winner(P_choice, C_choice):
    if P_choice == "Rock":
        if C_choice == "Rock":
            return "You Draw"
        elif C_choice == "Paper":
            return "You Lose!"
        elif C_choice == "Scissors":
            return "You Win!"
    elif P_choice == "Paper":
        if C_choice == "Rock":
            return "You Win!"
        elif C_choice == "Paper":
            return "You Draw"
        elif C_choice == "Scissors":
            return "You Lose!"
    elif P_choice == "Scissors":
        if C_choice == "Rock":
            return "You Lose!"
        elif C_choice == "Paper":
            return "You Win!"
        elif C_choice == "Scissors":
            return "You Draw"
    # Fallback in case of unexpected input
    return "You Draw"

##Computer choice
def computer_choice():
    options = ["Rock", "Paper", "Scissors"]
    choice = ran.choice(options)
    return choice

##Game run logic
def play_game(choice):
    compchoice = computer_choice()
    result = determine_winner(choice, compchoice)
    
    playerChoice.config(text=f"Your choice: \n {choice}")
    playerImg.config(image=choicePht[choice])
    computerChoice.config(text=f"Bot choice: \n {compchoice}")
    compImg.config(image=choicePht[compchoice])
    showResult.config(text=f"Result: \n {result}")
    resultImg.config(image=resultPht[result])

##Buttons
rock = tk.Button(master=window, image=rockPht, bg=BUTTONCOLOUR, command=lambda: play_game("Rock"))
paper = tk.Button(master=window, image=paperPht, bg=BUTTONCOLOUR, command=lambda: play_game("Paper"))
scissors = tk.Button(master=window, image=scissorsPht, bg=BUTTONCOLOUR, command=lambda: play_game("Scissors"))
rock.config(image=rockPht)
paper.config(image=paperPht)
scissors.config(image=scissorsPht)

"""rock.image = rockPht
paper.image = paperPht
scissors.image = scissorsPht"""

##Display widgets correctly
title.grid(row=0, column=0, columnspan=3, padx=20, pady=7)
instruction.grid(row=1, column=0, columnspan=3, padx=20, pady=7)

playerChoice.grid(row=2, column=0, rowspan=2, padx=7.5, pady=7)
playerImg.grid(row=4, column=0, rowspan=2, padx=7.5, pady=7, sticky="nsew")
computerChoice.grid(row=2, column=2, rowspan=2, padx=7.5, pady=7)
compImg.grid(row=4, column=2, rowspan=2, padx=7.5, pady=7, sticky="nsew")
showResult.grid(row=2, column=1, rowspan=2, padx=7.5, pady=7)
resultImg.grid(row=4, column=1, rowspan=2, padx=7.5, pady=7, sticky="nsew")

rock.grid(row=6, column=0, padx=7.5, pady=12)
paper.grid(row=6, column=1, padx=7.5, pady=12)
scissors.grid(row=6, column=2, padx=7.5, pady=12)

##Run Window
window.mainloop()