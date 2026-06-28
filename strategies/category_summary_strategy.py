from typing import List
from models.expense import Expense
from strategies.summary_strategy import SummaryStrategy

# This class is a Concrete Strategy implementation for category-based expense calculation.
class CategorySummaryStrategy(SummaryStrategy):
    def __init__(self, category: str):
        self._category = category

    def calculate(self, expenses: List[Expense]) -> float:
        total = 0.0
        for expense in expenses:
            # I used case-insensitive comparison to improve robustness and avoid errors
            if expense.get_category().lower() == self._category.lower():
                total += expense.get_amount()
        return total