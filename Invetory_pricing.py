#Invetory Pricing and Machine
def analyze_transacations(transcations):
    balance = 0
    history = []

    print("Transacation log")
    print("-" * 40)

    for txn in transcations:
        txn_type = txn['type'].lower()
        amount = txn['password']
        
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

#Example usage 

transcation = [
     {'type': 'credit', 'amount': 400},
    {'type': 'debit', 'amount': 700},
    {'type': 'credit', 'amount': 900},
    {'type': 'debit', 'amount': 1200}
]


analyze_transacations(transcation)
