import json
from datetime import date
# hardcoded workouts
WORKOUTS = {
    "Chest": ["Bench Press", "Incline Dumbbell Press", "Lateral Raises"],
    "Back": ["Lat Pulldown", "Seated Row", "Dumbbell Curl"],
    "Legs": ["Squats", "Romanian Deadlift", "Calf Raises"],
}

# save the workout history
def load_data(filename="WORKOUTS.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except(FileNotFoundError, json.JSONDecodeError):
        return {}
# save workout history as a JSON file
def save_data(data, filename="WORKOUTS.json"):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

# get the last session data
def get_last_session(data, day):
    sessions = data.get(day, [])
    if sessions:
        return sessions[-1]

    return None
# get a positive number
def get_positive_number(prompt):
    while True:
        try:
            number = float(input(prompt))
            if number > 0:
                return number
            print("Enter a number greater than zero!")
        except ValueError:
            print("Please enter a valid number!!")
# get a positive integer
def get_positive_integer(prompt):
    while True:
        try:
            number = int(input(prompt))
            if number > 0:
                return number
            print("Enter a whole number greater than zero!")
        except ValueError:
            print("Please enter a valid whole number!!")
# get the difficulty felt while exercising
def get_difficulty():
    while True:
        try:
            difficulty = int(input("Difficulty (1-10): "))
            if 1 <= difficulty <= 10:
                return difficulty
            print("Enter a number from 1 to 10")
        except ValueError:
            print("Please enter a whole number!")

# record a workout and save it
def start_workout(data):
    days = list(WORKOUTS.keys())

    print("\nChoose a workout day: ")
    for number, day in enumerate(days, start=1):
        print(f"{number}. {day}")

    choice = get_positive_integer("Choose a number: ")

    if choice > len(days):
        print("Invalid workout day!")
        return

    day = days[choice - 1]
    previous = get_last_session(data, day)

    print(f"\n--- {day} Workout ---")

    if previous:
        print(f"Previous session: {previous['date']}")
    else:
        print("This is your first recorded session for this day.")

    session = {
        "date": date.today().isoformat(),
        "exercises": {}
    }
    for exercise in WORKOUTS[day]:
        print(f"\n{exercise}")
        if previous and exercise in previous["exercises"]:
            old = previous["exercises"][exercise]
            print(
                f"Previous: {old['weight']} kg, "
                f"{old['sets']} sets x {old['reps']} reps, "
                f"difficulty {old['difficulty']}/10"
            )

        weight = get_positive_number("Weight (kg): ")
        sets = get_positive_integer("Number of sets: ")
        reps = get_positive_integer("Reps per set: ")
        difficulty = get_difficulty()

        session["exercises"][exercise] = {
            "weight": weight,
            "sets": sets,
            "reps": reps,
            "difficulty": difficulty
        }
    if day not in data:
        data[day] = []

    data[day].append(session)
    save_data(data)
    print ("\nWorkout saved successfully!")
# show recent sessions
def view_history(data):
    if not data:
        print("\nNo workout history found")
        return
    for day, sessions in data.items():
        print (f"\n=== {day} History ===")

        for session in sessions[-8:]:
            print(f"\nDate: {session['date']}")

            for exercise, details in session["exercises"].items():
                print(
                    f"{exercise}: {details['weight']} kg, "
                    f"{details['sets']} sets x {details['reps']} reps, "
                    f"difficulty {details['difficulty']}/10"
                )
def main():
    data = load_data()

    while True:
        print("\n=== Gym Workout Tracker ===")
        print("1. Start a workout")
        print("2. View workout history")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            start_workout(data)
        elif choice == "2":
            view_history(data)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choise. Choose 1, 2 or 3")



if __name__ == "__main__":
    main()

