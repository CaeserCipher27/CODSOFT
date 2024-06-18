import tkinter
from tkinter import *
import random

# Color Constants
LIGHT = "#FFE6E6"
YELLOW = "#FFFF80"
PINK_1 = "#FF5580"
PINK_2 = "#F6F7C4"
GREEN = "#A1EEBD"

comp_selection = None

window = Tk()
window.title("Rock Paper Scissors Game")
window.geometry("700x600")
window.config(bg=PINK_1, padx=30, pady=30)

heading = Label(text="Play Rock Paper Scissors!", font="jokerman 30 bold", bg=PINK_1, fg=LIGHT)
heading.pack(side=TOP)

subHeading = Label(text='Select any ONE from rock, paper, scissors', font='calibri 20 bold', bg=PINK_1, fg=PINK_2)
subHeading.pack(side=TOP, pady=20)

# game_list = ['rock', 'paper', 'scissors']

user_input = StringVar()

comp_selection = random.randint(1, 3)

var = StringVar()

enter = Entry(font='Tahoma 18', textvariable=user_input, bg=YELLOW)
enter.pack(side=TOP, pady=10)

if comp_selection == 1:
    comp_selection = 'rock'
elif comp_selection == 2:
    comp_selection = 'paper'
else:
    comp_selection = 'scissors'


def Play():
    user_selection = user_input.get()
    if user_selection.lower() == comp_selection.lower():
        var.set("It's a Draw! You made a same choice as computer.")
    elif user_selection.lower() == 'rock' and comp_selection.lower() == 'paper':
        var.set("You Lose! Computer chose Paper.")
    elif user_selection.lower() == 'rock' and comp_selection.lower() == 'scissors':
        var.set("You Win! Computer chose Scissors.")
    elif user_selection.lower() == 'paper' and comp_selection.lower() == 'scissors':
        var.set("You Lose! Computer chose Scissors.")
    elif user_selection.lower() == 'paper' and comp_selection.lower() == 'rock':
        var.set("You Win! Computer chose Rock.")
    elif user_selection.lower() == 'scissors' and comp_selection.lower() == 'rock':
        var.set("You Lose! Computer chose Rock.")
    elif user_selection.lower() == 'scissors' and comp_selection.lower() == 'paper':
        var.set("You Win! Computer chose Paper.")
    else:
        var.set("Invalid input! Select from - rock, paper & scissors")


def GameReset():
    global comp_selection
    var.set("")
    user_input.set("")
    comp_selection = random.randint(1, 3)
    if comp_selection == 1:
        comp_selection = 'rock'
    elif comp_selection == 2:
        comp_selection = 'paper'
    else:
        comp_selection = 'scissors'


def GameExit():
    window.destroy()


result_display = Label(textvariable=var, font='Perpetua 15', bg=GREEN)
result_display.pack(pady=10)

play_button = tkinter.Button(font='Helvetica 12 bold', text='PLAY', padx=5, bg='white', command=Play)
play_button.pack(side=TOP, pady=20)

reset_button = Button(font='Helvetica 12 bold', text='RESET', padx=5, bg='white', command=GameReset)
reset_button.pack(side=TOP, pady=20)

exit_button = Button(font='Helvetica 12 bold', text='EXIT', padx=5, bg='white', command=GameExit)
exit_button.pack(side=TOP, pady=20)

window.mainloop()
