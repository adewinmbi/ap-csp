# An external file called "scores.txt" is created when needed and used to store user scores

import tkinter as tk # This standard python module was imported and used under the Python Software Foundation License
import random # This standard python module was imported and used under the Python Software Foundation License

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

    # Display score analysis
    analysis = analyze_scores(load_scores(), current_score)
    lbl_results.config(text="You got a " + str(current_score) + "/10!\n" + analysis, font=("Courier"))
    
    # Reset test values
    current_letter = ""
    current_score = 0
    font_size = 55

def view_old_scores():
    display_text = ""

    # Append average to display to user
    analyze_old_scores(load_scores())
    display_text += "Average score: " + str(round(average, 1)) + "\n"

    index = 0
    for s in load_scores():
        display_text += "Test " + str(index) + " Score: " + str(s) + "\n"
        index += 1

    lbl_old_scores.config(text=display_text)
    frame_scores.tkraise()


def submit_ans():
    global current_score
    global level

    if (inp_answer.get() == current_letter or inp_answer.get() == current_letter.lower()): # If the answer is correct, increase the current score
        current_score += 1
    generate_letter()

    level += 1
    if (level >= 10): # Display 10 letters during one test
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

# Load past scores from a text file and return a list containing scores
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

# Return an analysis of the scores provided as parameters
def analyze_scores(score_list, new_score):
    global average
    average = 0
    sum = 0

    for score in score_list:
        sum += int(score)
    average = sum / len(score_list)

    if (new_score < average):
        return "Your vision score decreased and your new average is " + str(round(average, 1)) + ". Consider visiting an optometrist to improve your eyesight!"
    elif (new_score > average):
        return "Your vision score improved and your new average is " + str(round(average, 1)) + "! Great job maintaining healthy habits!"
    elif (new_score == average):
        return "Your vision score remained the same as an average of " + str(round(average, 1)) + ". Remember to book yearly checkups!"
    
# Analyze old scores without comparing to a new score
def analyze_old_scores(user_scores):
    global average
    average = 0
    sum = 0

    for score in user_scores:
        sum += int(score)
    average = sum / len(user_scores)

# ===== User Interface =====

# Create main window
root = tk.Tk("Vision Test")
root.configure(bg="light blue")
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
lbl_instructions = tk.Label(frame_main, text="Begin a new test or view old vision scores!", font=("Courier", 20), wraplength=700, justify="center", pady=10)
lbl_instructions.pack()

lbl_test_instructions = tk.Label(frame_test, text="Place the device 14 inches (36.6 cm) away from your face.\nIn the input box below, enter the letter you think you are reading.", font="Courier", wraplength=700, pady=20)
lbl_test_instructions.pack()

lbl_results = tk.Label(frame_end, text="", font=("Courier", font_size), wraplength=700, justify="left")
lbl_results.pack()

lbl_old_scores = tk.Label(frame_scores, text="", font="Courier", wraplength=700, justify="left")
lbl_old_scores.pack()

# Input boxes
inp_answer = tk.Entry(frame_test)
inp_answer.pack()

# Buttons
btn_new_test = tk.Button(frame_main, text="Begin New Test", font=("Courier", 15), command=new_test)
btn_new_test.pack()

btn_old_scores = tk.Button(frame_main, text="View Old Scores", font=("Courier", 15), command=view_old_scores)
btn_old_scores.pack()

btn_submit = tk.Button(frame_test, text="Submit Answer", font=("Courier", 15), command=submit_ans)
btn_submit.pack()

btn_restart_test = tk.Button(frame_end, text="Main Menu", font=("Courier", 15), command=return_to_menu)
btn_restart_test.pack()

btn_back = tk.Button(frame_scores, text="Return to Menu", font=("Courier", 15), command=return_to_menu)
btn_back.pack(side=tk.RIGHT)

# Letter text label
lbl_letter = tk.Label(frame_test, text="", font=("Courier", font_size), wraplength=700, justify="left")
lbl_letter.pack()

frame_main.tkraise()
root.mainloop()
