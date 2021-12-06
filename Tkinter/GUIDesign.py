import tkinter as tk

user_pass = ""

# Debug method
def test_my_button():
  user_pass = ent_pass.get()
  lbl_pass_display = tk.Label(frame_auth, text="User password is: " + user_pass, font="Courier")
  lbl_pass_display.pack()
  frame_auth.tkraise()

# Main window
root = tk.Tk()
root.wm_geometry("400x200")

# Login frame
frame_login = tk.Frame(root)
frame_login.grid(row=0, column=0, sticky="news")

# Text labels
lbl_username = tk.Label(frame_login, text='Username:',font="Courier")
lbl_username.pack()
lbl_pass = tk.Label(frame_login,text="Password:",font="Courier")
lbl_pass.pack()

# Input boxes
ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(pady=5)
ent_pass = tk.Entry(frame_login, bd=3)
ent_pass.pack(pady=10)

# Buttons
btn_login = tk.Button(frame_login, text="Login", command=test_my_button)
btn_login.pack()

# Auth frame
frame_auth = tk.Frame(root)
frame_auth.grid(row=0, column=0, sticky="news")

# Display the user's password

frame_login.tkraise()

root.mainloop()
