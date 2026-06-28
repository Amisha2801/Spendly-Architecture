from typing import List

from colorama import Fore, Style
from models.expense import Expense
from models.recurring_entry import RecurringEntry
from strategies.summary_strategy import SummaryStrategy
from services.firebase_service import FirebaseService
from services.currency_api_service import CurrencyAPIService

# Controller layer in MVC architecture.
# This class is responsible for coordinating between View, Models, Strategies, and Services.

class SpendlyController:
    def __init__(self):
        self._firebase_service = FirebaseService()
        self._currency_service = CurrencyAPIService()
        self._recurring_entries: List[RecurringEntry] = []

    def add_expense(self, amount: float, date: str, category: str):
        expense = Expense(amount, date, category)
        self._firebase_service.save_expense(expense)

    def get_expenses(self) -> List[Expense]:
        return self._firebase_service.get_expenses()
    
    # This is a basic summary generation used for category-level calculations.
    # This is maintained separately from insight reporting for separation of concerns.
    def generate_summary(self, strategy: SummaryStrategy) -> float:
        expenses = self.get_expenses()
        return strategy.calculate(expenses)

    # This function generates a structured financial insight report.
    # It combines Strategy pattern (calculation logic) and external API integration.
    def generate_insight_report(self, strategy: SummaryStrategy) -> dict:
        expenses = self.get_expenses()
        total_usd = strategy.calculate(expenses)

        exchange_rate = self._currency_service.get_exchange_rate("USD", "CAD")
        total_cad = total_usd * exchange_rate

        # Simple financial insight logic
        if total_usd > 2000:
            insight = "You are spending " + Fore.YELLOW + "ABOVE" + Style.RESET_ALL + " your budget this month."
        elif total_usd > 1000:
            insight = "You current spending level is " + Fore.RED + "HIGH" + Style.RESET_ALL + ". Consider reviewing your expenses for the month"
        elif total_usd > 500:
            insight = "Your spending level is " + Fore.BLUE + "MODERATE" + Style.RESET_ALL + "."
        else:
            insight = "Your spending level is " + Fore.GREEN + "UNDER CONTROL" + Style.RESET_ALL + ". Good job!"

        return {
            "total_usd": total_usd,
            "total_cad": total_cad,
            "expense_count": len(expenses),
            "insight": insight
        }