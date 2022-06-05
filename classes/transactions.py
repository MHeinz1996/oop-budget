import csv

class Transactions():
    def view_transactions(self) -> str:
        with open('data/transactions.csv', newline='') as file:
            csv_reader = csv.reader(file, delimiter=',')
            transactions = [row for row in csv_reader]
            file.close()

        # print(expenses[0])
        print(f"\nYour current transactions are:")

        for row in transactions:
            print(f"{row[0]}: ${row[1]}")

        total = 0.00

        for row in transactions:
            total += float(row[1])
        
        print(f"\nThe total cost of your transactions is ${round(total, 2)}")

    def add_transactions(self, type, cost) -> str:
        with open('data/transactions.csv', 'a+', newline='') as file:
            transactions = csv.writer(file)
            transactions.writerow([type, cost])
            file.close()

        print(f"\nAdded transaction {type} for ${cost}.")

    def clear_transactions(self):
        file = open('data/transactions.csv', 'w+')
        file.close()
        print("\nTransactions have been cleared.")