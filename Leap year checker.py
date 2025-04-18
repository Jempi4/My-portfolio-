year = int(input("What year is it? "))

if year < 1582:
    print("The year", year, "is not within the Gregorian calendar period.")
else:
    if year % 4 != 0:
        print ("The year", year, "is a common year.")
    elif year % 100 != 0:
        print ("The year", year, "is a leap year.")
    elif year % 400 != 0:
        print ("The year", year, "is a common year.")
    else:
        print ("The year", year, "is a leap year.")
