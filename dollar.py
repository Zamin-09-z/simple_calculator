import tkinter as tk
from tkinter import messagebox

# Conversion rate from INR to USD
INR_TO_USD = 279

def convert_to_dollar():
    try:
        rupees = float(entry_rupees.get())
        dollars = rupees / INR_TO_USD
        label_result.config(text=f"${dollars:.2f} USD")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number")

# Create the main window
root = tk.Tk()
root.title("Rupee to Dollar Converter")
root.geometry("300x200")

# Label and entry for rupee input
label_rupees = tk.Label(root, text="Enter amount in Rupees:")
label_rupees.pack(pady=10)

entry_rupees = tk.Entry(root)
entry_rupees.pack(pady=5)

# Button to convert
button_convert = tk.Button(root, text="Convert to Dollar", command=convert_to_dollar)
button_convert.pack(pady=10)

# Label to show result
label_result = tk.Label(root, text="")
label_result.pack(pady=10)

# Start the GUI event loop
root.mainloop()

