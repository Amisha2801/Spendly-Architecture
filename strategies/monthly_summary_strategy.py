from typing import List
from models.expense import Expense
from strategies.summary_strategy import SummaryStrategy

# This class is a Concrete Strategy implementation for calculating total monthly expenses.

class MonthlySummaryStrategy(SummaryStrategy):
    def calculate(self, expenses: List[Expense]) -> float:
        total = 0.0
        for expense in expenses:
            total += expense.get_amount()
        return total