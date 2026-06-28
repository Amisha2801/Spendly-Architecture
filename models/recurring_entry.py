class RecurringEntry:
    def __init__(self, amount: float, frequency: str, entry_type: str):
        self._amount = amount
        self._frequency = frequency  # e.g. monthly, weekly
        self._type = entry_type      # income or expense

    def get_amount(self) -> float:
        return self._amount

    def get_frequency(self) -> str:
        return self._frequency

    def get_type(self) -> str:
        return self._type

    def __str__(self):
        return f"RecurringEntry(amount={self._amount}, frequency='{self._frequency}', type='{self._type}')"