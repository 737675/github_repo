#Bank Transacation Analyzer Problem
def analyze_transactions(transactions):
    balance = 0
    history = []

    print("📋 Transaction Log:")
    print("-" * 40)

    for txn in transactions:
        txn_type = txn['type'].lower()
        amount = txn['amount']

        if txn_type == 'credit':
            balance += amount
            log = f"Credited ₹{amount:>6} | Balance: ₹{balance}"
        elif txn_type == 'debit':
            balance -= amount
            log = f"Debited  ₹{amount:>6} | Balance: ₹{balance}"
        else:
            log = f"Invalid transaction type: {txn_type}"
        
        history.append(log)
        print(log)

    print("-" * 40)
    print(f"🧾 Final Balance: ₹{balance}")
    return balance

#Example Usage
transactions = [
    {'type': 'credit', 'amount': 1000},
    {'type': 'debit', 'amount': 200},
    {'type': 'credit', 'amount': 500},
    {'type': 'debit', 'amount': 100}
]

analyze_transactions(transactions)

