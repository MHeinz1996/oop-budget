import csv

class Expenses:
    
    def __init__(self, name) -> None:
        self.file = name

    def view_expenses(self) -> str:
        
        with open(f'data/{self.file}_expenses.csv', newline='') as file:
            csv_reader = csv.reader(file, delimiter=',')
            expenses = [row for row in csv_reader]
            file.close()

        if expenses[0] == []:
            print('\nYour expenses are empty. Please add an expense.')
        else:
            print(f"\nYour current expenses are:")

            for row in expenses:
                print(f"{row[0]}: ${row[1]}")

            for row in expenses:
                print(f"{row[0]}: ${row[1]}")

            total = 0.00

            for row in expenses:
                total += float(row[1])

            print(f"\nThe total cost of your expenses is ${round(total, 2)}")

    def add_expenses(self, type, cost) -> str:
        with open(f'data/{self.file}_expenses.csv', 'a+', newline='') as file:
            espenses = csv.writer(file)
            espenses.writerow([type, cost])
            file.close()
        
        print(f"\nAdded expense {type} for ${cost}.")