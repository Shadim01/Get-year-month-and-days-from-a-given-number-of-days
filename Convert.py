days_in_year = 360
days_in_week = 7
days_in_month = 30

def find(numberofdays):
    year = int(numberofdays / days_in_year)
    month = int(numberofdays % days_in_year)/days_in_month
    week = int(numberofdays % days_in_year)/days_in_week
    day = int(numberofdays % days_in_year) % days_in_week

    print(f"\n\tYears : {year}\n\tMonths : {month}\n\tWeeks : {week}\n\tDays : {day}")

numberofdays = int(input("Number of days :"))

find(numberofdays)
