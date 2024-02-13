import re

# Write a regular expression that can detect dates in the DD/MM/YYYY
# days range from 01 to 31, the months range from 01 to 12, and the years range from 1000 to 2999

# days group (^0?[1-31])
# months group (^0?[1-12])
# years group ([1000-2999])

date_regex = re.compile(r"""
                        (0*[0-9]|1[0-9]|2[0-9]|3[0-1])  # date, first char 0 is optional
                        [/\.-:]+                         # separator, 1 or more
                        (0*[0-9]|1[0-2])                # months, first char 0 is optional
                        [/\.-:]+                         # separator, 1 or more
                        ([1-2][0-9]{3})                 # years, first number 1-2, 3x 0-9 numbers
                        """,
                        re.VERBOSE,
)
match_object = date_regex.search('01/12-2023')
print(match_object.groups())


day, month, year = int(match_object.group(1)), int(match_object.group(2)), int(match_object.group(3))
print(day, month, year)

def valid_date(day, month, year):

    # 31 day months = > [4, 6, 9, 11]
    days_in_months = {1: 31, 2: 0, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    leap_year = False
    # detect if leap year
    # Leap years are every year evenly divisible by 4,
    # except for years evenly divisible by 100, 
    # unless the year is also evenly divisible by 400.
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        leap_year = True
    else:
        leap_year = False
    
    # Adding a correct amount of days to February according if its leap year or not
    if month == 2 and leap_year == True:
        days_in_months[month] = 29
    elif month == 2 and leap_year == False:
        days_in_months[month] = 28
    
    # Checking if month has the correct amount of days or more
        
    for key, value in days_in_months.items():
        if key == month:
            if day > value:
                return False
        else:
            continue
    
    return True
    
print(valid_date(day,month,year))

