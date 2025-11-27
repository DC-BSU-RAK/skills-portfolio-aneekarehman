import os

import tkinter as tk
# This is what creates the window and widgets for this applications
from tkinter import simpledialog

# This produces the simple popup
from tkinter import Scrollbar
# I have imported a scroll-bar for the student information box
from tkinter import Frame

from tkinter import messagebox
# The messagebox gives out warnings, or errors made by the user
from tkinter import Menu
# This creates the menu option seen on the right hand side


FILENAME = "studentMarks.txt"
# This is the file that stores the information on the different students 
displaythestudentinfo = None
root = tk.Tk()
# The app window is created here


root.configure(bg="#06003E") 
# This is the blue background color



# This is the function that showcases the existance of the fil
def checkthefile():
    if not os.path.exists(FILENAME):
        f = open(FILENAME, "w")
        f.close()

# This function specifies which mark the student has recieved
def getthegrade(percent):
    if percent >= 70:
        return "A"
    # if its 70 or above then the student recieves an A grade.
    elif percent >= 60:
        return "B"
    # if its 60 or above then the student recieves an B grade.
    elif percent >= 50:
        return "C"
    # if its 50 or above then the student recieves an C grade.
    elif percent >= 40:
        return "D"
    # if its 40 or above then the student recieves an D grade.
    else:
        return "F"
    # if its below 40 then the student recieves a F mark.


# This reads the student file
def studentinfo():
    checkthefile()
    studentlist = []
    
    file = open(FILENAME, "r")
    # opens the file to read the file
    lines = file.readlines()
    # this reads the file
    file.close()
    
    for line in lines:
        line = line.strip()
        if line == "":
            continue
            
        parts = line.split(',')
        # Splits the line by commas
        
        if len(parts) == 6:
            code = parts[0]
            # This gets the marks from the user
            name = parts[1]
            
            # Get the marks
            try:
                mark1 = int(parts[2])
            except:
                mark1 = 0
            try:
                mark2 = int(parts[3])
            except:
                mark2 = 0
            try:
                mark3 = int(parts[4])
            except:
                mark3 = 0
            try:
                exam = int(parts[5])
            except:
                exam = 0
            
            # This calculates the total
            coursework = mark1 + mark2 + mark3
            # The sum of all 3 marks is the coursework result
            total = coursework + exam
            # This is the total of the coursework and exam
            percentage = round((total / 160) * 100, 2)
            # This calculates the percentage and produces a letter grade
            grade = getthegrade(percentage)
            
            # This is to create a dictionary for the students
            student = {}
            """These are the places that store the student code,
                student name, their course work marks 1 - 3. They also store
                the scores and percentages of the school work."""
            student["code"] = code
            student["name"] = name
            student["mark1"] = mark1
            student["mark2"] = mark2
            student["mark3"] = mark3
            student["exam"] = exam
            student["coursework"] = coursework
            student["percentage"] = percentage
            student["grade"] = grade
            
            studentlist.append(student)
    # Return the list of all students
    return studentlist



def studentsback(students):
    file = open(FILENAME, "w")
    # Iterates through the students in the dictionary list
    for s in students:
        line = str(s["code"]) + "," + str(s["name"]) + "," + str(s["mark1"]) + "," + str(s["mark2"]) + "," + str(s["mark3"]) + "," + str(s["exam"]) + "\n"
        file.write(line)
    
    file.close()

# This is used to update the display
def updatethedisplay():
    students = studentinfo()
    
    displaythestudentinfo.config(state="normal")
    displaythestudentinfo.delete("1.0", tk.END)
    
    if len(students) == 0:
        displaythestudentinfo.insert("1.0",
                                     "No students in the system yet")
        # This is shown when the list is empty
    else:
        text = ""
        totalpercent = 0
        
        for s in students:
            """this is a loop that goes through all students, and
                adds student name, code, coursework total marks, 
                the percentage and the grades."""
            
            text = text + "Name: " + s["name"] + "\n"
            text = text + "Code: " + s["code"] + "\n"
            text = text + "Coursework: " + str(s["coursework"]) + "\n"
            text = text + "Exam: " + str(s["exam"]) + "\n"
            text = text + "Percentage: " + str(s["percentage"]) + "%\n"
            text = text + "Grade: " + s["grade"] + "\n\n"
            
            totalpercent = totalpercent + s["percentage"]
        
        avg = round(totalpercent / len(students), 2)
        text = text + "Total Students: " + str(len(students)) + "\n"
        text = text + "Average: " + str(avg) + "%"
        
        displaythestudentinfo.insert("1.0", text)
    
    displaythestudentinfo.config(state="disabled")

# To view the information on each individual student
def viewa_spec_student():
    students = studentinfo()
    if len(students) == 0:
        messagebox.showinfo("Error",
                            "No students found")
        return
    # Error box is shown if the student doesnt exist in the program
    
    # This is used to find the student info through the specific code
    code = simpledialog.askstring("Search",
                                  "Enter student code:")
    if code == None:
        return
    
    found = False
    for s in students:
        if s["code"] == code:
            information = "Name: " + s["name"] + "\n\n"
            information = information + "Code: " + s["code"] + "\n\n"
            information = information + "Coursework: " + str(s["coursework"]) + "\n\n"
            information = information + "Exam: " + str(s["exam"]) + "\n\n"
            information = information + "Percentage: " + str(s["percentage"]) + "%\n\n"
            information = information + "Grade: " + s["grade"]
            # If found the students information is displayed in this popup
            messagebox.showinfo("Student Info",
                                information)
            found = True
            break
    
    if not found:
        messagebox.showinfo("Error",
                            "Student not found")
# If the student isnt found error pop-up is shown.


# This function showcases the highest mark, and the student info of the acheiver
def showhighestachiever():
    students = studentinfo()
    if len(students) == 0:
        messagebox.showinfo("Error",
                            "No students found")
        return
    
    markhighest = students[0]
    for s in students:
        if s["percentage"] > markhighest["percentage"]:
            markhighest = s
    # The corresponding information is shown like this
    information = "Name: " + markhighest["name"] + "\n"
    information = information + "Code: " + markhighest["code"] + "\n"
    information = information + "Percentage: " + str(markhighest["percentage"]) + "%\n"
    information = information + "Grade: " + markhighest["grade"]
    # In a pop up over here
    messagebox.showinfo("Highest Mark", information)

# This showcases the lowest mark holder and is similiar to the highest mark acheiver
def showlowestmark():
    students = studentinfo()
    if len(students) == 0:
        messagebox.showinfo("Error", "No students found")
        return
    
    lowest = students[0]
    for s in students:
        if s["percentage"] < lowest["percentage"]:
            lowest = s
    # This is how the pop up is shown of the lowest achiever
    information = "Name: " + lowest["name"] + "\n"
    information = information + "Code: " + lowest["code"] + "\n"
    information = information + "Percentage: " + str(lowest["percentage"]) + "%\n"
    information = information + "Grade: " + lowest["grade"]
    
    messagebox.showinfo("Lowest Mark", information)






# This is a function student information off of the program
def deleteastudentid():
    students = studentinfo()
    if len(students) == 0:
        messagebox.showinfo("Error",
                            "No students found")
        return
    # This asks the user for the code of the student they'd like to delete of the system
    code = simpledialog.askstring("Delete",
                                  "Enter student code to delete:")

    if code == None:
        return
    
    new_list = []
    found = False
    
    for s in students:
        if s["code"] != code:
            # If the code given does not match its still kept in the list
            
            new_list.append(s)
        else:
            found = True
    
    if not found:
        messagebox.showinfo("Error",
                            "Student not found")
        return
    # If it is then the student information is deleted and a message box displays that
    studentsback(new_list)
    messagebox.showinfo("Success",
                        "Student deleted")
    updatethedisplay()

# This is the function that adds a new student, and their information
def addanewstudent():
    students = studentinfo()
    
    code = simpledialog.askstring("Input", "Enter student code:")
    if code == None:
        return
    # This prompts the user to add a desired student code
    name = simpledialog.askstring("Input", "Enter student name:")
    if name == None:
        return
    # And the name
    mark1 = simpledialog.askinteger("Input", "Enter coursework mark 1 (0-20):")
    if mark1 == None or mark1 < 0 or mark1 > 20:
        messagebox.showerror("Error", "Invalid mark")
        return
    # this is where they add the 3 coursework marks
    mark2 = simpledialog.askinteger("Input", "Enter coursework mark 2 (0-20):")
    if mark2 == None or mark2 < 0 or mark2 > 20:
        messagebox.showerror("Error", "Invalid mark")
        return
    
    mark3 = simpledialog.askinteger("Input", "Enter coursework mark 3 (0-20):")
    if mark3 == None or mark3 < 0 or mark3 > 20:
        messagebox.showerror("Error", "Invalid mark")
        return
    # As well as the exam mark
    exam = simpledialog.askinteger("Input", "Enter exam mark (0-100):")
    if exam == None or exam < 0 or exam > 100:
        messagebox.showerror("Error", "Invalid exam mark")
        return
    
    coursework = mark1 + mark2 + mark3
    total = coursework + exam
    percentage = round((total / 160) * 100, 2)
    grade = getthegrade(percentage)
    # This is where the information given is calculated and stored
    newstudentinfo = {}
    newstudentinfo["code"] = code
    newstudentinfo["name"] = name
    newstudentinfo["mark1"] = mark1
    newstudentinfo["mark2"] = mark2
    newstudentinfo["mark3"] = mark3
    newstudentinfo["exam"] = exam
    newstudentinfo["coursework"] = coursework
    newstudentinfo["percentage"] = percentage
    newstudentinfo["grade"] = grade
    # Just as the program has stored previous information
    students.append(newstudentinfo)
    studentsback(students)
    messagebox.showinfo("Success",
                        "Student added successfully")
    # This is the popup that is shown after the desired information is added
    updatethedisplay()
# The code is updated with the new information over here



# This is a function to update a student record 
def updateastudentid():
    students = studentinfo()
    if len(students) == 0:
        messagebox.showinfo("Error",
                            "No students found")
        return
    
    code = simpledialog.askstring("Update",
                                  "Enter student code:")
    if code == None:
        return
    
    target = None
    for s in students:
        if s["code"] == code:
            target = s
            break
    
    if target == None:
        messagebox.showinfo("Error",
                            "Student not found")
        return
    # If the student code doesnt match a error box is shown to warn the user
    field = simpledialog.askstring("Update", "What Would you like to update? (name/mark1/mark2/mark3/exam)")
    if field == None:
        return
    # If the code does match then it asks the user what they would like to update from the 
    # given options
    field = field.lower()
    
    
    # this conditional chain is used to add in the updated information that the user inputs
    if field == "name":
        new_name = simpledialog.askstring("Input", "Enter new name:")
        if new_name != None:
            target["name"] = new_name
    elif field == "mark1":
        newstudentmark = simpledialog.askinteger("Input", "Enter new mark (0-20):")
        if newstudentmark != None and newstudentmark >= 0 and newstudentmark <= 20:
            target["mark1"] = newstudentmark
        else:
            messagebox.showerror("Error", "Invalid mark")
            return
    elif field == "mark2":
        newstudentmark = simpledialog.askinteger("Input", "Enter new mark (0-20):")
        if newstudentmark != None and newstudentmark >= 0 and newstudentmark <= 20:
            target["mark2"] = newstudentmark
        else:
            messagebox.showerror("Error", "Invalid mark")
            return
    elif field == "mark3":
        newstudentmark = simpledialog.askinteger("Input", "Enter new mark (0-20):")
        if newstudentmark != None and newstudentmark >= 0 and newstudentmark <= 20:
            target["mark3"] = newstudentmark
        else:
            messagebox.showerror("Error", "Invalid mark")
            return
    elif field == "exam":
        newexammark = simpledialog.askinteger("Input", "Enter new exam mark (0-100):")
        if newexammark != None and newexammark >= 0 and newexammark <= 100:
            target["exam"] = newexammark
        else:
            messagebox.showerror("Error", "Invalid mark")
            return
    else:
        messagebox.showerror("Error", "Invalid field")
        return
    
    # New information is added and message boxes are shown if the input is invalid
    
    
    
    # After the information is updated this recalculates the involved calculations
    # regarding the numbers, total, and the percentage
    target["coursework"] = target["mark1"] + target["mark2"] + target["mark3"]
    total = target["coursework"] + target["exam"]
    target["percentage"] = round((total / 160) * 100, 2)
    target["grade"] = getthegrade(target["percentage"])
    
    studentsback(students)
    messagebox.showinfo("Success",
                        "Student updated")
    updatethedisplay()

# This is a function to sort the student information in ascending or descending order
def sortallinfo():
    students = studentinfo()
    if len(students) == 0:
        messagebox.showinfo("Error",
                            "No students found")
        return
    # This asks the user whether they want to view the list in ascending or descending order
    order = simpledialog.askstring("Sort",
                                   "Enter 'asc' or 'desc':")
    if order == None:
        return
    
    order = order.lower()
    # If its anything other an asc or desc then the input is invalid and the messagebox shows that
    if order != "asc" and order != "desc":
        messagebox.showerror("Error", "Invalid input, Please enter 'asc' or 'desc' ")
        return
    
    
# This is the pop up that showcases the list chosen by the user 
    for i in range(len(students)):
        for j in range(len(students) - 1):
            if order == "asc":
                if students[j]["percentage"] > students[j + 1]["percentage"]:
                    temp = students[j]
                    students[j] = students[j + 1]
                    students[j + 1] = temp
                    # the if statement shows the ascending list and
                    # the else statement shows the descending list
            else:
                if students[j]["percentage"] < students[j + 1]["percentage"]:
                    temp = students[j]
                    students[j] = students[j + 1]
                    students[j + 1] = temp
    
    text = ""
    for s in students:
        text = text + "Name: " + s["name"] + "\n"
        text = text + "Percentage: " + str(s["percentage"]) + "%\n"
        text = text + "Grade: " + s["grade"] + "\n\n"
    
    messagebox.showinfo("Sorted Students", text)



# This is to refresh the display with the updated information shown in the display
def updatethedisplay():
    students = studentinfo()
    
    displaythestudentinfo.config(state="normal")
    displaythestudentinfo.delete("1.0", tk.END)


# For the grades they are shown in specific colors
    displaythestudentinfo.tag_configure("Agrade",
                                  foreground="green")
    displaythestudentinfo.tag_configure("Bgrade",
                                  foreground="orange")
    displaythestudentinfo.tag_configure("Cgrade",
                                  foreground="red")
    
    if len(students) == 0:
        displaythestudentinfo.insert("1.0", "No students in the system yet")
    else:
        total_percent = 0
        
        for s in students:
            displaythestudentinfo.insert(tk.END,
                                   "Name: " + s["name"] + "\n")
            displaythestudentinfo.insert(tk.END,
                                   "Code: " + s["code"] + "\n")
            displaythestudentinfo.insert(tk.END,
                                   "Coursework: " + str(s["coursework"]) + "\n")
            displaythestudentinfo.insert(tk.END,
                                   "Exam: " + str(s["exam"]) + "\n")
            

            # This changes the color of the text according to the results of the student
            perctext = f"Percentage: {s['percentage']}%\n\n"
            gradetext = f"Grade: {s['grade']}\n\n"
            
            if s["grade"] in ["A"]:
                tag = "Agrade"
            elif s["grade"] == ["B", "C"]:
                tag = "Bgrade"
            else:
                tag = "Cgrade"
            
            displaythestudentinfo.insert(tk.END, perctext, tag)
            displaythestudentinfo.insert(tk.END, gradetext, tag)
            
            total_percent += s["percentage"]
        
        avg = round(total_percent / len(students), 2)
        displaythestudentinfo.insert(tk.END, f"Total Students: {len(students)}\n")
        displaythestudentinfo.insert(tk.END, f"Average Percentage of Students: {avg}%\n")
    
    displaythestudentinfo.config(state="disabled")

checkthefile()


root.title("Student Marks Manager - By Aneeka Rehman")
root.geometry("1100x800")
# This is the name and size of the application


# This is the container of the information
container = Frame(root)
container.pack(fill="both",
               expand=True,
               padx=10,
               pady=5)



# this is to shift the display to the left
left = Frame(container)
left.pack(side="left",
          fill="both",
          expand=True,
          padx=(0, 5))

# This is the title showen in the application
title = tk.Label(root,
                 text="Student Marks System",
                 font=("Arial", 19,
                 "bold"))
title.pack(pady=10)


displaylabel = tk.Label(left,
                         text="Student Records",
                         font=("Arial",
                         22,
                        "bold"))
displaylabel.pack(pady=5)

frameoftext = Frame(left)
frameoftext.pack(fill="both", expand=True)
# This is the scrollbar of the left frame
scroll = Scrollbar(frameoftext)
scroll.pack(side="right", fill="y")

displaythestudentinfo = tk.Text(frameoftext,
                          wrap="word",
                          yscrollcommand=scroll.set,
                          font=("Courier",
                          16))
displaythestudentinfo.pack(side="left", fill="both", expand=True)
scroll.config(command=displaythestudentinfo.yview)

# This is the refresh button at the bottom of the page
refreshbutton = tk.Button(left, text="refresh display ↪", command=updatethedisplay, width=20, font=("Arial", 13, "bold"))
refreshbutton.pack(pady=5)

# The buttons are placed on the rightside
right = Frame(container, width=250)
right.pack(side="right", fill="y", padx=(5, 0))

buttonslabel = tk.Label(right, text="Options", font=("Arial", 19, "bold"))
buttonslabel.pack(pady=10)
# This is the title of the button section on the right


# These are all the buttons;

# This is the view button
viewbutton = tk.Button(right, text="Individual Student 📝", command=viewa_spec_student, width=25, height=2, font=("Arial", 19, "bold"))
viewbutton.pack(pady=5)

# This is the highest mark button
highestmark = tk.Button(right, text="Highest Mark ✅", command=showhighestachiever, width=25, height=2, font=("Arial", 19, "bold"), bg="#4CAF50")
highestmark.pack(pady=5)

# This is the lowest mark button
lowestmark = tk.Button(right, text="Lowest Mark ❌", command=showlowestmark, width=25, height=2, font=("Arial", 19, "bold"))
lowestmark.pack(pady=5)

# This is the sort students button
sortstudentsbutton = tk.Button(right, text="Sort Pupils 📤", command=sortallinfo, width=25, height=2, font=("Arial", 19, "bold"))
sortstudentsbutton.pack(pady=5)


# This is the add new student button
addthestudents = tk.Button(right, text="Add new Student 📌", command=addanewstudent, width=25, height=2, font=("Arial", 19, "bold"))
addthestudents.pack(pady=5)

# This is the update button
updatebutton = tk.Button(right, text="Update Student Info ➡️", command=updateastudentid, width=25, height=2, font=("Arial", 19, "bold"))
updatebutton.pack(pady=5)

# This is the delete student button
deletebutton = tk.Button(right, text="Delete 🚫", command=deleteastudentid, width=25, height=2, font=("Arial", 19, "bold"))
deletebutton.pack(pady=5)

# This is the exit button that closes the application
exitbutton = tk.Button(right, text="Exit 🔚", command=root.quit, width=25, height=7, font=("Arial", 25, "bold"),)
exitbutton.pack(pady=120)

# Load the students when program starts
updatethedisplay()

root.mainloop()