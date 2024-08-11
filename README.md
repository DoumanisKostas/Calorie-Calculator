# Calorie Calculator

A simple desktop application for calculating the Total Daily Energy Expenditure (TDEE) using the Mifflin-St Jeor Equation. This application allows users to input their height, weight, age, gender, and exercise frequency to estimate the number of calories they need to maintain their current weight.

## Features

- Input height (cm), weight (kg), age, gender, and exercise frequency (times per week).
- Calculates the Total Daily Energy Expenditure (TDEE) based on the Mifflin-St Jeor Equation.
- Displays the calculated TDEE in calories per day.
- Option to save the result to a text file.

## Requirements

- Python 3.x
- Tkinter (usually included with Python)
- 
- ## Usage

1. Run the application:
    ```bash
    python calorie_calculator.py
    ```

2. Enter your height, weight, age, gender, and exercise frequency.

3. Click "Calculate" to compute your TDEE.

4. The result will be displayed on the screen.

5. Click "Save" to save the result to a text file.

## Code Explanation

- **CalorieCalculator Class**: This class creates and manages the main application window. It includes methods for creating the user interface, calculating the TDEE, and saving the result to a file.
  - `create_form()`: Sets up the layout and widgets for the user interface.
  - `calculate_calories()`: Computes the TDEE based on user input and displays it.
  - `save_result()`: Saves the displayed result to a text file.
