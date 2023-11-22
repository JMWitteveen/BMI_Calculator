import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    #BMI formula is: Weight(kg) / (height(m)^2)
    
    try:
        weight = float(weight_entry.get())
        height_in_meter = float(height_entry.get()) / 100

        if weight <=0 or height_in_meter <= 0:
            raise ValueError("Please enter positive values for weight and height.")
        if height_in_meter < 0.3:
            raise ValueError("Please enter your height in centimeters instead of meters.")
    except ValueError as e:
        messagebox.showerror("Error", str(e))
        return

    height_squared = height_in_meter ** 2
    bmi = weight / height_squared
    bmi_category, color_index = get_bmi_category(bmi)
    set_result_label_color(color_index)
    
    result_text = f'Your BMI: {bmi: .2f}\nBMI Category: {bmi_category}'
    result_label.config(text=result_text)
    #result_label.config(text=f'Your BMI: {bmi: .2f}')

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight", 0
    elif 18.5 <= bmi < 25:
        return "Normal weight", 1
    elif 25 <= bmi < 30:
        return "Overweight", 2
    else:
        return "Obese", 3

def set_result_label_color(color_index):
    # Define a list of colors corresponding to the color_index
    color_list = ['blue', 'green', 'orange', 'red']

    if 0 <= color_index < len(color_list):
        result_label.config(fg=color_list[color_index])

#Create the main window
window = tk.Tk()
window.title('BMI Calculator')

#add weight label and input field
tk.Label(window, text="Weight (kg): ").grid(row=0, column=0, padx=10, pady=10)
weight_entry = tk.Entry(window)
weight_entry.grid(row=0, column=1, padx=10, pady=10)

#add height label and input field
tk.Label(window, text="Height (cm): ").grid(row=1, column=0, padx=10, pady=10)
height_entry = tk.Entry(window)
height_entry.grid(row=1, column=1, padx=10, pady=10)

#add the button to calculate the BMI
calculate_button = tk.Button(window, text="Calculate BMI", command=calculate_bmi)
calculate_button.grid(row=2, column=0, padx=10, pady=10)

result_label = tk.Label(window, text="")
result_label.grid(row=3, column=0, padx=10, pady=10)

#This starts the actual GUI
window.mainloop()