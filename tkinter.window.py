import tkinter as tk
#this sets up the main application window 
window = tk. Tk()
window.title("Fitness Junkies")
window.geometry("900x600")
#this is the frame that holds the button 
frame = tk.Frame(window, width = 600, height=400)
frame.pack(fill="both", expand=True, padx=10, pady=10)

#list of pull exercises
pull_exercises = [
    "1. Pull-ups",
    "2. Bent-over Rows",
    "3. Deadlifts",
    "4. Barbell Curls",
    "5. Face Pulls",
    "6. Lat Pull-downs" 
]

#function to show exercises in window
def show_exercises(exercises):
    #if there is any other list of exercises in the window, we are clearing them with this if statement
    for widget in frame.winfo_children():
        if isinstance(widget, tk.Label) or isinstance(widget, tk.Text):
            widget.destroy()
#this creates a label for each exercise of pull day
    for exercise in exercises:
        exercise_label = tk.Label(frame, text=exercise)
        exercise_label.pack(anchor="w", padx=10, pady=2)



#callback function that is called when the muscle_buttons button is clicked
def on_button_click(group):
    print(f"You clicked on: {group}")
#make button for muscle group disappear when clicked
    for btn in muscle_buttons:
        btn.pack_forget()

#this brings us to a choice for the user to choose either push or pull for "Arms"
    if group == "Arms":
        push_button = tk.Button(frame, text = "push day", width=15, command=lambda: print("You chose push day for arms!"))
        push_button.pack(anchor="w", padx=10, pady=5)
    if group == "Arms":
        pull_button = tk.Button(frame, text = "pull-day", width=15, command=lambda: print("You chose pull day for arms!"))
        pull_button.pack(anchor="w", padx=10, pady=5)  

#this brings us to a choice for the user to choose either glutes/hamstrings or quads/calves for "Legs"
    if group == "Legs":
        gh_button = tk.Button(frame, text = "glutes and hamstrings", width=15, command=lambda: print("You chose to work on your glutes and hamstrings!"))
        gh_button.pack(anchor="w", padx=10, pady=5)
    if group == "Legs":
        qc_button = tk.Button(frame, text = "quads and calves", width=15, command=lambda: print("You chose to work on your quads and calves!"))
        qc_button.pack(anchor="w", padx=10, pady=5)  

    elif group in ["Arms"]:
        # Display pull day exercises when Back or Legs is selected
            show_exercises(pull_exercises)
            instruction_label = tk.Label(frame, text="Pull Exercises for your workout:")
            instruction_label.pack(anchor="w", padx=10, pady=5)

#this is a list of muscle groups 
muscle_groups = ["Arms", "Legs", "Abs"]

#this creates an empty list for the muscle groups to disappear 
muscle_buttons = []

#this creates a button for each muscle group and stores them in a list 
for group in muscle_groups:
    btn = tk.Button(frame, text=group, width=15, command=lambda g=group: on_button_click(g))  
    btn.pack(anchor="w", padx=10, pady=20)
    muscle_buttons.append(btn) #stores the button in the list so we can access it later 




window.mainloop()
