# Brianna Adewinmbi and Kyle Huang

# p227_starter_one_button_shell.py
import subprocess
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename

def do_command(command):
  global command_textbox, url_entry

  # If url_entry is blank, use localhost IP address 
  url_val = url_entry.get()
  if (len(url_val) == 0):
      url_val = "localhost"

  command.append(url_val)

  # Change commands for unix-like systems
  if subprocess.os.name == "posix":
    if command[0] == "ping":
      command.insert(1, "-c")
      command.insert(2, "2")
    if command[0] == "tracert":
      command[0] = "traceroute"
      command[1] = "-m"

  # Print to textbox
  command_textbox.delete(1.0, tk.END)
  command_textbox.insert(tk.END, " ".join(command) + " working....\n")
  command_textbox.update()

  output = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

  command_textbox.insert(tk.END, output.stdout)
  
# Save function.
def mSave():
  filename = asksaveasfilename(defaultextension='.txt',filetypes = (('Text files', '*.txt'),('Python files', '*.py *.pyw'),('All files', '*.*')))
  if filename is None:
    return
  with open(filename, mode="w") as file:
    file.write(command_textbox.get("1.0", tk.END))

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

# Makes the command button pass it's name to a function using lambda
ping_btn = tk.Button(frame, text="Ping", command=lambda:do_command(["ping"]))
ping_btn.pack()

# tracert
tracert_btn = tk.Button(frame, text="Traceroute",
command=lambda:do_command(["tracert", "-h", "10"]))
tracert_btn.pack()

# nslookup
nslookup_btn = tk.Button(frame, text="Name server lookup", command=lambda:do_command(["nslookup"]))
nslookup_btn.pack()

# Makes the command button pass it's name to a function using lambda
ping_btn = tk.Button(frame, text="Check to see if a URL is up and active", command=lambda:do_command(["ping"]))
ping_btn.pack()

# creates the frame with label for the text box
frame_URL = tk.Frame(root, pady=10,  bg="black") # change frame color
frame_URL.pack()

# decorative label
url_label = tk.Label(frame_URL, text="Enter a URL of interest: ", 
  compound="center",
  font=("comic sans", 14),
  bd=0, 
  relief=tk.FLAT, 
  cursor="heart",
  fg="mediumpurple3",
  bg="black")
url_label.pack(side=tk.LEFT)
url_entry= tk.Entry(frame_URL,  font=("comic sans", 14)) # change font
url_entry.pack(side=tk.LEFT)

frame = tk.Frame(root,  bg="black") # change frame color
frame.pack()

# Adds an output box to GUI.
command_textbox = tksc.ScrolledText(frame, height=10, width=100)
command_textbox.pack()

# Create save button
save_btn = tk.Button(frame, text="Save", command=mSave, bg="blue")
save_btn.pack()

root.mainloop()
