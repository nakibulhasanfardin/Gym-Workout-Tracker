# Gym Workout Tracker

# Video Demo: https://youtu.be/FBTkOvTW_zE

# Description:

The Gym Workout Tracker is a Python terminal application designed to help users record and review their gym workout sessions. The main goal of this project is to provide a simple way to track workout performance over time without requiring a complicated interface or external database.

Users can select a predefined workout day and record information about their exercises, including the weight used, number of sets, repetitions, and exercise difficulty. The application also displays information from a previous session, allowing users to compare their current performance with earlier workouts.

The application stores workout history in a JSON file named "workouts.json". This allows the recorded data to remain available after the program is closed and makes it possible to review previous sessions when the application is run again.

# Files:

- "project.py" — Contains the main application and the functions responsible for running the program, processing user input, recording workout information, and displaying workout history.
- "test_project.py" — Contains automated tests written with "pytest" to check the behavior of the application's functions.
- "workouts.json" — Stores workout history in JSON format. The file is created automatically when workout data is saved, if implemented that way in the application.

# Design Choices:

I chose to build this project as a terminal application because it allowed me to focus on Python fundamentals and program logic rather than spending time building a graphical user interface. I organized the code into separate functions to make it easier to read, maintain, and test.

Input validation is included to help prevent invalid entries from disrupting the program. JSON was chosen for data storage because it is a straightforward format that works well for a small application and can be handled using Python's built-in tools.

I also included automated tests using "pytest" to check important parts of the program. Writing tests helped me understand the importance of verifying that functions behave as expected and made the project more reliable.

Through this project, I practiced using Python functions, handling user input, working with files and JSON data, organizing a program into manageable parts, and writing automated tests. The project represents my application of the concepts learned throughout CS50's Introduction to Programming with Python.

# How to Run:

To run the application, open a terminal in the project directory and execute:

python project.py

To run the tests, execute:

pytest test_project.py

# Author:

A.K.M Nakibul Hasan Fardin
