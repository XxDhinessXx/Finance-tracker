from database import get_connection
from datetime import datetime

def add_transaction(description, category, amount):
    """Add a transaction to the database."""
    date = datetime.now().strftime("%Y-%m-%d")
    try:
        conn = get_connection()
        c = conn.cursor()
        c.execute("INSERT INTO transactions (date, description, category, amount) VALUES (?, ?, ?, ?)",
                  (date, description, category, amount))
        conn.commit()
        conn.close()
        return "Transaction added successfully!"
    except Exception as e:
        return f"Error adding transaction: {e}"

def view_transactions():
    """Return all transactions."""
    try:
        conn = get_connection()
        c = conn.cursor()
        c.execute("SELECT * FROM transactions")
        transactions = c.fetchall()
        conn.close()
        return transactions
    except Exception as e:
        return []
