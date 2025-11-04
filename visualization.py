import matplotlib.pyplot as plt
from database import get_connection

def visualize_spending():
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT category, SUM(amount) FROM transactions GROUP BY category")
    data = c.fetchall()
    conn.close()

    categories = [row[0] for row in data]
    amounts = [row[1] for row in data]

    # Create a pie chart
    plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures the pie is drawn as a circle.
    plt.title('Spending by Category')
    plt.show()
