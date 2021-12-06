import tkinter as tk

# Main window
root = tk.Tk()
root.wm_geometry("400x200")

colors = ["blue", "lime", "red", "yellow"]
scale = 10

def draw_grid():
    color_index = 0
    for r in range(2):
        for c in range (2):

            # Change size of grid cells
            if c == 0:
                pad = 3
            else:
                pad = 1

            tk.Label(root, bg=colors[color_index], borderwidth=1, width=10*pad, height=10).grid(row=r, column=c, sticky="news")
            print("yea")
            color_index += 1


draw_grid()
root.mainloop()
