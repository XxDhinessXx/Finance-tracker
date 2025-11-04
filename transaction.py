from database import get_connection
from datetime import datetime

def add_transaction(description, category, amount):
    date = datetime.now().strftime("%Y-%m-%d")
    conn = get_connection()
    c = conn.cursor()
    c.execute("INSERT INTO transactions (date, description, category, amount) VALUES (?, ?, ?, ?)",
              (date, description, category, amount))
    conn.commit()
    conn.close()
    return "Transaction added successfully!"

def view_transactions():
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM transactions")
    transactions = c.fetchall()
    conn.close()
    return transactions
