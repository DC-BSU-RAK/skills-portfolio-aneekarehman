
# Exercise 2 - Skills Portfolio 

# Alexa Tell Me a Joke

# Aneeka Rehman - Creative Computing - Code Lab II


import tkinter as tk
# This creates the window for the buttons and labels

from PIL import Image, ImageTk
# This is used for the images, specifically the background in this case
import pygame
# This is used to play the laughing sound effect 

import random
# Used to randomly select the jokes

# This starts the pygame audio system to play the laughing sound effect
pygame.mixer.init()

# This is my background image file that stores my background iamge
BGFILE = "background.png"


# This is the function that runs when the punchline button is clicked,
# it changes the text the label displays and plays the laughing sound effect
def revealpunchline():
    actualpunchline.config(text=jokeonscreen[1])

# This is the sound effect that plays, immediately
    sound = pygame.mixer.Sound("laugh2.mp3")
    sound.play()




# This is a function created to load the jokes from the txt file
def openthejokes():
    # This is where the jokes are stored
    jokes = []
    with open("randomJokes.txt", "r", encoding="utf-8") as f:
        for line in f:
            if "?" in line:
                # This is for the question marks in the joke questions.
                setup, punchline = line.split("?", 1)
                jokes.append((setup + "?", punchline.strip()))
    return jokes





# This function obtains the jokes randomly
def randomjoke():
    global jokeonscreen
    jokeonscreen = random.choice(jokes)
    # This updates the joke label to showcase the upcoming joke
    joke.config(text=jokeonscreen[0])
    # This is where the punchline is hidden
    actualpunchline.config(text="")


# The actual GUI window

root = tk.Tk()
# The title of the application
root.title("Alexa Tell Me a Joke")
# The dimension of the application
root.geometry("800x600")

# The background image is opened here
background = Image.open("background.png")
background = background.resize((800, 600))
backgroundimage = ImageTk.PhotoImage(background)

# The image is converted into an image object so that it could be displayed
background_label = tk.Label(root, image=backgroundimage)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
background_label.image = backgroundimage



jokes = openthejokes()
jokeonscreen = random.choice(jokes)
# This calls the jokes function and picks a random joke to be displayed



# This is created for the joke to be displayed, including its font and sizing
# And where it is placed in the application
joke = tk.Label(root, text=jokeonscreen[0], font=("Arial", 18))
joke.pack(pady=(370, 15))

# Same goes for the punchline
actualpunchline = tk.Label(root, text="", font=("Arial", 30), fg="pink", bg="white")
actualpunchline.pack( pady=15)


# Here are the 3 different buttons:

# This is the next button, that causes a new random joke to be displayed on screen
nextbutton = tk.Button(root, text="Next Joke", font=("Arial", 19), command=randomjoke)
nextbutton.pack(side="bottom", pady=5)

# This is the punchline button, that reveals the hidden corresponding punchline
punchlinebutton = tk.Button(root, text="Punchline", font=("Arial", 19), command=revealpunchline)
punchlinebutton.pack(side="bottom", pady=5)

# This is the final button, the quit button which is above the other 2 buttons,
# and is used to exit the application completely.
quitbutton = tk.Button(root, text="Quit the App", font=("Arial", 14), command=root.destroy)
quitbutton.pack(side="bottom", pady=(0, 4))



# This runs the entire application
root.mainloop()