from database import get_connection

def set_budget(category, amount):
    conn = get_connection()
    c = conn.cursor()
    c.execute("REPLACE INTO budgets (category, amount) VALUES (?, ?)", (category, amount))
    conn.commit()
    conn.close()
    return f"Budget set for {category}: {amount}"

def view_budget():
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM budgets")
    budgets = c.fetchall()
    conn.close()
    return budgets
