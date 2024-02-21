import math
import ephem
import datetime
import math


def get_new_moons(year):
    """
    Calculate the dates of new moons for each month in a given year.

    Args:
    year (int): The year for which new moons should be calculated.

    Returns:
    list of str: A list containing the dates of each new moon in the year.
    """
    new_moons = []
    date = datetime.datetime(year, 1, 1)
    while date.year == year:
        next_new_moon = ephem.next_new_moon(date)
        new_moons.append(next_new_moon.datetime())
        date = next_new_moon.datetime() + datetime.timedelta(days=1)
    return new_moons


def get_spring_equinox(year):
    """
    Calculate the date of the spring equinox for a given year.

    Args:
    year (int): The year for which the spring equinox should be calculated.

    Returns:
    str: The date of the spring equinox in a human-friendly format.
    """
    # Observer location set to Greenwich as default for equinox calculation
    observer = ephem.Observer()
    observer.lat, observer.lon = '0', '0'
    observer.date = f'{year}/1/1'

    # Find the date of the spring equinox
    equinox = ephem.next_vernal_equinox(observer.date)
    return equinox.datetime().strftime("%A, %B %d, %Y")


def get_closest_new_moon_to_equinox(year):
    """
    Calculate the datetime of the closest new moon to the spring equinox for a given year.

    Args:
    year (int): The year for which to calculate.

    Returns:
    datetime: The datetime of the closest new moon to the spring equinox.
    """
    observer = ephem.Observer()
    observer.lat, observer.lon = '0', '0'
    observer.date = f'{year}/1/1'

    equinox = ephem.next_vernal_equinox(observer.date)
    equinox_date = equinox.datetime()

    new_moon_before = ephem.previous_new_moon(equinox_date).datetime()
    new_moon_after = ephem.next_new_moon(equinox_date).datetime()

    if (equinox_date - new_moon_before) < (new_moon_after - equinox_date):
        closest_new_moon = new_moon_before
    else:
        closest_new_moon = new_moon_after

    return closest_new_moon


def create_lunar_month_structure(new_moons, new_year_date, year):
    """
    Create a structure for lunar months starting from the new year moon.

    Args:
    new_moons (list): List of datetime objects for new moons.
    new_year_date (datetime): The new moon date closest to the spring equinox.
    year (int): The year for which the calendar is being created.

    Returns:
    list of dict: Lunar months with start and end dates, and lengths.
    """
    # Convert all new moon datetime objects to date only
    new_moons_dates_only = [moon.date() for moon in new_moons]

    # Find the index of the new year moon
    new_year_index = new_moons_dates_only.index(new_year_date.date())

    # Create lunar months structure
    lunar_months = []
    for i in range(new_year_index, len(new_moons_dates_only)):
        start_date = new_moons[i].date()

        # Calculate end_date as the day before the next new moon
        # For the last month in the list, use the last day of the year
        if i + 1 < len(new_moons_dates_only):
            end_date = new_moons[i + 1].date() - datetime.timedelta(days=1)
        else:
            end_date = datetime.date(year, 12, 31)

        length = (end_date - start_date).days + 1  # Including the start date

        if start_date.year == year:  # Include only months that start in the specified year
            lunar_months.append({
                "start_date": start_date.strftime("%Y-%m-%d"),
                "end_date": end_date.strftime("%Y-%m-%d"),
                "length": length
            })

    return lunar_months
