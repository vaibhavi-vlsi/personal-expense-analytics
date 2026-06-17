import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("expense_data.csv")

# Display first rows
print("First five rows:")
print(df.head())

# Calculate total expenses
total_expense = df["Amount"].sum()
print("\nTotal Expense:", total_expense)

# Expense by category
category_expense = df.groupby("Category")["Amount"].sum()

# Create bar chart
plt.figure(figsize=(8, 5))
category_expense.plot(kind="bar")

plt.title("Personal Expenses by Category")
plt.xlabel("Category")
plt.ylabel("Amount")

plt.tight_layout()
plt.savefig("expense_analysis.png")

plt.show()
