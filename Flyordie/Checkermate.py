import tkinter as tk
from overlay import Window
import pygame, sys
from pygame.locals import *


class setup_board(): 
        def board():
                win = Window()
                backgroundImage = tk.PhotoImage(file = "/Users/admin/Desktop/CODING JOURNAL /Flyordie/board.png")
                label = tk.Label(win.root, text="CheckersML",image = backgroundImage)
                win.transparent = True 
                win.alpha = (100)		
                win.size = (600,600)               
                label.pack()
                Window.launch()  

class how_the_game_is_played():      
        def white_checker(self, parameter_list):
                """

                create something awesome
                """
                pass

setup_board.board()
