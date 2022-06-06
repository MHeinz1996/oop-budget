import csv

class Budget:
    def __init__(self, name) -> None:
        self.budget = 0
        self.file = name

    def add_budget(self, new_budget) -> str:
        print(f"\nBudget successfully updated to ${new_budget}")
        self.budget = new_budget
        with open(f'data/{self.file}_budget.csv', 'w', newline='') as file:
            budget = csv.writer(file)
            budget.writerow(['budget', self.budget])
            file.close()

    def view_budget(self) -> str:
        with open(f'data/{self.file}_budget.csv', newline='') as file:
            csv_reader = csv.reader(file, delimiter=',')
            budget = [row for row in csv_reader]
            file.close()
        if budget[0] == []:
            print('\nYour budget is empty. Please add a budget.')
        else:
            with open(f'data/{self.file}_expenses.csv', newline='') as file:
                csv_reader = csv.reader(file, delimiter=',')
                expenses = [row for row in csv_reader]
                file.close()

            if expenses[0] == []:
                print('\nYour expenses are empty. Please add an expense.')
            else:
                with open(f'data/{self.file}_transactions.csv', newline='') as file:
                    csv_reader = csv.reader(file, delimiter=',')
                    transactions = [row for row in csv_reader]
                    file.close()
                
                if transactions[0] == []:
                    print('\nYour transactions are empty. Please add a transaction.')
                else:

                    total = 0.00

                    for row in expenses:
                        total += float(row[1])
                    
                    for row in transactions:
                        total += float(row[1])

                    print(f"\nYour current budget is ${budget[0][1]}.")
                    print(f"Your remaining budget is ${round(float(budget[0][1]) - total, 2)}.")
                    print(f"Your expenses make up {float(round((total/float(budget[0][1]))*100, 2))}% of your total budget.")