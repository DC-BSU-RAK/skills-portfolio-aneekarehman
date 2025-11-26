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

# This is what loads the images up for the GUI
def loadtheimage(path, size=(80, 80)):
    # this is the function that helps to load the images kept in the assets files.
    # Specifically the buttons, which is why the size is kept at 80 by 80.
    img = Image.open(path).resize(size)
    return ImageTk.PhotoImage(img)

# This is where the code for the quiz app begins
class Theultimatequizgame:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1200x800")
        # This is the dimension size of the math quiz.
        self.root.title("Ultimate Math Quiz - By Aneeka Rehman")
        # This is the title of the math quiz
        self.history = []
        # This creates a list that is empty so that the the past questions could be viewed
        # (when clicking the previous button).
        self.historyref = -1
        # since history is mainly used to look back at the questions.
        self.thecompletescore = 0
        # For now, the score is zero. when the game is finished the score is tallied here.
        # These are the 3 difficulty levels that were listed in the brief
        self.the3levels = ["Easy",
                           "Moderate",
                           "Advanced"]

        # This is the Google Press Start font taken from google fonts
        try:
            self.newfont = font.Font(family="Press Start 2P", size=16)
        except tk.TclError:
            # If the font taken from google fonts fails to load on the application
            # a default Arial font is used instead for ALL the text in the app. 
            self.newfont = font.Font(family="Arial", size=16)
            # the size is kept at 16 for all texts that use the font, which is mostly windows.
        root.option_add("*Font", self.newfont)

        # ---------- Button Positions ----------
        self.buttonplace = {
            "startbutton": (500, 600),
            # This is the way the different imagebuttons are placed in this app. Using
            # tuples to mark their position in this case 500 is the xaxis and 600 is the yaxis.
            "diff_easy": (500, 400),
            "diff_moderate": (500, 520),
            "diff_advanced": (500, 640),
            # These three buttons are what lead the user to the different levels. Found on the difficulty page.
            "submitbutton": (900, 330),
            # This is the tick button used to move onto the next quesion
            "homebuttonforquiz": (900, 530),
            # This is the home button icon seen below the tick button
            "previousbutton": (800, 430),
            # This is the button used to go back to the previous question
            "nextbutton": (995, 430),
            "progress_bar": (380, 570),
            # This is the progress bar that updates as the questions go by
            "thenextlevelbutton": (460, 500),
            # This is the the button that moves onto the next level
            "headtohomebutton": (460, 600),
            # This button is the return to home button
            "finalheadtohomebutton": (460, 580)
        }

        self.pages = {}
            # This stores the pages 

        # This is to load the progress bar images one by one
        self.progress_images = []
        for i in range(1, 11):
            # There are 10 progress bar images that need to be loaded.
            path = f"assets/progressbar/progress_{i}.png"
            # This is where the progress bar images are kept in the progress bar page.
            img = ImageTk.PhotoImage(Image.open(path))
            # this allows the images to run in their numbered order
            self.progress_images.append(img)

        # Here are the five different pages seen in this application:
        self.FirstPage()
        self.Levelspage()
        self.Quizpage()
        self.ResultsPage()
        self.FinalResultsPage()

        # The variables that we will work with
        self.thelevels = {"Easy": (1, 9),
                          "Moderate": (10, 99),
                          "Advanced": (1000, 9999)}
        self.amountofquestions = 10
        # there are 10 questions in each level to be answered by the user.
        # the number of questions answered at the moment are zero
        self.countofquestions = 0
        self.score = 0
        #for now the score is at 0 since the game hasnt begun
        self.attempts = 0
        # The user is given 2 attempts but it starts off at zero


        self.visiblepage("start")
        # This is to display the pages on screen.

    # This is what allows for changes in frames
    def visiblepage(self, name):
        self.pages[name].tkraise()
        # the tkraise method is used to switch between pages   

    # The first page starts here ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def FirstPage(self):
        frame = tk.Frame(self.root, width=1200, height=800)
        # This is to set the screen size for the first page

        frame.place(x=0, y=0)
        self.pages["start"] = frame
        # This loads the actual image and switches it to a tkinter image object

        background = ImageTk.PhotoImage(Image.open("assets/pages/FirstPage.png").resize((1200, 800)))
        label = tk.Label(frame, image=background, bd=0, highlightthickness=0)
        label.image = background
        # this prevents the image from being garbage collected.
        label.place(x=0, y=0, relwidth=1, relheight=1)

        start_normal_img = ImageTk.PhotoImage(Image.open("assets/FPbuttons/Play.png"))
        start_hover_img = ImageTk.PhotoImage(Image.open("assets/FPbuttons/Play_hover.png"))

        startbutton = tk.Label(frame, image=start_normal_img, cursor="hand2", bd=0, highlightthickness=0)
        # The border has been removed to create a seamless blend of the button, and a parent frame is created to
        # place the button in, the cursor is changed to let the user know they can click onto the button
        startbutton.place(x=self.buttonplace["startbutton"][0], y=self.buttonplace["startbutton"][1])
        startbutton.bind("<Button-1>", lambda e: self.visiblepage("difficulty"))
        # When the user left clicks the page changes to the difficulty page.

        startbutton.bind("<Enter>", lambda e: startbutton.config(image=start_hover_img))
        startbutton.bind("<Leave>", lambda e: startbutton.config(image=start_normal_img))
        # This creates the hover effect with the 2 different images

        startbutton.normal_img = start_normal_img
        startbutton.hover_img = start_hover_img
        # this prevents the image from being garbage collected.

    # The rest of the buttons function this way as well

    # The difficulty page starts here ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def Levelspage(self):
        frame = tk.Frame(self.root, width=1200, height=800)
        frame.place(x=0, y=0)
        self.pages["difficulty"] = frame

        bg_img = ImageTk.PhotoImage(Image.open("assets/pages/difpage.png").resize((1200, 800)))
        label = tk.Label(frame, image=bg_img, bd=0, highlightthickness=0)
        label.image = bg_img
        label.place(x=0, y=0, relwidth=1, relheight=1)

        self.levels = ["Easy",
                       "Moderate",
                       "Advanced"]
        # These are the 3 button levels to choose from.
        self.diff_buttons = {}
        for level in self.levels:
            normal_img = ImageTk.PhotoImage(Image.open(f"assets/levelbuttons/{level}_normal.png"))
            hover_img = ImageTk.PhotoImage(Image.open(f"assets/levelbuttons/{level}_hover.png"))
            btn = tk.Label(frame, cursor="hand2", bd=0, image=normal_img, highlightthickness=0)
            x, y = self.buttonplace[f"diff_{level.lower()}"]
            btn.place(x=x, y=y)
            # This positions the buttons using the axis' assigned.
            btn.normal_img = normal_img
            btn.hover_img = hover_img
            btn.bind("<Button-1>", lambda e, l=level: self.quizbegin(l))
            btn.bind("<Enter>", lambda e, b=btn: b.config(image=b.hover_img))
            btn.bind("<Leave>", lambda e, b=btn: b.config(image=b.normal_img))
            self.diff_buttons[level] = btn

# The quiz page starts here ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def Quizpage(self):
        frame = tk.Frame(self.root, width=1200, height=800)
        frame.place(x=0, y=0)
        self.pages["quiz"] = frame

        bg_img = ImageTk.PhotoImage(Image.open("assets/pages/Levelspage.png").resize((1200, 800)))
        label = tk.Label(frame, image=bg_img, bd=0, highlightthickness=0)
        label.image = bg_img
        label.place(x=0, y=0, relwidth=1, relheight=1)

        # Questions and the box to enter the answer in
        self.question_label = tk.Label(frame, text="", font=("Press Start 2P", 28), bg="#010103", fg="white")
        self.question_label.place(x=400, y=200)

        self.answer_entry = tk.Entry(frame, font=("Press Start 2P", 35), width=10)
        self.answer_entry.place(x=405, y=300)
        self.answer_entry.bind("<Return>", lambda event: self.correctanswercheck())

        # The buttons on the quiz page
        self.submit_normal = loadtheimage("assets/levelbuttons/tick.png")
        self.submit_hover = loadtheimage("assets/levelbuttons/tick_hover.png")

        self.prev_normal = loadtheimage("assets/levelbuttons/previous.png")
        self.prev_hover = loadtheimage("assets/levelbuttons/previous_hover.png")

        self.next_normal = loadtheimage("assets/levelbuttons/next.png")
        self.next_hover = loadtheimage("assets/levelbuttons/next_hover.png")

        self.home_normal = loadtheimage("assets/levelbuttons/home_normal.png")
        self.home_hover = loadtheimage("assets/levelbuttons/home_hover.png")

        # Submit Button
        self.submitbutton = tk.Label(frame, image=self.submit_normal, cursor="hand2", bd=0, highlightthickness=0)
        x, y = self.buttonplace["submitbutton"]
        self.submitbutton.place(x=x, y=y)
        self.submitbutton.bind("<Button-1>", lambda e: self.correctanswercheck())
        self.submitbutton.bind("<Enter>", lambda e: self.submitbutton.config(image=self.submit_hover))
        self.submitbutton.bind("<Leave>", lambda e: self.submitbutton.config(image=self.submit_normal))

        # Previous Button
        self.previousbutton = tk.Label(frame, image=self.prev_normal, cursor="hand2", bd=0, highlightthickness=0)
        x, y = self.buttonplace["previousbutton"]
        self.previousbutton.place(x=x, y=y)
        self.previousbutton.bind("<Enter>", lambda e: self.previousbutton.config(image=self.prev_hover))
        self.previousbutton.bind("<Leave>", lambda e: self.previousbutton.config(image=self.prev_normal))
        self.previousbutton.bind("<Button-1>", lambda e: self.previous_question())

        # Next Button
        self.nextbutton = tk.Label(frame, image=self.next_normal, cursor="hand2", bd=0, highlightthickness=0)
        x, y = self.buttonplace["nextbutton"]
        self.nextbutton.place(x=x, y=y)
        self.nextbutton.bind("<Enter>", lambda e: self.nextbutton.config(image=self.next_hover))
        self.nextbutton.bind("<Leave>", lambda e: self.nextbutton.config(image=self.next_normal))
        self.nextbutton.bind("<Button-1>", lambda e: self.manual_next())

        # Home Button
        self.home_btn = tk.Label(frame, image=self.home_normal, cursor="hand2", bd=0, highlightthickness=0)
        x, y = self.buttonplace["homebuttonforquiz"]
        self.home_btn.place(x=x, y=y)
        self.home_btn.bind("<Button-1>", lambda e: self.visiblepage("start"))
        self.home_btn.bind("<Enter>", lambda e: self.home_btn.config(image=self.home_hover))
        self.home_btn.bind("<Leave>", lambda e: self.home_btn.config(image=self.home_normal))

        # This is the progress bar that showcases how far along the user is with the questions
        self.progress_bar_label = tk.Label(frame, bd=0, highlightthickness=0)
        x, y = self.buttonplace["progress_bar"]
        self.progress_bar_label.place(x=x, y=y)

# The Results page starts here ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def ResultsPage(self):
        frame = tk.Frame(self.root, width=1200, height=800)
        frame.place(x=0, y=0)
        self.pages["results"] = frame

        bg_img = ImageTk.PhotoImage(Image.open("assets/pages/rpage.png"))
        label = tk.Label(frame, image=bg_img, bd=0, highlightthickness=0)
        label.image = bg_img
        label.place(x=0, y=0, relwidth=1, relheight=1)

        self.results_score_label = tk.Label(frame, text="", font=self.newfont, fg="white", bg="#111")
        self.results_score_label.place(x=600, y=280)

        self.results_percent_label = tk.Label(frame, text="", font=self.newfont, fg="white", bg="#111")
        self.results_percent_label.place(x=600, y=390)

        # next level button to move onto the moderate or advanced level
        self.next_level_normal = ImageTk.PhotoImage(Image.open("assets/levelbuttons/nextlevel.png"))
        self.next_level_hover = ImageTk.PhotoImage(Image.open("assets/levelbuttons/nextlevel_hover.png"))

        self.thenextlevelbutton = tk.Label(frame, image=self.next_level_normal, cursor="hand2", bd=0, highlightthickness=0)
        x, y = self.buttonplace["thenextlevelbutton"]
        self.thenextlevelbutton.place(x=x, y=y)
        self.thenextlevelbutton.bind("<Button-1>", self.next_level)
        self.thenextlevelbutton.bind("<Enter>", lambda e: self.thenextlevelbutton.config(image=self.next_level_hover))
        self.thenextlevelbutton.bind("<Leave>", lambda e: self.thenextlevelbutton.config(image=self.next_level_normal))

        # Home Button
        self.results_home_normal = ImageTk.PhotoImage(Image.open("assets/homebuttons/headtohome.png"))
        self.results_home_hover = ImageTk.PhotoImage(Image.open("assets/homebuttons/headtohome_hover.png"))

        self.headtohomebutton = tk.Label(frame, image=self.results_home_normal, cursor="hand2", bd=0, highlightthickness=0)
        x, y = self.buttonplace["headtohomebutton"]
        self.headtohomebutton.place(x=x, y=y)
        self.headtohomebutton.bind("<Button-1>", lambda e: self.visiblepage("start"))
        self.headtohomebutton.bind("<Enter>", lambda e: self.headtohomebutton.config(image=self.results_home_hover))
        self.headtohomebutton.bind("<Leave>", lambda e: self.headtohomebutton.config(image=self.results_home_normal))

# The Final Results page starts here ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Same logic applies from the results page

    def FinalResultsPage(self):
        frame = tk.Frame(self.root, width=1200, height=800)
        frame.place(x=0, y=0)
        self.pages["final_results"] = frame

        bg_img = ImageTk.PhotoImage(Image.open("assets/pages/Results Final.png"))
        label = tk.Label(frame, image=bg_img, bd=0, highlightthickness=0)
        label.image = bg_img
        label.place(x=0, y=0, relwidth=1, relheight=1)

        self.final_score_label = tk.Label(frame, text="", font=self.newfont, fg="white", bg="#111")
        self.final_score_label.place(x=600, y=280)

        self.final_percent_label = tk.Label(frame, text="", font=self.newfont, fg="white", bg="#111")
        self.final_percent_label.place(x=600, y=390)

        self.final_home_btn_img = ImageTk.PhotoImage(Image.open("assets/homebuttons/headtohome.png"))
        self.final_home_btn_hover = ImageTk.PhotoImage(Image.open("assets/homebuttons/headtohome_hover.png"))

        self.finalheadtohomebutton = tk.Label(frame, image=self.final_home_btn_img, cursor="hand2", bd=0, highlightthickness=0)
        x, y = self.buttonplace["finalheadtohomebutton"]
        self.finalheadtohomebutton.place(x=x, y=y)
        self.finalheadtohomebutton.bind("<Button-1>", lambda e: self.visiblepage("start"))
        self.finalheadtohomebutton.bind("<Enter>", lambda e: self.finalheadtohomebutton.config(image=self.final_home_btn_hover))
        self.finalheadtohomebutton.bind("<Leave>", lambda e: self.finalheadtohomebutton.config(image=self.final_home_btn_img))

# This is where actual game mechanics take place
    def quizbegin(self, difficulty):
        self.difficulty = difficulty
        self.countofquestions = 0
        self.score = 0
        self.attempts = 0
        self.history = []
        self.historyref = -1
        self.updatebar()
        self.visiblepage("quiz")
        self.nextquestion()

# This is where the random question is generated.
# Random numbers and operations (addition or subtraction are chosen)
    def generatequestion(self):
        minvalue, maxvalue = self.thelevels[self.difficulty]
        firstnumber = random.randint(minvalue, maxvalue)
        num2 = random.randint(minvalue, maxvalue)
        op = random.choice(["+", "-"])
        answer = firstnumber + num2 if op == "+" else firstnumber - num2
        return firstnumber, num2, op, answer

    def nextquestion(self):
        if self.countofquestions >= self.amountofquestions:
            self.show_results()
            return
        # This section checks if the quiz is over
        firstnumber, num2, op, answer = self.generatequestion()
        self.history.append((firstnumber, num2, op, answer))
        # if not it generates a new question
        self.historyref = len(self.history) - 1
        # This stores the information of the new question
        self.firstnumber, self.num2, self.operation, self.answer = firstnumber, num2, op, answer

        self.question_label.config(text=f"Q{self.countofquestions + 1}. {firstnumber} {op} {num2} = ?")
        self.answer_entry.delete(0, tk.END)
        # increase the number of attempts once answered and clears the input area for the next question
        self.attempts = 0
        self.countofquestions += 1
        # This updates the progress bar
        self.updatebar()

    def updatebar(self):
        idx = self.historyref
        # This checks what questions the user in on between one to ten
        if 0 <= idx < len(self.progress_images):
            self.progress_bar_label.config(image=self.progress_images[idx])
            # This is to mainly update the progress bar
            self.progress_bar_label.image = self.progress_images[idx]

    def correctanswercheck(self):
        raw = self.answer_entry.get().strip()
        if raw == "":
            # This recieves the user input
            return
        try:
            user_ans = int(raw)
            # to check if its an integer
        except ValueError:
            return

        self.attempts += 1
        # keeps track of which attempt the user is on

        if user_ans == self.answer:
            # If the user gets the answer right on the first try then they get 10 points,
            # if they get it right on the second attempt then its 5 points
            points = 10 if self.attempts == 1 else 5
            self.score += points
            self.root.after(550, self.nextquestion)
            # a slight delay then the program moves onto the next question
        else:
            if self.attempts < 2:
                pass
            # if after both attempts the answer is wrong then -5 points
            else:
                self.score = max(self.score - 5, 0)
                self.root.after(600, self.nextquestion)


# The design for the popups
    def popups(self, message, duration=1800):
# This is used to place the popup at the top centered slightly
        top = tk.Toplevel(self.root)
        top.overrideredirect(True)
        top.attributes("-topmost", True)

        # Canvas for retro window
        canvas = tk.Canvas(top, width=400, height=150, bg="#010103", highlightthickness=6, highlightbackground="white")
        canvas.pack()

        # Display message
        canvas.create_text(190, 85, text=message, font=("Press Start 2P", 15), fill="white")

        # Center the popup
        self.root.update_idletasks()
        rw = self.root.winfo_width()
        rh = self.root.winfo_height()
        rx = self.root.winfo_rootx()
        ry = self.root.winfo_rooty()
        tw = top.winfo_reqwidth()
        th = top.winfo_reqheight()
        x = rx + (rw - tw) // 2
        y = ry + (rh - th) // 2
        top.geometry(f"+{x}+{y}")
# This is used to center the popup

        # Auto-destroy after duration
        top.after(duration, top.destroy)


# The popup with the text
    def correctanswercheck(self):
        raw = self.answer_entry.get().strip()
        if raw == "":
            self.popups("Enter a number", duration=1800)
            # allows the user to enter a number if they havent done so
            return
        try:
            user_ans = int(raw)
        except ValueError:
            # if the user enters anything other than an integer they're asked to enter a valid number
            self.popups("Enter a valid number", duration=1800)
            return

        self.attempts += 1

        if user_ans == self.answer:
            points = 10 if self.attempts == 1 else 5
            self.score += points
            self.popups(f"Right Answer +{points} points", duration=1400)
            self.root.after(550, self.nextquestion)
        else:
            # These could be shown to the user if they get the answer right or wrong.
            if self.attempts < 2:
                self.popups("Incorrect! Try again", duration=1400)
            else:
                self.score = max(self.score - 5, 0)
                self.popups(f"Wrong Answer -5 pts  Ans:{self.answer}", duration=1600)
                self.root.after(600, self.nextquestion)



    def manual_next(self):
        # Allows the user to manually move forward if they dont want to answer a question
        if self.historyref < len(self.history) - 1:
            self.historyref += 1
            firstnumber, num2, op, answer = self.history[self.historyref]
            self.firstnumber, self.num2, self.operation, self.answer = firstnumber, num2, op, answer
            self.question_label.config(text=f"Q{self.historyref + 1}. {firstnumber} {op} {num2} = ?")
            self.answer_entry.delete(0, tk.END)
            self.updatebar()
        else:
            self.nextquestion()

# Same concept here except they can go back
    def previous_question(self):
        if self.historyref > 0:
            self.historyref -= 1
            firstnumber, num2, op, answer = self.history[self.historyref]
            self.firstnumber, self.num2, self.operation, self.answer = firstnumber, num2, op, answer
            self.question_label.config(text=f"Q{self.historyref + 1}. {firstnumber} {op} {num2} = ?")
            self.answer_entry.delete(0, tk.END)
            self.updatebar()

    def show_results(self):
        self.thecompletescore += self.score
        current_level_index = self.the3levels.index(self.difficulty) + 1
        total_possible_points = current_level_index * self.amountofquestions * 10
        percent = int((self.thecompletescore / total_possible_points) * 100)
        # This is used to showcase the results in points and percentage after each level
        self.results_score_label.config(text=f"{self.thecompletescore}")
        self.results_score_label.place(x=700, y=280)  
        # here is where they are written
        self.results_percent_label.config(text=f"{percent}%")
        self.results_percent_label.place(x=700, y=390)

        if self.difficulty == self.the3levels[-1]:
            self.show_final_results()
        else:
            self.visiblepage("results")

    def next_level(self, event=None):
        # This moves the user onto the next level after they have completed either easy or moderate
        current_index = self.the3levels.index(self.difficulty)
        next_index = current_index + 1
        if next_index < len(self.the3levels):
            next_diff = self.the3levels[next_index]
            self.quizbegin(next_diff)
        else:
            self.show_final_results()

# This where the user is shown the accumlated results, which include both the points and percentage.
    def show_final_results(self):
        total_possible = self.amountofquestions * 10 * len(self.the3levels)
        percent = int((self.thecompletescore / total_possible) * 100) if total_possible > 0 else 0

        self.final_score_label.config(text=f"{self.thecompletescore}")
        self.final_score_label.place(x=700, y=280)  

        self.final_percent_label.config(text=f"{percent}%")
        self.final_percent_label.place(x=700, y=390)  


        self.visiblepage("final_results")


# This runs the application
if __name__ == "__main__":
    root = tk.Tk()
    app = Theultimatequizgame(root)
    root.mainloop()
