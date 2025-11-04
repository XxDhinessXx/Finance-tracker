import sqlite3

def initialize_db():
    conn = sqlite3.connect('finance.db')  # This creates or connects to the 'finance.db' database file
    c = conn.cursor()

    # Create tables if they don't exist
    c.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY,
            date TEXT,
            description TEXT,
            category TEXT,
            amount REAL
        )
    ''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS budgets (
            id INTEGER PRIMARY KEY,
            category TEXT UNIQUE,
            amount REAL
        )
    ''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS savings (
            id INTEGER PRIMARY KEY,
            goal REAL
        )
    ''')

    conn.commit()  # Save changes
    conn.close()  # Close the connection to the database

def clear_all_data():
    conn = get_connection()  # Use your existing function to get the database connection
    c = conn.cursor()

    # Delete all rows from the transactions, budgets, and savings tables
    c.execute("DELETE FROM transactions")
    c.execute("DELETE FROM budgets")
    c.execute("DELETE FROM savings")

    conn.commit()  # Save the changes
    conn.close()

    print("All data has been cleared from the database.")

def get_connection():
    return sqlite3.connect('finance.db')
