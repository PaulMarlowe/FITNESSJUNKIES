import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Fitness Junkies")
window.geometry("900x600")

# Create a frame
frame = tk.Frame(window, width=600, height=400)
frame.pack(padx=10, pady=10, anchor="w")  # Anchor the frame to the left

def on_button_click(muscle_group):
    print(f"Selected muscle group: {muscle_group}")

# List of muscle groups
muscle_groups = ["Arms", "Legs", "Chest", "Back", "Abs"]

# Create buttons for each muscle group
for group in muscle_groups:
    btn = tk.Button(
        frame,
        text=group,
        width=20,  # Increase button width
        height=2,  # Increase button height
        font=("Arial", 14),  # Larger font for better visibility
        command=lambda g=group: on_button_click(g)
    )
    btn.pack(anchor="w", padx=20, pady=10)  # Align to the left with spacing

window.mainloop()


#lifitng app
#separate muscles into groups:
   #arms
   #shoulders
   #back
   #chest
   #core
   #legs
#pick which muscles they want to target
#choose how many days you work out a week: 2, 3, 4, 5, 6

#input hypertrophy...increasing weight and lower reps
#include reps and sets for 

#three mainpoints
   #tkinter window for choosing muscle group
   #user input
   #learning to storing user input info could be a new main point. We could also create a plot

#arms
   #rope extentions
   #tricep dips
   #preacher curls
   #barbell curls
   
#back
   #rows
   #lat pull downs
   #reverse flys 

#shoulder
   #overhead press
   #lateral raises
   #face pulls

#chest
   #bench press
   #pec flys
   #push-ups

#legs
   #hamstring curls
   #back squat
   #calf raises
   #leg press
   #legs extensions


#functions that we would need: 
   #class with methods that 




