import tkinter as tk
from tkcalendar import Calendar
import json

# Initialize the main application window
window = tk.Tk()
window.title("Fitness Junkies")
window.geometry("900x600")

# This is the frame that holds the button
frame = tk.Frame(window, width=600, height=400)
frame.pack(fill="both", expand=True, padx=10, pady=10)

# Lists of exercises
pull_exercises = [
    "1. Pull-ups",
    "2. Bent-over Rows",
    "3. Deadlifts",
    "4. Barbell Curls",
    "5. Face Pulls",
    "6. Lat Pull-downs"
]

push_exercises = [
    "1. Bench Press",
    "2. Incline Bench Press",
    "3. Dumbbell Shoulder Press",
    "4. Dumbbell Chest Fly",
    "5. Push-Ups",
    "6. Tricep Dips"
]

gh_exercises = [
    "1. Barbell Deadlift",
    "2. Romanian Deadlift",
    "3. Glute Bridge",
    "4. Hip Thrust",
    "5. Lunges",
    "6. Step-Ups"
]

qc_exercises = [
    "1. Barbell Squats",
    "2. Leg Press",
    "3. Lunges",
    "4. Leg Extensions",
    "5. Calf Raises",
    "6. Box Jumps"
]

# Dictionary to store scheduled workouts
scheduled_workouts = {}

# Function to display scheduled workouts
def display_scheduled_workouts():
    for widget in frame.winfo_children():
        if isinstance(widget, tk.Label):
            widget.destroy()

    if scheduled_workouts:
        schedule_display = tk.Label(frame, text="Scheduled Workouts:", font=("Arial", 14))
        schedule_display.pack(anchor="w", padx=10, pady=5)

        for date, workout in scheduled_workouts.items():
            workout_label = tk.Label(frame, text=f"{date}: {workout}", font=("Arial", 12))
            workout_label.pack(anchor="w", padx=20, pady=2)
    else:
        no_schedule_label = tk.Label(frame, text="No workouts scheduled yet.", font=("Arial", 12))
        no_schedule_label.pack(anchor="w", padx=10, pady=5)

# Function to return to the starting UI
def back_to_start():
    global back_button
    # Clear current UI elements
    for widget in frame.winfo_children():
        widget.destroy()

    # Re-add muscle group buttons
    for group in muscle_groups:
        btn = tk.Button(frame, text=group, width=15, command=lambda g=group: on_button_click(g))
        btn.pack(anchor="w", padx=10, pady=20)
        muscle_buttons.append(btn)

    # Reset placeholders
    display_scheduled_workouts()

# Function to show the calendar for scheduling workouts
def open_calendar():
    def schedule_workout():
        selected_date = cal.get_date()
        workout = workout_entry.get()
        if selected_date and workout:
            scheduled_workouts[selected_date] = workout
            save_workouts()
            result_label.config(text=f"Workout scheduled for {selected_date}: {workout}")
            display_scheduled_workouts()  # Update the displayed workouts
        else:
            result_label.config(text="Please select a date and enter a workout.")

    # Create a top-level window for the calendar
    calendar_window = tk.Toplevel(window)
    calendar_window.title("Schedule Workout")

    # Add the calendar widget
    cal = Calendar(calendar_window, selectmode="day")
    cal.pack(pady=10)

    # Add a text entry for the workout
    workout_entry = tk.Entry(calendar_window, width=40)
    workout_entry.pack(pady=5)

    # Button to schedule the workout
    schedule_button = tk.Button(calendar_window, text="Schedule Workout", command=schedule_workout)
    schedule_button.pack(pady=5)

    # Label to show confirmation
    result_label = tk.Label(calendar_window, text="")
    result_label.pack(pady=5)

# Function to save workouts to a JSON file
def save_workouts():
    with open("workout_schedule.json", "w") as file:
        json.dump(scheduled_workouts, file)

# Function to load workouts from a JSON file
def load_workouts():
    global scheduled_workouts
    try:
        with open("workout_schedule.json", "r") as file:
            scheduled_workouts = json.load(file)
    except FileNotFoundError:
        scheduled_workouts = {}

# Function to clear all scheduled workouts
def clear_schedule():
    global scheduled_workouts
    scheduled_workouts = {}  # Clear the dictionary
    save_workouts()  # Save the empty dictionary to the JSON file
    display_scheduled_workouts()  # Update the displayed workouts

# Function to show exercises in the window
def show_exercises(exercises):
    for widget in frame.winfo_children():
        if isinstance(widget, tk.Label):
            widget.destroy()
    for exercise in exercises:
        exercise_label = tk.Label(frame, text=exercise)
        exercise_label.pack(anchor="w", padx=10, pady=2)

# Callback function when a muscle group button is clicked
def on_button_click(group):
    global back_button

    # Clear current buttons
    for widget in frame.winfo_children():
        widget.destroy()

    # Add specific buttons for the selected muscle group
    if group == "Arms":
        push_button = tk.Button(frame, text="Push Day", width=15, command=lambda: show_exercises(push_exercises))
        push_button.pack(anchor="w", padx=10, pady=5)
        pull_button = tk.Button(frame, text="Pull Day", width=15, command=lambda: show_exercises(pull_exercises))
        pull_button.pack(anchor="w", padx=10, pady=5)

    elif group == "Legs":
        gh_button = tk.Button(frame, text="Glutes and Hamstrings", width=15, command=lambda: show_exercises(gh_exercises))
        gh_button.pack(anchor="w", padx=10, pady=5)
        qc_button = tk.Button(frame, text="Quads and Calves", width=15, command=lambda: show_exercises(qc_exercises))
        qc_button.pack(anchor="w", padx=10, pady=5)

    # Add schedule workout button
    schedule_button = tk.Button(frame, text="Schedule Workout", width=20, command=open_calendar)
    schedule_button.pack(anchor="w", padx=10, pady=10)

    # Add back button
    back_button = tk.Button(frame, text="Back", width=20, command=back_to_start)
    back_button.pack(anchor="w", padx=10, pady=10)

# List of muscle groups
muscle_groups = ["Arms", "Legs", "Abs"]

# List of muscle group buttons
muscle_buttons = []

# Add muscle group buttons to the starting UI
for group in muscle_groups:
    btn = tk.Button(frame, text=group, width=15, command=lambda g=group: on_button_click(g))
    btn.pack(anchor="w", padx=10, pady=20)
    muscle_buttons.append(btn)

# Add the "Clear Schedule" button
clear_button = tk.Button(frame, text="Clear Schedule", width=20, command=clear_schedule)
clear_button.pack(anchor="w", padx=10, pady=10)

# Load saved workouts on startup
load_workouts()
display_scheduled_workouts()

# Run the main application
window.mainloop()

