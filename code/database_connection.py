import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Path to your downloaded service account key
cred = credentials.Certificate("serviceAccountKey.json")

# Initialize Firebase app
firebase_admin.initialize_app(cred)

# Get Firestore client
db = firestore.client()

# Add sample data
doc_ref = db.collection("expenses").document("sample_expense")
doc_ref.set({
    "amount": 100,
    "category": "Food",
    "date": "2026-02-20"
})

print("Successfully connected to Firestore and added sample data!")