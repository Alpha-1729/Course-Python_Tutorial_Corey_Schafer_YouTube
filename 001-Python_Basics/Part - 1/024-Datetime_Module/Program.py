#!/usr/bin/python3
# Datetime Module

"""
>>>> In python we have dates, times, datetimes, timezone, time deltas.
>>>> naive and aware datetimes
        naive date and times.
            They don't have enough information to determine things like timezone or daylight savings times.
            But they are easier to work with.
        aware date and times.   
            They have enough information to determine timezone and day light savings.
>>>> Python datetime format code.
        Reference Link: https://docs.python.org/3/library/datetime.html
>>>>
"""

import datetime
import pytz

# Create a date.
# Don't add leading zeroes to month and date.
d = datetime.date(2016, 7, 24)
print(d)

# Create todays local date.
tday = datetime.date.today()
print(tday)

# Getting the Year, Month and Date from the date.
print(tday.year)
print(tday.month)
print(tday.day)

# Get the week day of the date.
print(tday.weekday())   # Monday = 0 and Sunday = 6
print(tday.isoweekday())    # Monday = 1 and Sunday = 7

# Time deltas.
# It is the difference between two date or times.
tdelta = datetime.timedelta(days=7)
print(tday + tdelta)    # Generate a date after 7 days.
print(tday - tdelta)    # Generate a date before 7 days.

# If we add or subtract two dates, we get timedelta as the result.
bday = datetime.date(2027, 9, 24)
till_bday  = bday - tday
print(till_bday)
print(till_bday.days)
print(till_bday.total_seconds())    # Total number of seconds between these two days.

# Times.
# Hour minute second microsecond
t = datetime.time(9, 30, 45, 100000)
print(t)
print(t.microsecond)

# DateTimes.
dt = datetime.datetime(2016, 7, 26, 12, 30, 45, 100000)
print(dt)
print(dt.date())    # Getting the date.
print(dt.time())    # Getting the time.
print(dt.microsecond)   # Getting the individual values.

# Time delta with datetime.
tdelta = datetime.timedelta(hours=12)
print(dt + tdelta)

# 3 main datetime constructor.

#  Return current local datetime with timezone=None (we don't have an option to pass a timezone.)
dt_today =  datetime.datetime.today()

# Return current local datetime.
# Here we have an option to pass a timezone.
dt_now = datetime.datetime.now()

# Gives the UTC time, we don't have an option to pass a timezone.
dt_utcnow = datetime.datetime.utcnow()
print(dt_today)
print(dt_now)
print(dt_utcnow)

# Pytz
# It is a third party package to deal with timezone.
# pip3 install pytz
dt = datetime.datetime(2016, 7, 27, 12, 30, 45, tzinfo=pytz.UTC)
print(dt)

dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(dt_utcnow)

# Simple and standard way.
dt_now = datetime.datetime.now(tz=pytz.UTC)
print(dt_now)

# Convert from UTC time zone to mountain time zone.
dt_mtn = dt_now.astimezone(pytz.timezone('US/Mountain'))
print(dt_mtn)

# Print all timezone in pytz library.
for tz in pytz.all_timezones:
    print(tz) 

# Convert a naive datetime to timezone based.
dt_now = datetime.datetime.now()
mtn_tz = pytz.timezone('US/Mountain')
dt_mtn = mtn_tz.localize(dt_now)
dt_east = dt_mtn.astimezone(pytz.timezone('US/Eastern'))
print(dt_east)


# Displaying dates.
# ISO format.
print(dt_east.isoformat())

# Using format code.
# Convert datetime to string.
# August 06, 2024
print(dt_east.strftime('%B %d, %Y'))

# Convert datetime string to datetime.
dt_str = 'August 06, 2024'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)

