from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tkboot


root = tkboot.Window(themename="superhero")

root.title("Calculator")
root.geometry("500x350")

# Create function
# counter = 0
# def changer():
#     counter += 1
#     if counter % 2 == 0:



# Create Label
my_label = tkboot.Label(
    text="Namaste Python", font=("Helvetica", 12), bootstyle="info, inverse"
)
my_label.pack(pady=1)

# Create Button
# my_Button = tkboot.Button(text="Click Me", bootstyle="warning", COMMAND=changer)
# my_Button.pack()


root.mainloop()
