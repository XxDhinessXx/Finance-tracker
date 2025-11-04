import matplotlib.pyplot as plt
from database import get_connection

def visualize_spending():
    """Show a pie chart of spending by category."""
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT category, SUM(amount) FROM transactions GROUP BY category")
    data = c.fetchall()
    conn.close()

    if not data:
        print("No data to visualize.")
        return

    categories = [row[0] for row in data]
    amounts = [row[1] for row in data]

    plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title('Spending by Category')
    plt.show()

def visualize_spending_bar():
    """Show a bar chart of spending by category."""
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT category, SUM(amount) FROM transactions GROUP BY category")
    data = c.fetchall()
    conn.close()

    if not data:
        print("No data to visualize.")
        return

    categories = [row[0] for row in data]
    amounts = [row[1] for row in data]

    plt.bar(categories, amounts, color='skyblue')
    plt.xlabel('Category')
    plt.ylabel('Amount')
    plt.title('Spending by Category')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
