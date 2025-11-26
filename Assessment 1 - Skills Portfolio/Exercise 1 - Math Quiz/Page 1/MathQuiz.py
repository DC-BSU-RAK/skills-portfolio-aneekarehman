
# CODE LAB II - Skills Portfolio 
# Aneeka Rehman Memon

# EXERCISE 1: Math Quiz


import tkinter as tk 
# this imports the tkinter graphical user interface 

from tkinter import font 
# this imports the fonts that were used in this specific application, 

from PIL import ImageTk, Image
# PIL stands for Pyhtong Imaging Library or Pillow,
# this is used to load images on this application.

import random
# I will be using the random generator to generate random numbers for 
# the quiz questions as well as the addition or subtraction operation. 



def loadtheimage(path, size=(80, 80)):
    # this is the function that helps to load the images kept in the assets files.
    # Specifically the buttons, which is why the size is kept at 80 by 80.
    img = Image.open(path).resize(size)
    return ImageTk.PhotoImage(img)

# This is where the code for the quiz app begins

class UltimateMathQuiz: 
    def __init__(self, root):
        self.root = root
        self.root.title("Ultimate Math Quiz - By Aneeka Rehman")
        # This is the title of the math quiz
        self.root.geometry("1200x800")
        # This is the dimension size of the math quiz.
        
        # These are the 3 difficulty levels that were listed in the brief
        self.threelevels = ["Easy", "Moderate", "Advanced"]
        
        self.history = []
        # This creates a list that is empty so that the the past questions could be viewed
        # (when clicking the previous button).
        
        self.historyref = -1
        # since history is mainly used to look back at the questions.
        
        self.talliedpoints = 0
        # For now, the score is zero. when the game is finished the score is tallied here.
        
        try:
            self.googlefontPRESS = font.Font(family="Press Start 2P", size=16)
        except tk.TclError:
            # If the font taken from google fonts fails to load on the application
            # a default Arial font is used instead for ALL the text in the app. 
            self.googlefontPRESS = font.Font(family="Arial", size=16)
            # the size is kept at 16 for all texts that use the font, which is mostly windows.
            root.option_add("*Font", self.googlefontPRESS)
            
        self.ButtonPositions = {
            "playbuttonint": (500, 600),
            # This is the way the different imagebuttons are placed in this app. Using
            # tuples to mark their position in this case 500 is the xaxis and 600 is the yaxis.
            
            "button_easy": (500, 400),
            "button_moderate": (500, 400),
            "button_advanced": (500, 640),
            # These three buttons are what lead the user to the different levels. Found on the difficulty page.
            
            "tickbutton":(900, 330),
            # This is the tick button used to move onto the next quesion
            
            "returntohomebutton":(900, 530),
            # This is the home button icon seen below the tick button
            
            "previousbutton": (800, 430),
            # This is the button used to go back to the previous question
            
            
            
        }