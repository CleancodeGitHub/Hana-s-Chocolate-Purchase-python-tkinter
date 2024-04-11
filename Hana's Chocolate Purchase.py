#This program allows Hana to input the total amount of money she has and the price of one chocolate bar. Then, it calculates and displays how much money remains for the school fund after buying chocolate bars.#

#===============
import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style

def calculate_school_fund():
    try:
        # Get the values from the entry widgets and convert them to integers
        total_money = int(entry1.get())
        chocolate_price = int(entry2.get())

        # Ensure chocolate price is not zero to avoid division by zero error
        if chocolate_price == 0:
            result_label.config(text='Chocolate price cannot be zero', style='danger.TLabel')
            return

        # Calculate the number of chocolates Hana can buy
        chocolates_bought = total_money // chocolate_price

        # Calculate the remaining money for the school fund
        remaining_money = total_money - (chocolates_bought * chocolate_price)

        # Display the result
        result_label.config(text=f'Hana can buy {chocolates_bought} chocolates and contribute {remaining_money} EUR for the \n school in Africa', style='success.TLabel', font=("Verdana", 14, "bold"))
    except ValueError:
        # Handle the case where the input is not a valid integer
        result_label.config(text='Please enter valid numbers', style='danger.TLabel')
        

# Create the main Tkinter window
root = tk.Tk()
root.title("Hana's Chocolate Purchase")
root.geometry("800x300")
root.configure(bg='#00bf00')  # Light green background color

# Apply ttkbootstrap style
style = Style(theme='minty')

# Create a frame to hold the widgets
frame = ttk.Frame(root)
frame.pack(padx=20, pady=20)

# Create labels and entry widgets
label1 = ttk.Label(frame, text="How many EUR does Hana have?", font=("Verdana", 14, "bold"))
label1.grid(row=0, column=0, padx=10, pady=10)
entry1 = ttk.Entry(frame, style='success.TEntry', font=("Verdana", 14))
entry1.grid(row=0, column=1, padx=10, pady=10)

label2 = ttk.Label(frame, text="How much does one chocolate bar cost?", font=("Verdana", 14, "bold"))
label2.grid(row=1, column=0, padx=10, pady=10)
entry2 = ttk.Entry(frame, style='success.TEntry', font=("Verdana", 14))
entry2.grid(row=1, column=1, padx=10, pady=10)

# Create a button to calculate the remaining money for the school fund
calculate_button = ttk.Button(frame, text="Calculate", command=calculate_school_fund, style='primary.TButton')
calculate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Create a label to display the result
result_label = ttk.Label(root, text="", style='success.TLabel')
result_label.pack(padx=20, pady=20)

# Start the Tkinter event loop
root.mainloop()


