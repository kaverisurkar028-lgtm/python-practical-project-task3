# Smart Expense Tracker - Task 3
import json
import os
from datetime import datetime

class ExpenseTracker:
    def __init__(self):
        self.file = "expenses.json"
        self.expenses = self.load_data()
    
    def load_data(self):
        if os.path.exists(self.file):
            with open(self.file, "r") as f:
                return json.load(f)
        return []
    
    def save_data(self):
        with open(self.file, "w") as f:
            json.dump(self.expenses, f, indent=4)
    
    def add_expense(self):
        amount = float(input("Amount: "))
        category = input("Category (Food/Travel/Bills/Shopping): ")
        desc = input("Description: ")
        date = datetime.now().strftime("%d-%m-%Y")
        self.expenses.append({
            "amount": amount,
            "category": category,
            "desc": desc,
            "date": date
        })
        self.save_data()
        print("✅ Expense Added & Saved!")
    
    def view_all(self):
        if not self.expenses:
            print("No expenses yet")
            return
        total = 0
        for i, e in enumerate(self.expenses, 1):
            print(f"{i}. {e['date']} | {e['category']} | ₹{e['amount']} | {e['desc']}")
            total += e['amount']
        print(f"\nTotal Spent: ₹{total}")
    
    def category_wise(self):
        totals = {}
        for e in self.expenses:
            totals[e['category']] = totals.get(e['category'], 0) + e['amount']
        print("\n--- Category Wise Total ---")
        for cat, amt in totals.items():
            print(f"{cat}: ₹{amt}")

tracker = ExpenseTracker()
while True:
    print("\n=== SMART EXPENSE TRACKER ===")
    print("1.Add Expense 2.View All 3.Category Total 4.Exit")
    ch = input("Choice: ")
    if ch == '1': tracker.add_expense()
    elif ch == '2': tracker.view_all()
    elif ch == '3': tracker.category_wise()
    elif ch == '4': 
        print("Goodbye!")
        break
