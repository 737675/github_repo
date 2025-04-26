#Date Difference Calculator Problem
from datetime import datetime

def calculate_date_difference(date1, date2):
    format = "%d-%m-%Y"  # Expected date format
    d1 = datetime.strptime(date1, format)
    d2 = datetime.strptime(date2, format)
    difference = abs((d2 - d1).days)
    print(f"📅 The difference between {date1} and {date2} is {difference} days.")

# Example usage
date1 = input("Enter the first date (dd-mm-yyyy): ")
date2 = input("Enter the second date (dd-mm-yyyy): ")

calculate_date_difference(date1, date2)



