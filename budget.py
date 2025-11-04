from database import get_connection

def set_budget(category, amount):
    """Set or update a budget for a category."""
    try:
        conn = get_connection()
        c = conn.cursor()
        c.execute("REPLACE INTO budgets (category, amount) VALUES (?, ?)", (category, amount))
        conn.commit()
        conn.close()
        return f"Budget set for {category}: {amount}"
    except Exception as e:
        return f"Error setting budget: {e}"

def view_budget():
    """Return all budgets."""
    try:
        conn = get_connection()
        c = conn.cursor()
        c.execute("SELECT * FROM budgets")
        budgets = c.fetchall()
        conn.close()
        return budgets
    except Exception as e:
        return []
