# Warehouse Audit Calendar
# For days 1–30, apply these rules:

# Every 3rd day → Cycle count
# Every 5th day → Scanner audit
# Days that are both → FULL AUDIT
# Any other day → Normal operations

# Expected: Day 3: Cycle count, Day 5: Scanner audit, Day 15: FULL AUDIT, Day 30: FULL AUDIT



months_days = {
    "January": 31,
    "February": 28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
}
month= 'October'
days_in_month = months_days[month]
for day in range(1,days_in_month+1):

# dynamicaly determine the month 


# if day % 3 == 0 and day % 5 == 0:
#     print(f"Day {day} FULL AUDIT ")
# elif day % 5 == 0:
#     print(f"Day {day} Scanner audit")
# elif day % 3 == 0:
#     print(f"Day {day} Cycle count")
# else:
#     print(f"Normal operations")

    for current_day in range(1,days_in_month+1):
        if current_day  == day:
            if day %3 == 0 and day % 5== 0:
                print(f"Day {day} FULL AUDIT")
            elif day % 5 == 0:
                print(f"Day {day} Scanner audit")
            elif day % 3== 0:
                print(f"Day {day} Cycle count")
            else:
                print(f"Day {day} Normal operations")        

