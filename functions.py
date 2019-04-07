#leap day: you are given the year and you must write a function to check if the year is leap or not 


def is_leap(year):
    leap = False
        
    if year%4==0:
        if year%100==0 and year%400==0:
            leap = True
        else:
            leap = False
    else:
        leap = False
    return leap

year = int(input())
print(is_leap(year))