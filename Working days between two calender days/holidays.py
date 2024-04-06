from bs4 import BeautifulSoup
import requests
from datetime import date, datetime, timedelta
from bisect import bisect_left,bisect_right

# Function to check if a given date is a Friday or Saturday
def is_weekend(date):
    return date.weekday() in [4, 5]  # 4 is Friday, 5 is Saturday

# Function to get holidays from the website and sort them
def get_sorted_holidays(url):
    result = requests.get(url).text
    doc = BeautifulSoup(result, 'html.parser')

    tbody = doc.find('tbody')
    trs = tbody.find_all('tr')

    holidays = []

    for tr in trs:
        time_tag = tr.find('time', itemprop='startDate')
        if time_tag:
            holiday_date = datetime.strptime(time_tag['datetime'], '%Y-%m-%d').date()
            # Excluding Friday's and Saturday's from the holiday list
            if holiday_date.weekday() not in [4, 5]:  # 4 is Friday, 5 is Saturday
                holidays.append(holiday_date)

    holidays.sort()  # Sort the list of holidays
    return holidays


def working_days(start_date, end_date, holidays):
    total_days = (end_date - start_date).days + 1  # Total number of days
    
    total_weekends = 0
    tds = total_days
    while tds % 7 != 0:
        if start_date.weekday() in [4, 5] or bisect_left(holidays, start_date) != len(holidays) and holidays[bisect_left(holidays, start_date)] == start_date:
            total_weekends += 1
        start_date += timedelta(1)
        tds -= 1
    
    # print(tds)    
    total_weekends += (tds // 7) * 2

    # Find the lower bound of start_date and upper bound of end_date from holidays
    start_idx = bisect_left(holidays, start_date)
    end_idx = bisect_right(holidays, end_date)

    # Subtract the two indexes and add 1 to include end_date, then add the result with total weekends
    if end_idx>=len(holidays) or holidays[end_idx]>end_date:
        total_holidays = end_idx - start_idx
    else:
        total_holidays = end_idx - start_idx

    # add the total holidays to total_weekends
    total_weekends += total_holidays

    # subtract the total weekends from total_days
    working_days_count = total_days - total_weekends
    return working_days_count





# Modify/Edit Start and end dates

x = date(2024, 1, 1)  # Start date
y = date(2024, 2, 29)  # End date

# URL for the website
url = "https://www.officeholidays.com/countries/bangladesh/2024"

# Get sorted holidays from the website
holidays = get_sorted_holidays(url)

# Calculate working days between x and y excluding weekends and holidays
working_days = working_days(x, y, holidays)

print(f'Total {working_days} working days in this period')
