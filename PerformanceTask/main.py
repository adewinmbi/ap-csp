from ctypes import alignment
import tkinter as tk
import random

# options
# take new test
# - Displays largest size letter
# - if answer is correct, displays smaller letter
# - else, calculate score out of 20 (only show 10 letters, but multiply by 2)
#   Try again:
#      - Reset take new test screen
# view old test scores
# - Shows average and past scores
# Ex.
#   Average = 5.4
#   Test 1 Score = 9
#   Test 2 Score = 4
#   Test 2 Score = 7

# TODO: Make sure the method I want to be graded is at the top

current_letter = ""
current_score = 0
level = 0
font_size = 55
average = 0

def new_test():
    frame_test.tkraise()
    generate_letter()

def end_test():
    global current_letter
    global current_score
    global font_size
    
    # Report score to user
    frame_end.tkraise()
    save_score(current_score)
    analysis = analyze_scores(load_scores(), current_score)
    lbl_results.config(text="You got a " + str(current_score) + "/10!\n" + analysis, font=("Courier")) # tell user if they got worse, better, have no previous scores, would like to try again, the score they just recieved
    
    # Reset test values
    current_letter = ""
    current_score = 0
    font_size = 55

def view_old_scores():
    display_text = ""

    # Append average to display to user
    analyze_scores(load_scores())
    display_text += "Average score: " + str(average) + "\n"

    index = 0
    for s in load_scores():
        display_text += "Test " + str(index) + " Score: " + str(s) + "\n"
        index += 1

    lbl_old_scores.config(text=display_text)
    frame_scores.tkraise()


def submit_ans():
    global current_score
    global level

    if (inp_answer.get() == current_letter or inp_answer.get() == current_letter.lower()):
        current_score += 1
    generate_letter()

    level += 1
    if (level >= 10): # REMOVE/FIX the test lasts 10 rounds
        level = 0
        end_test()

def generate_letter():
    global current_letter
    global font_size

    # Generate random number and convert to ASCII letter
    letter = chr(random.randint(65, 90))
    current_letter = letter

    # Decrease size of letter display
    font_size = font_size - 5
    lbl_letter.config(text=letter, font=("Courier", font_size))

def return_to_menu():
    frame_main.tkraise()

# ===== Manage User Scores =====

def load_scores():
    score_list = []

    with open('scores.txt', 'r') as f:
        score_list = f.read().split('\n')
        score_list.pop()

    return score_list

def save_score(score):
    with open('scores.txt', 'a') as f:
        f.write(str(score))
        f.write('\n')

def analyze_scores(user_scores, new_score):
    global average
    average = 0
    sum = 0

    for score in user_scores:
        sum += int(score)
    average = sum / len(user_scores)

    if (new_score < average):
        return "Your vision score decreased from your average of " + str(round(average, 1)) + ". Consider visiting an optometrist to improve your eyesight!"
    else:
        return "Your vision score improved from your average of " + str(round(average, 1)) + "! Great job staying healthy!"
    
def analyze_scores(user_scores):
    global average
    average = 0
    sum = 0

    for score in user_scores:
        sum += int(score)
    average = sum / len(user_scores)

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

frame_scores = tk.Frame(root)
frame_scores.grid(row=0, column=0, sticky="news")

# Text labels
lbl_instructions = tk.Label(frame_main, text="Begin a new test or view old vision scores!", font="Courier", wraplength=700, justify="left")
lbl_instructions.pack()

lbl_letter = tk.Label(frame_test, text="", font=("Courier", font_size), wraplength=700, justify="left")
lbl_letter.pack()

lbl_results = tk.Label(frame_end, text="", font=("Courier", font_size), wraplength=700, justify="left")
lbl_results.pack()

lbl_old_scores = tk.Label(frame_scores, text="", font="Courier", wraplength=700, justify="left")
lbl_old_scores.pack()

# Input boxes
inp_answer = tk.Entry(frame_test)
inp_answer.pack()

# Buttons
btn_new_test = tk.Button(frame_main, text="Begin New Test", command=new_test)
btn_new_test.pack()

btn_old_scores = tk.Button(frame_main, text="View Old Scores", command=view_old_scores)
btn_old_scores.pack()

btn_submit = tk.Button(frame_test, text="Submit Answer", command=submit_ans)
btn_submit.pack()

btn_restart_test = tk.Button(frame_end, text="Main Menu", command=return_to_menu)
btn_restart_test.pack()

btn_back = tk.Button(frame_scores, text="Return to Menu", command=return_to_menu)
btn_back.pack(side=tk.RIGHT)

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