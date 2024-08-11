import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox

class CalorieCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calorie Calculator")

        # Variables for storing user input
        self.height_var = tk.DoubleVar()
        self.weight_var = tk.DoubleVar()
        self.age_var = tk.IntVar()
        self.gender_var = tk.StringVar()
        self.exercise_times_var = tk.IntVar()

        # Result variable
        self.tdee_result = tk.StringVar()

        # Create the form
        self.create_form()

    def create_form(self):
        # Height label
        tk.Label(self.root, text="Height (cm):").grid(row=0, column=0, padx=10, pady=5)
        height_entry = tk.Entry(self.root, textvariable=self.height_var)
        height_entry.grid(row=0, column=1, padx=10, pady=5)

        # Weight label
        tk.Label(self.root, text="Weight (kg):").grid(row=1, column=0, padx=10, pady=5)
        weight_entry = tk.Entry(self.root, textvariable=self.weight_var)
        weight_entry.grid(row=1, column=1, padx=10, pady=5)

        # Age label
        tk.Label(self.root, text="Age:").grid(row=2, column=0, padx=10, pady=5)
        age_entry = tk.Entry(self.root, textvariable=self.age_var)
        age_entry.grid(row=2, column=1, padx=10, pady=5)

        # Gender label
        tk.Label(self.root, text="Gender:").grid(row=3, column=0, padx=10, pady=5)
        gender_combobox = ttk.Combobox(self.root, textvariable=self.gender_var, values=["Male", "Female"])
        gender_combobox.grid(row=3, column=1, padx=10, pady=5)
        gender_combobox.set("Male")  # Default value

        # Exercise per week label
        tk.Label(self.root, text="Exercise Per Week:").grid(row=4, column=0, padx=10, pady=5)
        exercise_times_entry = tk.Entry(self.root, textvariable=self.exercise_times_var)
        exercise_times_entry.grid(row=4, column=1, padx=10, pady=5)

        # Calculate button
        calculate_button = tk.Button(self.root, text="Calculate", command=self.calculate_calories)
        calculate_button.grid(row=5, column=0, columnspan=2, pady=10)

        # Result label
        tk.Label(self.root, text="Result:").grid(row=6, column=0, padx=10, pady=5)
        result_label = tk.Label(self.root, textvariable=self.tdee_result)
        result_label.grid(row=6, column=1, padx=10, pady=5)

        # Save button
        save_button = tk.Button(self.root, text="Save", command=self.save_result)
        save_button.grid(row=7, column=0, columnspan=2, pady=10)

    def calculate_calories(self):
        height = self.height_var.get()
        weight = self.weight_var.get()
        age = self.age_var.get()
        gender = self.gender_var.get()
        exercise_times = self.exercise_times_var.get()

        # Mifflin-St Jeor Equation for BMR
        if gender.lower() == 'male':
            bmr = 10 * weight + 6.25 * height - 5 * age + 5
        elif gender.lower() == 'female':
            bmr = 10 * weight + 6.25 * height - 5 * age - 161
        else:
            raise ValueError("Invalid gender. Enter 'Male' or 'Female'.")

        # Calculate Total Daily Energy Expenditure (TDEE)
        tdee = bmr * (1.2 + 0.175 * exercise_times)

        # Display result
        self.tdee_result.set(f"Total Daily Energy Expenditure (TDEE) is: {tdee:.2f} Calories/Day")

    def save_result(self):
        result_to_save = self.tdee_result.get()

        # Ask for save location
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])

        # Save result to file
        with open(file_path, 'w') as file:
            file.write(result_to_save)
        
        messagebox.showinfo("Save Result", "Save Successful!")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalorieCalculator(root)
    root.mainloop()
