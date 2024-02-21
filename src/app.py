from functions.calculations import *

# Define the year for which the calendar is being created
year = 2024

# Step 1: Get the new moons for the year
new_moons_for_year = get_new_moons(year)

# Step 2: Calculate the spring equinox
spring_equinox = get_spring_equinox(year)

# Step 3: Find the closest new moon to the spring equinox
new_year_date = get_closest_new_moon_to_equinox(year)

# Print the spring equinox and the start date of the new year
print(f"Spring Equinox: {spring_equinox}")
print(f"New Year starts on: {new_year_date.strftime('%A, %B %d, %Y')}")

lunar_month_structure = create_lunar_month_structure(
    new_moons_for_year, new_year_date, year)

# Print the lunar month structure
for month in lunar_month_structure:
    print(f"Start Date: {month['start_date']}, End Date: {
          month['end_date']}, Length: {month['length']} days")
