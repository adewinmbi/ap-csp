import tkinter as tk
import random

# options
# take new test
# - Displays largest size letter
# - if answer is correct, displays smaller letter
# - else, calculate score out of 20 (only show 10 letters, but multiply by 2)
# view old test scores

# TODO: Make sure the method I want to be graded is at the top

user_scores = []
largest_font = 50
# 65 = A, 90 = Z

def new_test():
    frame_test.tkraise()


# ===== Save/Load User Scores =====

with open('readme.txt', 'w') as f:
    f.write('readme')



# ===== User Interface =====

# Create main window
root = tk.Tk()
root.wm_geometry("800x500")

# Create frames
frame_main = tk.Frame(root)
frame_main.grid(row=0, column=0, sticky="news")

frame_test = tk.Frame(root)
frame_test.grid(row=0, column=0, sticky="news")

# Text labels
lbl_instructions = tk.Label(frame_main, text="Begin a new test or view old vision scores!", font="Courier")
lbl_instructions.pack()

lbl_letter = tk.Label(frame_test, text="A", font=("Courier", largest_font))
lbl_letter.pack()

# Buttons
btn_new_test = tk.Button(frame_main, text="New Test", command=new_test)
btn_new_test.pack()

frame_main.tkraise()
root.mainloop()

# # Text labels
# lbl_username = tk.Label(frame_main_login, text='Username:',font="Courier")
# lbl_username.pack()
# lbl_pass = tk.Label(frame_main_login,text="Password:",font="Courier")
# lbl_pass.pack()

# # Input boxes
# ent_username = tk.Entry(frame_main_login, bd=3)
# ent_username.pack(pady=5)
# ent_pass = tk.Entry(frame_main_login, bd=3)
# ent_pass.pack(pady=10)

# # Buttons
# btn_login = tk.Button(frame_main_login, text="Login", command=test_my_button)
# btn_login.pack()