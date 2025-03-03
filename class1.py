from tkinter import *

# A Widget is an object with a specific information or function

# Creating the main window widget
root = Tk()

#########################
######## Methods ########
#########################

def on_click():
    #label = Label(root, text="Click, Click, Click")
    #label.grid(row=0, column=0)
    comment = item.get()
    label = Label(root, text=comment).grid(row=0,column=0)

def rbutton(value):
    label3 = Label(root, text=radioVar.get())
    label3.grid(row=5,column=0)


#########################
######## Widgets ########
#########################
# Create a widget to display in our root.

label = Label(root, text="Hello World").grid(row=0,column=0)
label2 = Label(root, text="This is CSCI 3340").grid(row=1,column=0)
button = Button(root, text="Click Here", command=on_click).grid(row=2,column=0)
item = Entry(root) # Method Concatination
item.insert(0,"Type your favorite pie")

#drop down menu setup
dropVar = StringVar()
dropVar.set("Choose a Pie")
dropMenu = OptionMenu(root,dropVar, "Keylime", "Apple", "Pumpkin", "Blueberry")

#Radio BUtton Setup
radioVar = IntVar()
#radioVar = StringVar()
options = ["Option1","Option2","Option3"]
for i in range(len(options)):
    Radiobutton(root, text=options[i], variable=radioVar, value=i, command=lambda:rbutton(radioVar.get())).grid(row=4,column=i)



# Packing widgets in the root
#label.pack()

# Using grids to create a window instead of package
item.grid(row=3,column=0)
dropMenu.grid(row=6,column=0)


# Call the main loop for displaying the root window
root.mainloop()
