import csv

class Budget():
    def __init__(self) -> None:
        self.budget = 0

    def add_budget(self, new_budget) -> str:
        print(f"\nBudget successfully updated to ${new_budget}")
        self.budget = new_budget
        with open('data/budget.csv', 'w', newline='') as file:
            budget = csv.writer(file)
            budget.writerow(['budget', self.budget])
            file.close()

    def view_budget(self) -> str:
        with open('data/budget.csv', newline='') as file:
            csv_reader = csv.reader(file, delimiter=',')
            budget = [row for row in csv_reader]
            file.close()

        with open('data/expenses.csv', newline='') as file:
            csv_reader = csv.reader(file, delimiter=',')
            expenses = [row for row in csv_reader]
            file.close()

        with open('data/transactions.csv', newline='') as file:
            csv_reader = csv.reader(file, delimiter=',')
            transactions = [row for row in csv_reader]
            file.close()

        total = 0.00

        for row in expenses:
            total += float(row[1])
        
        for row in transactions:
            total += float(row[1])

        print(f"\nYour current budget is ${budget[0][1]}.")
        print(f"Your remaining budget is ${round(float(budget[0][1]) - total, 2)}.")
        print(f"Your expenses make up {float(round((total/float(budget[0][1]))*100, 2))}% of your total budget.")