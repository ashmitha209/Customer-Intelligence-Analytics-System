import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Your Password",
    database="customer_insights"
)
cursor = connection.cursor()
query = """
SELECT
    c.customer_name,
    SUM(o.total_amount) AS total_spent
FROM customer c
JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY c.customer_name
ORDER BY total_spent DESC
LIMIT 10;
"""
cursor.execute(query)

result = cursor.fetchall()

print("========== TOP 10 CUSTOMERS BY SPENDING ==========\n")

for row in result:
    print("Customer Name :", row[0])
    print("Total Spent :", row[1])
    print("--------------------------------------------")

cursor.close()
connection.close()
