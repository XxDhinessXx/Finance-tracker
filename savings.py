from database import get_connection

def set_savings_goal(goal):
    conn = get_connection()
    c = conn.cursor()
    c.execute("DELETE FROM savings")  # Replace existing goal
    c.execute("INSERT INTO savings (goal) VALUES (?)", (goal,))
    conn.commit()
    conn.close()
    return f"Savings goal set: {goal}"

def check_savings_goal(goal):
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT SUM(amount) FROM transactions WHERE category = 'Savings'")
    total_savings = c.fetchone()[0] or 0.0
    conn.close()
    if total_savings >= goal:
        return f"Savings so far: {total_savings}\nYou've reached your savings goal!"
    else:
        return f"Savings so far: {total_savings}\nYou need {goal - total_savings} more to reach your goal."
