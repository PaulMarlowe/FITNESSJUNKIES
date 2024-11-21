import tkinter as tk
window = tk. Tk()
window.title("Fitness Junkies")
window.geometry("900x600")
frame1 = tk.Frame(window, width = 100, height=50)
frame1.pack()
label1 = tk.Label(master=frame1, text="frame one")
label1.pack()
window.mainloop()
