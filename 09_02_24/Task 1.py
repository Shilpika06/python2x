# Create a program that determines weather a given year is a leap year or not

leap_year= int(input("Enter the year to check whether its a leap year or not:"))
if (leap_year % 4):
    print("The given year", leap_year," is not a leap year")
else:
    print("The given year", leap_year," is a leap year")