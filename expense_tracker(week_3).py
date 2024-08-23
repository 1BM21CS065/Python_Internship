import json
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import os

# File path for expense data
EXPENSES_FILE = 'expenses_data.json'

# Load expenses from a JSON file
def load_expenses():
    if os.path.exists(EXPENSES_FILE):
        with open(EXPENSES_FILE, 'r') as file:
            return json.load(file)
    return []

# Save expenses to a JSON file
def save_expenses(expense_list):
    with open(EXPENSES_FILE, 'w') as file:
        json.dump(expense_list, file, indent=4)

# Add a new expense record
def record_expense(date_str, amount, category, description):
    expense_entry = {
        'date': date_str,
        'amount': amount,
        'category': category,
        'description': description
    }
    expense_data.append(expense_entry)
    save_expenses(expense_data)

# Calculate the total expenses per month
def calculate_monthly_summary(expense_data):
    monthly_totals = {}
    for entry in expense_data:
        date = datetime.strptime(entry['date'], '%d/%m/%Y')
        period = date.strftime('%Y-%m')
        if period not in monthly_totals:
            monthly_totals[period] = 0
        monthly_totals[period] += entry['amount']
    return monthly_totals

# Calculate total expenses per category
def calculate_category_summary(expense_data):
    category_totals = {}
    for entry in expense_data:
        cat = entry['category']
        if cat not in category_totals:
            category_totals[cat] = 0
        category_totals[cat] += entry['amount']
    return category_totals

# Handle adding an expense via the UI
def handle_add_expense():
    date_input = date_entry.get()
    amount_input = amount_entry.get()
    category_input = category_combobox.get()
    description_input = description_entry.get()

    # Validate the inputs
    if not date_input or not amount_input or not category_input:
        messagebox.showerror("Input Error", "Date, Amount, and Category are required!")
        return

    try:
        amount_value = float(amount_input)
    except ValueError:
        messagebox.showerror("Input Error", "Amount must be a numeric value!")
        return

    try:
        datetime.strptime(date_input, '%d/%m/%Y')
    except ValueError:
        messagebox.showerror("Input Error", "Date must be in DD/MM/YYYY format!")
        return

    record_expense(date_input, amount_value, category_input, description_input)
    messagebox.showinfo("Success", "Expense successfully added!")
    clear_form_entries()

# Clear all form fields
def clear_form_entries():
    date_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    category_combobox.set('')
    description_entry.delete(0, tk.END)

# Display monthly expense summary
def display_monthly_summary():
    summary = calculate_monthly_summary(expense_data)
    summary_text = '\n'.join([f"{period}: ₹{total:.2f}" for period, total in summary.items()])
    messagebox.showinfo("Monthly Summary", summary_text if summary else "No expenses recorded yet!")

# Display category-wise expense summary
def display_category_summary():
    summary = calculate_category_summary(expense_data)
    summary_text = '\n'.join([f"{category}: ₹{total:.2f}" for category, total in summary.items()])
    messagebox.showinfo("Category Summary", summary_text if summary else "No expenses recorded yet!")

# Initialize the main application window
app = tk.Tk()
app.title("Expense Tracker")

# Set background color
app.configure(bg='#e0f7fa')  # Light cyan background

# Layout for the application
main_frame = ttk.Frame(app, padding="20")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Apply styles
style = ttk.Style()
style.configure('TFrame', background='#e0f7fa')
style.configure('TLabel', background='#e0f7fa', foreground='#00796b')
style.configure('TButton', background='#4CAF50', foreground='black', padding=6)
style.map('TButton',
background=[('active', '#388E3C')],
foreground=[('active', 'black')])

# Date input field
ttk.Label(main_frame, text="Date (DD/MM/YYYY):").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
date_entry = ttk.Entry(main_frame, width=20)
date_entry.grid(row=0, column=1, padx=5, pady=5)

# Amount input field
ttk.Label(main_frame, text="Amount (₹):").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
amount_entry = ttk.Entry(main_frame, width=20)
amount_entry.grid(row=1, column=1, padx=5, pady=5)

# Category selection
ttk.Label(main_frame, text="Category:").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
categories = ['Food', 'Transportation', 'Entertainment', 'Utilities', 'Other']
category_combobox = ttk.Combobox(main_frame, values=categories, state='readonly')
category_combobox.grid(row=2, column=1, padx=5, pady=5)

# Description input field
ttk.Label(main_frame, text="Description:").grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
description_entry = ttk.Entry(main_frame, width=50)
description_entry.grid(row=3, column=1, padx=5, pady=5, columnspan=2)

# Action buttons
ttk.Button(main_frame, text="Add Expense", command=handle_add_expense).grid(row=4, column=0, padx=5, pady=10)
ttk.Button(main_frame, text="Monthly Summary", command=display_monthly_summary).grid(row=4, column=1, padx=5, pady=10)
ttk.Button(main_frame, text="Category Summary", command=display_category_summary).grid(row=4, column=2, padx=5, pady=10)

# Set the size and resizing options for the window
app.geometry("600x300")
app.resizable(True, True)

# Load existing expenses data
expense_data = load_expenses()

# Start the main loop of the application
app.mainloop()
