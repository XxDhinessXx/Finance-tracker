import tkinter as tk
from tkinter import messagebox
from database import initialize_db, clear_all_data
from transaction import add_transaction, view_transactions
from budget import set_budget, view_budget
from savings import set_savings_goal, check_savings_goal, view_savings_goal
from visualization import visualize_spending, visualize_spending_bar

def add_transaction_gui():
    win = tk.Toplevel(root)
    win.title("Add Transaction")

    tk.Label(win, text="Description:").grid(row=0, column=0)
    desc_entry = tk.Entry(win)
    desc_entry.grid(row=0, column=1)

    tk.Label(win, text="Category:").grid(row=1, column=0)
    cat_entry = tk.Entry(win)
    cat_entry.grid(row=1, column=1)

    tk.Label(win, text="Amount:").grid(row=2, column=0)
    amt_entry = tk.Entry(win)
    amt_entry.grid(row=2, column=1)

    def submit():
        desc = desc_entry.get()
        cat = cat_entry.get()
        try:
            amt = float(amt_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid amount.")
            return
        add_transaction(desc, cat, amt)
        messagebox.showinfo("Success", "Transaction added.")
        win.destroy()

    tk.Button(win, text="Submit", command=submit).grid(row=3, column=0, columnspan=2)

def view_transactions_gui():
    transactions = view_transactions()
    if not transactions:
        messagebox.showinfo("Transactions", "No transactions found.")
        return
    msg = ""
    for trans in transactions:
        msg += f"ID: {trans[0]}, Date: {trans[1]}, Desc: {trans[2]}, Cat: {trans[3]}, Amount: {trans[4]}\n"
    messagebox.showinfo("Transactions", msg)

def set_budget_gui():
    win = tk.Toplevel(root)
    win.title("Set Budget")

    tk.Label(win, text="Category:").grid(row=0, column=0)
    cat_entry = tk.Entry(win)
    cat_entry.grid(row=0, column=1)

    tk.Label(win, text="Amount:").grid(row=1, column=0)
    amt_entry = tk.Entry(win)
    amt_entry.grid(row=1, column=1)

    def submit():
        cat = cat_entry.get()
        try:
            amt = float(amt_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid amount.")
            return
        set_budget(cat, amt)
        messagebox.showinfo("Success", "Budget set.")
        win.destroy()

    tk.Button(win, text="Submit", command=submit).grid(row=2, column=0, columnspan=2)

def view_budget_gui():
    budgets = view_budget()
    if not budgets:
        messagebox.showinfo("Budgets", "No budgets set.")
        return
    msg = ""
    for budget in budgets:
        msg += f"Category: {budget[1]}, Amount: {budget[2]}\n"
    messagebox.showinfo("Budgets", msg)

def set_savings_goal_gui():
    win = tk.Toplevel(root)
    win.title("Set Savings Goal")

    tk.Label(win, text="Savings Goal:").grid(row=0, column=0)
    goal_entry = tk.Entry(win)
    goal_entry.grid(row=0, column=1)

    def submit():
        try:
            goal = float(goal_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid amount.")
            return
        set_savings_goal(goal)
        messagebox.showinfo("Success", "Savings goal set.")
        win.destroy()

    tk.Button(win, text="Submit", command=submit).grid(row=1, column=0, columnspan=2)

def check_savings_goal_gui():
    win = tk.Toplevel(root)
    win.title("Check Savings Progress")

    tk.Label(win, text="Savings Goal to Check:").grid(row=0, column=0)
    goal_entry = tk.Entry(win)
    goal_entry.grid(row=0, column=1)

    def submit():
        try:
            goal = float(goal_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid amount.")
            return
        result = check_savings_goal(goal)
        messagebox.showinfo("Savings Progress", result)
        win.destroy()

    tk.Button(win, text="Submit", command=submit).grid(row=1, column=0, columnspan=2)

def view_savings_goal_gui():
    result = view_savings_goal()
    messagebox.showinfo("Current Savings Goal", result)

def visualize_spending_gui():
    visualize_spending()

def visualize_spending_bar_gui():
    visualize_spending_bar()

def clear_all_data_gui():
    confirm = messagebox.askyesno("Confirm", "Are you sure you want to clear all data?")
    if confirm:
        clear_all_data()
        messagebox.showinfo("Success", "All data cleared.")

def exit_app():
    root.destroy()

# Initialize DB and GUI
initialize_db()
root = tk.Tk()
root.title("Personal Finance Manager")

# Main menu buttons
tk.Button(root, text="Add Transaction", width=30, command=add_transaction_gui).pack(pady=5)
tk.Button(root, text="View Transactions", width=30, command=view_transactions_gui).pack(pady=5)
tk.Button(root, text="Set Budget", width=30, command=set_budget_gui).pack(pady=5)
tk.Button(root, text="View Budget", width=30, command=view_budget_gui).pack(pady=5)
tk.Button(root, text="Set Savings Goal", width=30, command=set_savings_goal_gui).pack(pady=5)
tk.Button(root, text="Check Savings Progress", width=30, command=check_savings_goal_gui).pack(pady=5)
tk.Button(root, text="Visualize Spending (Pie Chart)", width=30, command=visualize_spending_gui).pack(pady=5)
tk.Button(root, text="Visualize Spending (Bar Chart)", width=30, command=visualize_spending_bar_gui).pack(pady=5)
tk.Button(root, text="View Savings Goal", width=30, command=view_savings_goal_gui).pack(pady=5)
tk.Button(root, text="CLEAR ALL DATA", width=30, fg="red", command=clear_all_data_gui).pack(pady=5)
tk.Button(root, text="Exit", width=30, command=exit_app).pack(pady=5)

root.mainloop()
