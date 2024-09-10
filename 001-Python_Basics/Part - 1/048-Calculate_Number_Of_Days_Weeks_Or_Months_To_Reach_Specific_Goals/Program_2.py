# Script to calculate the number of weeks to loose a certain number of pounds.


import datetime

current_weight = 220
goal_weight = 180
avg_lbs_week = 1.5

start_date = datetime.date.today()
current_date = start_date 

while current_weight > goal_weight:
    current_date += datetime.timedelta(days=7)
    current_weight -= avg_lbs_week

print(f"Current data: {current_date}")
print(f"Reached goal in {(current_date - start_date).days // 7} weeks")
