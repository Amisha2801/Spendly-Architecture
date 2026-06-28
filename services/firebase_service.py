import os
import firebase_admin
from firebase_admin import credentials, firestore
from models.expense import Expense

# This Service layer is responsible for all Firestore interactions.
# This class encapsulates database logic to maintain architectural separation.
class FirebaseService:
    def __init__(self):
        # Prevent re-initializing Firebase multiple times
        if not firebase_admin._apps:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            cred_path = os.path.join(current_dir, "serviceAccountKey.json")
            cred = credentials.Certificate(cred_path)
            firebase_admin.initialize_app(cred)

        self._db = firestore.client()

    # This function persists a single expense record to the cloud database.
    def save_expense(self, expense: Expense):
        self._db.collection("expenses").add({
            "amount": expense.get_amount(),
            "date": expense.get_date(),
            "category": expense.get_category()
        })

    # This function retrieves all stored expense records from Firestore and converts them into Expense model objects.
    def get_expenses(self):
        expenses = []
        docs = self._db.collection("expenses").stream()
        for doc in docs:
            data = doc.to_dict()
            expense = Expense(
                data["amount"],
                data["date"],
                data["category"]
            )
            expenses.append(expense)

        return expenses