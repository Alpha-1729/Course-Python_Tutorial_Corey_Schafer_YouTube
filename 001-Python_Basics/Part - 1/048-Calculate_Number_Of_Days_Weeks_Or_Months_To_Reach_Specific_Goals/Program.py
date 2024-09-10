#!/usr/bin/python3
# Calculate Number Of Days Weeks Or Months To Reach Specific Goals

"""
>>>>
>>>>
>>>>
>>>>
"""

# Script to calculate the number of month to pay off a credit card.

import datetime
import calendar


def get_next_month_start_date(today):
    """
    Calculate the first day of the next month.
        First find the remaining days of the current month.
        Add one day to get the first day of the next month.
    """
    # calendar.monthrange() will return the day number of the first day of the month and total days in that month.
    # day number 0 corresponds to Monday.
    days_in_current_month = calendar.monthrange(today.year, today.month)[1]
    days_till_month_end = days_in_current_month - today.day
    start_date = today + datetime.timedelta(days=days_till_month_end + 1)
    return start_date


balance = 5000
interest_rate = 13 * 0.01
monthly_payment = 500

today = datetime.date.today()
start_date = get_next_month_start_date(today)
current_date = start_date

while balance > 0:
    interest_charge = (interest_rate / 12) * balance
    balance += interest_charge
    balance -= monthly_payment

    balance = round(balance, 2)
    if balance < 0:
        balance = 0

    print(current_date, balance)

    current_date = get_next_month_start_date(current_date)
