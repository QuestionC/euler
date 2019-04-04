# Thirty days has september, april, june and november
# all the rest have thirty-one Saving february alone 
# which has twentry eight, rain or shine, and on leap years, twenty nine
# A leap year occours on any year evenly divisible by 4, but not on a century unless it is divisible by 400

# How many sundays fell on the first of the month from Jan1901 thru Dec2000?
# 1 Jan 1900 was a Monday

# 0 = sunday
day = 1

month_info = {
        1: ("January", 31),
        2: ("February", 0),
        3: ("March", 31),
        4: ("April", 30),
        5: ("May", 31),
        6: ("June", 30),
        7: ("July", 31),
        8: ("August", 31),
        9: ("September", 30),
        10: ("October", 31),
        11: ("November", 30),
        12: ("December", 31)
        }


# Increment every time we encounter day = 0
num_sundays = 0

for year in range (1900, 2001):
    for month in range (1, 13):
        if day == 0 and year > 1900:
            num_sundays += 1
       
        # Now pass the number of days
        if month == 2:
            # Leap year?
            if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                print ((month_info[month][0], year))
                day += 29
            else:
                day += 28
        else:
            day += month_info[month][1]
        day %= 7

print (num_sundays)
