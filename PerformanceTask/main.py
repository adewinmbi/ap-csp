from os.path import exists
import tkinter as tk
import random

# options
# take new test
# - Displays largest size letter
# - if answer is correct, displays smaller letter
# - else, calculate score out of 20 (only show 10 letters, but multiply by 2)
# view old test scores

# TODO: Make sure the method I want to be graded is at the top

current_letter = ""
current_score = 0
round = 0

user_scores = []
font_size = 52
# 65 = A, 90 = Z

def new_test():
    frame_test.tkraise()
    generate_letter()

def end_round():
    # Save score in text file
    with open('scores.txt', 'a') as f:
        f.write(str(current_score))
        f.write('\n')

    # Report score to user
    frame_end.tkraise()
    # tell user if they got worse, better, have no previous scores, would like to try again, the score they just recieved
    lbl_results.config(text="You got a " + str(current_score) + "/10!")

def submit_ans():
    global current_score
    global round

    if (inp_answer.get() == current_letter or inp_answer.get() == current_letter.lower()):
        current_score += 1
    lbl_letter.config(text=generate_letter())

    round += 1
    print(round)
    if (round >= 10): # REMOVE/FIX the test lasts 10 rounds
        round = 0
        end_round()

    # print(current_score)

def generate_letter():
    global current_letter
    global font_size

    # Generate random number and convert to ASCII letter
    letter = chr(random.randint(65, 90))
    current_letter = letter

    # Decrease size of letter display
    font_size = font_size - 5
    lbl_letter.config(font=("Courier", font_size))

    return letter

# ===== Save/Load User Scores =====



# ===== User Interface ===== (maybe reorganize this so everything isnt just a block of texts)

# Create main window
root = tk.Tk()
root.wm_geometry("800x500")

# Create frames
frame_main = tk.Frame(root)
frame_main.grid(row=0, column=0, sticky="news")

frame_test = tk.Frame(root)
frame_test.grid(row=0, column=0, sticky="news")

frame_end = tk.Frame(root)
frame_end.grid(row=0, column=0, sticky="news")

# Text labels
lbl_instructions = tk.Label(frame_main, text="Begin a new test or view old vision scores!", font="Courier")
lbl_instructions.pack()

lbl_letter = tk.Label(frame_test, text="", font=("Courier", font_size))
lbl_letter.pack()

lbl_results = tk.Label(frame_end, text="", font=("Courier", font_size))
lbl_results.pack()

# Input boxes
inp_answer = tk.Entry(frame_test)
inp_answer.pack()

# Buttons
btn_new_test = tk.Button(frame_main, text="New Test", command=new_test)
btn_new_test.pack()

btn_submit = tk.Button(frame_test, text="Submit Answer", command=submit_ans)
btn_submit.pack()

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