import tkinter as tk

def calculate_bmi():
    #BMI formula is: Weight(kg) / (height(m)^2)
    weight = float(weight_entry.get())
    height_in_cm = float(height_entry.get()) / 100
    height_squared = height_in_cm ** 2
    bmi = weight / height_squared

    result_label.config(text=f'Your BMI: {bmi: .2f}')


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