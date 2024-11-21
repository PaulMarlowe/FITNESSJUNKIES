import tkinter as tk
window = tk. Tk()
window.title("Fitness Junkies")
window.geometry("900x600")




frame = tk.Frame(window, width = 600, height=400)
frame.pack()

def on_button_click():
    pass

muscle_groups = ["Arms", "Legs", "Chest", "Back", "Abs"]

for group in muscle_groups:
    btn = tk.Button(frame, text=group, width=15, command=lambda g=group: on_button_click(g))
    btn.pack(pady=5)  

window.mainloop()
