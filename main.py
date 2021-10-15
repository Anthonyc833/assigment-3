"""from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys"""
"import pygame"
from tkinter import *
from random import randint
import tkinter as tk


root = Tk()

lb1 = tk.Label(root, text="Hit or pass(h) or (no)").grid(row=0)
e1 = tk.Entry(root)
e1.grid(row=0, column=1)




player_total = 0
score = 21
playing = True


def maingame():
    player_total = 0
    playing = True
    while playing == True:
        Player_input = str(input("Hit or pass(h) or (no)"))
        if player_total == 21:
            break
        else:
            print(Player_input)
            if Player_input == "h":
                rannum = randint(1, 11)
                player_total = rannum + player_total
                print(player_total)
                x = Label(text = str(player_total))
                x.grid()
                playing = True
            if Player_input == "no":
                print("The score you got is", player_total)
                break








btn1 = Button(root, text="go", command=maingame, height="2", width="30").grid(column="3")

root.mainloop()



"""App = QApplication(sys.argv)

# create the instance of our Window
window = maingame()

# start the app
sys.exit(App.exec()) """




