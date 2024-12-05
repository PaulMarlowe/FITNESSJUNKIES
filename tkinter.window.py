import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
import json

# Alright, let’s get started by setting up the main application window!
window = tk.Tk()
window.title("Fitness Junkies")
window.geometry("900x600")
window.configure(bg="#e6f7ff")  # Let’s give the app a nice light blue background.

# Here’s where we’ll keep track of all the workouts you’ve scheduled.
scheduled_workouts = {}

# This is the main area where buttons and options will go.
frame = tk.Frame(window, bg="#e6f7ff")
frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

# Over here, we’ll show the workouts you’ve scheduled.
text_widget = tk.Text(window, width=40, height=20, bg="#ffffff", fg="#000000", wrap="word", state="disabled")
text_widget.grid(row=0, column=2, padx=10, pady=10, sticky="n")

# Let’s make sure we update the list of scheduled workouts whenever something changes.
def update_text_widget():
    text_widget.config(state="normal")  # Turn editing on for a second.
    text_widget.delete("1.0", tk.END)  # Clear out the old stuff.

    # Add either the list of workouts or a friendly message if there’s nothing yet.
    if scheduled_workouts:
        text_widget.insert(tk.END, "Scheduled Workouts:\n\n")
        for date, workout in scheduled_workouts.items():
            text_widget.insert(tk.END, f"{date}: {workout}\n")
    else:
        text_widget.insert(tk.END, "No workouts scheduled yet.")
    
    text_widget.config(state="disabled")  # Turn editing back off to keep it safe.

# If you ever want to go back to the main menu, here’s how we handle it!
def back_to_start():
    for widget in frame.winfo_children():
        widget.destroy()
    add_main_buttons()  # Bring back the main buttons.
    update_text_widget()  # Refresh the workout list.

# Here’s where we let you pick a date and set a workout.
def open_calendar():
    def schedule_workout():
        selected_date = cal.get_date()
        workout = workout_entry.get()
        if selected_date and workout:
            # Add your new workout to the schedule and save it.
            scheduled_workouts[selected_date] = workout
            save_workouts()
            result_label.config(text=f"Workout scheduled for {selected_date}: {workout}", fg="green")
            update_text_widget()
        else:
            result_label.config(text="Please select a date and enter a workout.", fg="red")

    # Pop open a calendar window for scheduling!
    calendar_window = tk.Toplevel(window)
    calendar_window.title("Schedule Workout")
    calendar_window.geometry("400x400")
    calendar_window.configure(bg="#fff9e6")  # A soft cream background feels inviting.

    cal = Calendar(calendar_window, selectmode="day", background="#e6f7ff", foreground="black")
    cal.pack(pady=10)

    workout_entry = tk.Entry(calendar_window, width=40)
    workout_entry.pack(pady=5)

    schedule_button = tk.Button(calendar_window, text="Schedule Workout", command=schedule_workout, bg="#004d80", fg="white", activebackground="#006699")
    schedule_button.pack(pady=5)

    result_label = tk.Label(calendar_window, text="", bg="#fff9e6")
    result_label.pack(pady=5)

# Save all your workouts to a file so we don’t lose them.
def save_workouts():
    with open("workout_schedule.json", "w") as file:
        json.dump(scheduled_workouts, file, indent=4)

# Let’s load the workouts from the file when you start the app.
def load_workouts():
    global scheduled_workouts
    try:
        with open("workout_schedule.json", "r") as file:
            scheduled_workouts = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        # If there’s no file or it’s empty, we’ll just start fresh.
        scheduled_workouts = {}

# If you want to clear all the scheduled workouts, here’s how we do it.
def clear_schedule():
    global scheduled_workouts
    scheduled_workouts = {}  # Bye-bye, workouts!
    save_workouts()
    update_text_widget()

# Show a list of exercises for the selected group.
def show_exercises(exercises):
    for widget in frame.winfo_children():
        widget.destroy()

    # Let’s show the exercises in a neat, numbered list.
    header = tk.Label(frame, text="Exercises", font=("Arial", 18, "bold"), bg="#e6f7ff", fg="#004d80")
    header.grid(row=0, column=0, columnspan=2, sticky="w", padx=10, pady=10)

    for i, exercise in enumerate(exercises, start=1):
        exercise_label = tk.Label(frame, text=f"{i}. {exercise}", font=("Arial", 12), bg="#e6f7ff", fg="black")
        exercise_label.grid(row=i, column=0, sticky="w", padx=20, pady=5)

    # Add a "Back" button to let you return to the main menu.
    back_button = tk.Button(frame, text="Back", command=back_to_start, bg="#004d80", fg="white", activebackground="#006699")
    back_button.grid(row=len(exercises) + 1, column=0, padx=10, pady=10)

    # Add the "Schedule Workout" button to the right of the exercises.
    schedule_button = tk.Button(frame, text="Schedule Workout", command=open_calendar, bg="#004d80", fg="white", activebackground="#006699")
    schedule_button.grid(row=1, column=1, rowspan=len(exercises), padx=10, pady=5, sticky="ns")

# Handle clicks on a muscle group button.
def on_button_click(group):
    for widget in frame.winfo_children():
        widget.destroy()

    if group == "Arms":
        # Give you options for Push or Pull days for arms.
        tk.Button(frame, text="Push Day", command=lambda: show_exercises([
            "Bench Press", "Incline Bench Press", "Dumbbell Shoulder Press",
            "Dumbbell Chest Fly", "Push-Ups", "Tricep Dips"
        ]), bg="#b3e6ff", fg="black").grid(row=0, column=0, padx=10, pady=10)
        tk.Button(frame, text="Pull Day", command=lambda: show_exercises([
            "Pull-ups", "Bent-over Rows", "Deadlifts", "Barbell Curls", 
            "Face Pulls", "Lat Pull-downs"
        ]), bg="#b3e6ff", fg="black").grid(row=1, column=0, padx=10, pady=10)
    elif group == "Legs":
        # Push or Pull day options for legs.
        tk.Button(frame, text="Push Day", command=lambda: show_exercises([
            "Barbell Squats", "Leg Press", "Lunges", "Leg Extensions", 
            "Calf Raises", "Box Jumps"
        ]), bg="#b3e6ff", fg="black").grid(row=0, column=0, padx=10, pady=10)
        tk.Button(frame, text="Pull Day", command=lambda: show_exercises([
            "Barbell Deadlift", "Romanian Deadlift", "Glute Bridge", 
            "Hip Thrust", "Lunges", "Step-Ups"
        ]), bg="#b3e6ff", fg="black").grid(row=1, column=0, padx=10, pady=10)
    elif group == "Abs":
        # Show abs workouts right away.
        show_exercises([
            "Crunches", "Plank Holds", "Leg Raises", "Russian Twists", 
            "Bicycle Crunches", "Mountain Climbers"
        ])

# Add buttons for each muscle group to the main menu.
def add_main_buttons():
    header = tk.Label(frame, text="Select a Muscle Group:", font=("Arial", 18, "bold"), bg="#e6f7ff", fg="#004d80")
    header.grid(row=0, column=0, columnspan=2, pady=10)

    muscle_groups = ["Arms", "Legs", "Abs"]
    for i, group in enumerate(muscle_groups):
        tk.Button(frame, text=group, command=lambda g=group: on_button_click(g), bg="#b3e6ff", fg="black", activebackground="#80d4ff").grid(row=i + 1, column=0, padx=20, pady=10)

    # Add a button to clear all the scheduled workouts.
    tk.Button(frame, text="Clear Schedule", command=clear_schedule, bg="#004d80", fg="white", activebackground="#006699").grid(row=len(muscle_groups) + 1, column=0, padx=20, pady=10)

# Load saved workouts and display the UI when the app starts.
load_workouts()
add_main_buttons()
update_text_widget()

window.mainloop()
