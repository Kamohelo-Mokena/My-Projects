from tkinter import *

#create the main window
window = Tk() 
window.geometry('420x420')
window.title("My first GUI something")
window.config(background="#f3b986")

#create a label
label = Label(window,text="Google",bg="#f3d7b4",font=("Arial Black",28))
label.pack(pady=80) # add the label to the window and give it some vertical padding

#create a button
def on_button_click():
    label.config(text="Our button clicked!") #change the label text when button is clicked

#creating buttons
button = Button(window, text="Click Me!!", command=on_button_click)
button.pack(pady=50)

#adding window icon
icon = PhotoImage(file = 'roboforce.png')
window.iconphoto(True, icon)

#running the GUI loop
window.mainloop() 