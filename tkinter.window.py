import tkinter as tk
window = tk. Tk()
window.title("Fitness Junkies")
window.geometry("900x600")

print("hi")




frame = tk.Frame(window, width = 600, height=400)
frame.pack(fill="both", expand=True, padx=10, pady=10)


def on_button_click():
    pass

muscle_groups = ["Arms", "Legs", "Chest", "Back", "Abs"]

for group in muscle_groups:
    btn = tk.Button(frame, text=group, width=15, command=lambda g=group: on_button_click(g))  
    btn.pack(anchor="w", padx=10, pady=20)

window.mainloop()
