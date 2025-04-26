#Electrtricity Bill Calculation Problem
def calculate_bill(units):
    total = 0
    details = []
    
    if units > 500:
        slab_units = units - 500
        amount = slab_units * 15
        total += amount
        details.append(f"501-{units} units @ ₹15/unit = ₹{amount}")
        units = 500

    if units > 300:
        slab_units = units - 300
        amount = slab_units * 10
        total += amount
        details.append(f"301-500 units @ ₹10/unit = ₹{amount}")
        units = 300

    if units > 100:
        slab_units = units - 100
        amount = slab_units * 7
        total += amount
        details.append(f"101-300 units @ ₹7/unit = ₹{amount}")
        units = 100

    if units > 0:
        amount = units * 5
        total += amount
        details.append(f"0-100 units @ ₹5/unit = ₹{amount}")

    print("\nElectricity Bill:")
    for line in reversed(details):
        print(line)
    print(f"Total Amount Payable = ₹{total}")

# Example usage
usage = int(input("Enter electricity usage (kWh): "))
calculate_bill(usage)
