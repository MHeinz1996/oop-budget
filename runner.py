from classes.budget import Budget
from classes.expenses import Expenses
from classes.transactions import Transactions
# After you write all your classes, use this file to call them all together and run your program

budget = Budget()
expenses = Expenses()
transactions = Transactions()

print(f"\n\t\t\tBUDGET TOOL\nThis tool is designed to help you calculate your monthly budget")

choice = None
while choice != '8':
    choice = input(f"\n1. View Budget\n2. Add budget\n3. View expenses\n4. Add expenses\n5. View transactions\n6. Add transactions\n7. Clear transactions\n8. Quit\n> ")

    match choice:
        case '1':
            budget.view_budget()

        case '2':
            update = input(f"\nWhat do you want to set your budget to?\n> $")
            budget.add_budget(update)
        
        case '3':
            expenses.view_expenses()

        case '4':
            type = input(f"\nWhat type of expense would you like to add (ex. Food, Rent, Savings, etc.)?\n> ")
            cost = input(f"How much does this expense cost?\n> ")
            expenses.add_expenses(type, cost)

        case '5':
            transactions.view_transactions()

        case '6':
            type = input(f"\nWhat transaction would you like to add?\n> ")
            cost = input(f"How much did this transaction cost?\n> ")
            transactions.add_transactions(type, cost)
        
        case '7':
            transactions.clear_transactions()


# Areas for improvement: Make it so that budget info is stored by user