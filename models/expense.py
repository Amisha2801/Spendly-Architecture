class Expense:
    def __init__(self, amount: float, date: str, category: str):
        self._amount = amount
        self._date = date
        self._category = category

    def get_amount(self) -> float:
        return self._amount

    def get_date(self) -> str:
        return self._date

    def get_category(self) -> str:
        return self._category

    def __str__(self):
        return f"Expense(amount={self._amount}, date='{self._date}', category='{self._category}')"