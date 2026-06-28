from abc import ABC, abstractmethod
from typing import List
from models.expense import Expense

# Class Strategy interface defines summary calculation behavior.
# It enables flexible extension of calculation logic without modifying controller.

class SummaryStrategy(ABC):
    @abstractmethod
    def calculate(self, expenses: List[Expense]) -> float:
        pass