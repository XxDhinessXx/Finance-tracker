import sqlite3

def initialize_db():
    """Create tables if they don't exist."""
    conn = sqlite3.connect('finance.db')
    c = conn.cursor()
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
    conn.commit()
    conn.close()

def clear_all_data():
    """Delete all data from all tables."""
    try:
        conn = get_connection()
        c = conn.cursor()
        c.execute("DELETE FROM transactions")
        c.execute("DELETE FROM budgets")
        c.execute("DELETE FROM savings")
        conn.commit()
        conn.close()
        print("All data has been cleared from the database.")
    except Exception as e:
        print(f"Error clearing data: {e}")

def get_connection():
    """Get a connection to the database."""
    return sqlite3.connect('finance.db')
