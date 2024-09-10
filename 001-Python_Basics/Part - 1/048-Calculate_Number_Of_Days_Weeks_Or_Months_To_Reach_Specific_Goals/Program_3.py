# Script to calculate how long does to take to reach certain number of subscribers in youtube.

import datetime
import math

goal_subs = 100000
current_subs = 85000
subs_to_go = goal_subs - current_subs

avg_subs_day = 200
days_to_go = math.ceil(subs_to_go / current_subs)

today = datetime.date.today()
print(today + datetime.timedelta(days=days_to_go))
