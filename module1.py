
import tkinter as tk
from tkinter import messagebox
import pandas as pd
import os

# --- Configuration ---
EXCEL_FILE_NAME = 'employee_data.xlsx'

# --- Data Loading Function ---
def load_data():
    """Loads data from the Excel file and converts it into a dictionary for quick lookup."""
    if not os.path.exists(EXCEL_FILE_NAME):
        messagebox.showerror("File Error", f"The file '{EXCEL_FILE_NAME}' was not found. Please ensure it is in the same folder.")
        return {}
        
    try:
        # Read the Excel file into a pandas DataFrame
        df = pd.read_excel(EXCEL_FILE_NAME)
        
        # Convert the 'ID' column to string to ensure consistent key matching
        df['ID'] = df['ID'].astype(str)
        
        # Set 'ID' as the index and convert the DataFrame to a dictionary
        # orientation='index' makes each row an entry in the dictionary, keyed by 'ID'
        return df.set_index('ID').to_dict('index')
        
    except Exception as e:
        messagebox.showerror("Data Error", f"Could not load data from Excel: {e}")
        return {}

# Load the employee data when the script starts
employee_db = load_data()


# --- Search Function logic ---
def show_details():
    emp_id = entry_id.get().strip() # Get ID and remove extra spaces
    
    # Clear previous results
    lbl_result_name.config(text="")
    lbl_result_desig.config(text="")
    lbl_result_salary.config(text="")
    lbl_result_allowance.config(text="")
    lbl_result_inc.config(text="")

    if emp_id in employee_db:
        data = employee_db[emp_id]
        
        # Update labels with data
        lbl_result_name.config(text=data["Name"], fg="green")
        lbl_result_desig.config(text=data["Designation"])
        lbl_result_salary.config(text=data["Salary"])
        lbl_result_allowance.config(text=data["Other Allowance"])
        lbl_result_inc.config(text=data["Last Increment"])
    else:
        # Show error if ID is invalid or not loaded
        messagebox.showerror("Error", "ID not found! Please check the ID or the Excel file.")

# 3. Main Window Setup (Tkinter GUI)
root = tk.Tk()
root.title("Walton Group Employee Information")
root.geometry("400x450")
root.configure(bg="#f0f0f0")

# --- Header Section ---
header_frame = tk.Frame(root, bg="#0056b3", pady=15)
header_frame.pack(fill="x")

lbl_header = tk.Label(header_frame, text="Walton Group", font=("Arial", 20, "bold"), bg="#0056b3", fg="white")
lbl_header.pack()

# --- Input Section ---
input_frame = tk.Frame(root, bg="#f0f0f0", pady=20)
input_frame.pack()

lbl_enter_id = tk.Label(input_frame, text="Enter Employee ID:", bg="#f0f0f0", font=("Arial", 12))
lbl_enter_id.grid(row=0, column=0, padx=5)

entry_id = tk.Entry(input_frame, font=("Arial", 12), width=10)
entry_id.grid(row=0, column=1, padx=5)

btn_search = tk.Button(input_frame, text="Search", command=show_details, bg="#28a745", fg="white", font=("Arial", 10, "bold"))
btn_search.grid(row=0, column=2, padx=10)

# --- Output Section ---
output_frame = tk.Frame(root, bg="white", bd=2, relief="groove", pady=20, padx=20)
output_frame.pack(fill="both", expand=True, padx=20, pady=10)

# Label Styles
lbl_font = ("Arial", 11, "bold")
val_font = ("Arial", 11)

# Name Row
tk.Label(output_frame, text="Name:", bg="white", font=lbl_font).grid(row=0, column=0, sticky="w", pady=5)
lbl_result_name = tk.Label(output_frame, text="", bg="white", font=val_font)
lbl_result_name.grid(row=0, column=1, sticky="w", pady=5)

# Designation Row
tk.Label(output_frame, text="Designation:", bg="white", font=lbl_font).grid(row=1, column=0, sticky="w", pady=5)
lbl_result_desig = tk.Label(output_frame, text="", bg="white", font=val_font)
lbl_result_desig.grid(row=1, column=1, sticky="w", pady=5)

# Salary Row
tk.Label(output_frame, text="Salary:", bg="white", font=lbl_font).grid(row=2, column=0, sticky="w", pady=5)
lbl_result_salary = tk.Label(output_frame, text="", bg="white", font=val_font)
lbl_result_salary.grid(row=2, column=1, sticky="w", pady=5)

# Allowance Row
tk.Label(output_frame, text="Other Allowance:", bg="white", font=lbl_font).grid(row=3, column=0, sticky="w", pady=5)
lbl_result_allowance = tk.Label(output_frame, text="", bg="white", font=val_font)
lbl_result_allowance.grid(row=3, column=1, sticky="w", pady=5)

# Increment Row
tk.Label(output_frame, text="Last Increment:", bg="white", font=lbl_font).grid(row=4, column=0, sticky="w", pady=5)
lbl_result_inc = tk.Label(output_frame, text="", bg="white", font=val_font)
lbl_result_inc.grid(row=4, column=1, sticky="w", pady=5)

# Run the Application
root.mainloop()