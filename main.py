from database import initialize_db, clear_all_data, get_connection 
from transaction import add_transaction, view_transactions
from budget import set_budget, view_budget
from savings import set_savings_goal, check_savings_goal
from visualization import visualize_spending
import time as tm

def launch_gui():
    import gui  # This will start the GUI

running = True

def main():
    global running
    initialize_db()

    print("Welcome to the Personal Finance Manager!")

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
        print("7. Visualize Spending")
        tm.sleep(0.25)
        print("8. CLEAR ALL DATA")
        tm.sleep(0.25)
        print("9. Exit")
        tm.sleep(0.25)
        print("0. Launch GUI")  # <-- Added option

        tm.sleep(0.3)
        choice = input("Enter your choice: ")

        if choice == '1':
            desc = input("Enter description: ")
            cat = input("Enter category: ")
            amount = float(input("Enter amount: "))
            add_transaction(desc, cat, amount)
        elif choice == '2':
            view_transactions()
        elif choice == '3':
            category = input("Enter category: ")
            amount = float(input(f"Set budget for {category}: "))
            set_budget(category, amount)
        elif choice == '4':
            view_budget()
        elif choice == '5':
            goal = float(input("Enter savings goal: "))
            set_savings_goal(goal)
        elif choice == '6':
            goal = float(input("Enter savings goal to check: "))
            check_savings_goal(goal)
        elif choice == '7':
            visualize_spending()
        elif choice == '8':
            confirm = input("Are you sure you want to clear all data (yes/no): ")
            if confirm.lower() == 'yes':
                clear_all_data()
        elif choice == '9':
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
