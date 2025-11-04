from database import get_connection

def set_savings_goal(goal):
    """Set a new savings goal (replaces existing)."""
    try:
        conn = get_connection()
        c = conn.cursor()
        c.execute("DELETE FROM savings")
        c.execute("INSERT INTO savings (goal) VALUES (?)", (goal,))
        conn.commit()
        conn.close()
        return f"Savings goal set: {goal}"
    except Exception as e:
        return f"Error setting savings goal: {e}"

def check_savings_goal(goal):
    """Check progress towards a savings goal."""
    try:
        conn = get_connection()
        c = conn.cursor()
        c.execute("SELECT SUM(amount) FROM transactions WHERE category = 'Savings'")
        total_savings = c.fetchone()[0] or 0.0
        conn.close()
        if total_savings >= goal:
            return f"Savings so far: {total_savings}\nYou've reached your savings goal!"
        else:
            return f"Savings so far: {total_savings}\nYou need {goal - total_savings} more to reach your goal."
    except Exception as e:
        return f"Error checking savings goal: {e}"

def view_savings_goal():
    """View the current savings goal."""
    try:
        conn = get_connection()
        c = conn.cursor()
        c.execute("SELECT goal FROM savings ORDER BY id DESC LIMIT 1")
        row = c.fetchone()
        conn.close()
        if row:
            return f"Current savings goal: {row[0]}"
        else:
            return "No savings goal set."
    except Exception as e:
        return f"Error viewing savings goal: {e}"
