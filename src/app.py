from convertdate import french_republican
from datetime import datetime
import sys


def convert_to_french_republican(year, month, day):
    return french_republican.from_gregorian(year, month, day)


print("Date Converter to French Republican Calendar")

choice = input(
    "Do you want to use the current date? (yes/no): ").strip().lower()

if choice == 'yes':
    current_date = datetime.now()
    year, month, day = current_date.year, current_date.month, current_date.day
elif choice == 'no':
    try:
        year = int(input("Enter year (YYYY): "))
        month = int(input("Enter month (1-12): "))
        day = int(input("Enter day (1-31): "))
        datetime(year, month, day)  # Validate date
    except ValueError:
        print("Invalid date entered.")
        sys.exit(1)
else:
    print("Invalid choice. Please enter 'yes' or 'no'.")
    sys.exit(1)

french_date = convert_to_french_republican(year, month, day)
print(
    f"French Republican Date: Year {french_date[0]}, Month {french_date[1]}, Day {french_date[2]}")
