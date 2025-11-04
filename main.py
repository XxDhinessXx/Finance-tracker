from database import initialize_db, clear_all_data, get_connection 
from transaction import add_transaction, view_transactions
from budget import set_budget, view_budget
from savings import set_savings_goal, check_savings_goal, view_savings_goal
from visualization import visualize_spending, visualize_spending_bar
import time as tm

def launch_gui():
    import gui  # This will start the GUI

running = True

def print_budgets():
    budgets = view_budget()
    if not budgets:
        print("No budgets set.")
    else:
        for budget in budgets:
            print(f"Category: {budget[1]}, Amount: {budget[2]}")

def print_transactions():
    transactions = view_transactions()
    if not transactions:
        print("No transactions found.")
    else:
        for trans in transactions:
            print(f"ID: {trans[0]}, Date: {trans[1]}, Desc: {trans[2]}, Cat: {trans[3]}, Amount: {trans[4]}")

def main():
    global running
    initialize_db()

    print("Welcome to the Personal Finance Manager!")

    categories = ["Food", "Rent", "Utilities", "Savings", "Income", "Other"]

    # This is the main loop of the program. It will run until the user chooses to exit 
    while running is True:
        print("\nChoose an option:")
        tm.sleep(0.3) 

        # time delay to make it appear as if the software is slowly rendering all the options.
        # This also allows for easier reading as the options appear slower and not appear all at once
        # Gives the program itself a slower and more calm approach
        # O.25s is the best because human reaction time is 0.25s and would appear to be the perfect timing
        print("1. Add Transaction")
        tm.sleep(0.25)
        print("2. View Transactions")
        tm.sleep(0.25)
        print("3. Set Budget")
        tm.sleep(0.25)
        print("4. View Budget")
        tm.sleep(0.25)
        print("5. Set Savings Goal")
        tm.sleep(0.25)
        print("6. Check Savings Progress")
        tm.sleep(0.25)
        print("7. Visualize Spending (Pie Chart)")
        tm.sleep(0.25)
        print("8. Visualize Spending (Bar Chart)")
        tm.sleep(0.25)
        print("9. CLEAR ALL DATA")
        tm.sleep(0.25)
        print("10. Exit")
        tm.sleep(0.25)
        print("0. Launch GUI")  # <-- Added option

        tm.sleep(0.3)
        choice = input("Enter your choice: ")

        if choice == '1':
            desc = input("Enter description: ")
            print(f"Categories: {', '.join(categories)}")
            cat = input("Enter category: ")
            try:
                amount = float(input("Enter amount: "))
                print(add_transaction(desc, cat, amount))
            except ValueError:
                print("Invalid amount.")
        elif choice == '2':
            print_transactions()
        elif choice == '3':
            print(f"Categories: {', '.join(categories)}")
            category = input("Enter category: ")
            try:
                amount = float(input(f"Set budget for {category}: "))
                print(set_budget(category, amount))
            except ValueError:
                print("Invalid amount.")
        elif choice == '4':
            print_budgets()
        elif choice == '5':
            try:
                goal = float(input("Enter savings goal: "))
                print(set_savings_goal(goal))
            except ValueError:
                print("Invalid amount.")
        elif choice == '6':
            print(view_savings_goal())
            try:
                goal = float(input("Enter savings goal to check: "))
                print(check_savings_goal(goal))
            except ValueError:
                print("Invalid amount.")
        elif choice == '7':
            visualize_spending()
        elif choice == '8':
            visualize_spending_bar()
        elif choice == '9':
            confirm = input("Are you sure you want to clear all data (yes/no): ")
            if confirm.lower() == 'yes':
                clear_all_data()
        elif choice == '10':
            print("Goodbye!")
            running = False
        elif choice == '0':
            print("Launching GUI...")
            launch_gui()
            # After closing the GUI, the terminal menu will continue
        else:
            print("Invalid choice. Please try again.")

    from gui import root  # This will start the GUI and block until closed

if __name__ == '__main__':
    main()
