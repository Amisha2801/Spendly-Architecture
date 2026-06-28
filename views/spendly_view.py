from unicodedata import category

from controllers.spendly_controller import SpendlyController
from strategies.monthly_summary_strategy import MonthlySummaryStrategy
from strategies.category_summary_strategy import CategorySummaryStrategy
from datetime import datetime

# This import is for colored terminal output to enhance user experience and make insights more visually appealing.
from colorama import Fore, Style, init

init(autoreset=True)

# Spendly_view is a view layer in MVC architecture.
# This class handles all user interaction and formatted output.

class SpendlyView:
    def __init__(self, controller: SpendlyController):
        self._controller = controller

    def display_menu(self):
        print(Fore.CYAN + "\n===========================================================")
        print(Fore.CYAN + "      💰 WELCOME TO SPENDLY SMART EXPENSE TRACKER 💰")
        print(Fore.CYAN + "===========================================================")
        print(Fore.GREEN + "Track expenses, analyze spending, and gain insights.\n" + Style.RESET_ALL)

        print("1. Add Expense")
        print("2. Generate Monthly Insight Report")
        print("3. Generate Category Summary")
        print("4. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Select an option: ")

            if choice == "1":

                while True:
                    try:
                        amount_input = float(input("Enter amount: "))
                        amount = float(amount_input)  # This ensures that even if user enters a numeric value as a string, it will be converted to float for consistency in data handling.

                        # This check allows users to enter negative values for expenses but gives them the option to convert it to a positive value instead of rejecting it outright, providing flexibility while maintaining data integrity.
                        if amount < 0:
                            print(Fore.YELLOW + "\nWarning: You entered a negative value.")
                            decision = input("Treat this as an expense (convert to positive)? (y/n): ")

                            if decision.lower() == "y":
                                amount = abs(amount)
                                print(Fore.YELLOW + "Amount converted to positive expense.")
                            else:
                                print(Fore.RED + "Expense entry cancelled.\n")
                                break
                        break

                    except ValueError:
                        print(Fore.RED + "\nInvalid amount entered. Please enter a numeric value.\n")
                    
                if amount is None:
                    continue

                while True:   
                    date_input = input("Enter date (YYYY-MM-DD): ")
                    
                    try:
                        datetime.strptime(date_input, "%Y-%m-%d")
                        date = date_input
                        break
                    except ValueError:
                        print(Fore.RED + "\nInvalid date format. Please use YYYY-MM-DD.\n")

                category = input("Enter category: ")

                self._controller.add_expense(amount, date, category)
                print(Fore.GREEN + "\nExpense added successfully.\n")

            elif choice == "2":
                strategy = MonthlySummaryStrategy()
                # This displays structured financial insight report returned from controller.
                report = self._controller.generate_insight_report(strategy)
                
                print(Fore.BLUE + "\n--- Monthly Financial Insight Report ---\n")
                print(f"Raw Total (USD): {Fore.GREEN}${report['total_usd']:.2f}")
                print(f"Converted Total (CAD): {Fore.GREEN}${report['total_cad']:.2f}")
                print(f"Number of Expenses: {Fore.GREEN}{report['expense_count']}\n")
                print(Fore.BLUE + "Financial Insight:")
                print(report['insight'])
                print("\n------------------------------------------------------------------\n")

            elif choice == "3":

                while True:
                    expenses = self._controller.get_expenses()
                    categories = list(set(expense.get_category() for expense in expenses))

                    print("\nEnter category to summarize.")
                    print(Fore.YELLOW + "If you don't know available categories, enter 1 to view available categories.")
                    print(Fore.YELLOW + "Enter * to return to main menu.")

                    category = input("Category: ")

                    if category == "*":
                        break

                    if category == "1":
                        if categories:
                            print(Fore.CYAN + "\nAvailable Categories:")
                            for cat in categories:
                                print(Fore.CYAN + f"- {cat}")
                            print()
                        else:
                            print(Fore.RED + "\nNo categories found in system.\n")
                        continue

                    # This creates a mapping of lowercase category names to their original case versions to allow for case-insensitive user input
                    category_map = {cat.lower():cat for cat in categories}

                    # This check ensures that user enters a valid category and provides guidance if they don't instead of crashing the code.
                    if category.lower() not in category_map:
                        print(Fore.RED + f"\n'{category}' category does not exist.")
                        print(Fore.YELLOW + "Enter 1 to view available categories or try again.\n")
                        continue

                    category = category_map[category.lower()]
                    strategy = CategorySummaryStrategy(category)
                    total = self._controller.generate_summary(strategy)

                    print(Fore.GREEN + f"\nTotal for {category}: ${total:.2f}\n")

            elif choice == "4":
                print(Fore.GREEN + "\nThank you for using Spendly. Stay financially smart!\n")
                break

            else:
                print(Fore.RED + "\nInvalid option. Please try again.\n")