# Lab 07 - Calendar Verification System

print("========================================")
print("     CALENDAR VERIFICATION SYSTEM       ")
print("========================================")
year = int(input("Enter year: "))
if year <= 0:
    print("Error: Please enter a positive integer greater than 0.")
else:
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        is_leap = True
        reason = "Divisible by 4 and not a century year" if year % 100 != 0 else "Century year divisible by 400"
    else:
        is_leap = False
        if year % 100 == 0:
            reason = "Century year not divisible by 400"
        else:
            reason = "Not divisible by 4"
    if is_leap:
        status = "LEAP YEAR"
        days_in_year = 366
        days_in_feb = 29
    else:
        status = "COMMON YEAR"
        days_in_year = 365
        days_in_feb = 28
    print(f"\nYear: {year}")
    print(f"Status: {status}")
    print(f"Days in Year: {days_in_year} days")
    print(f"Days in February: {days_in_feb} days")
    print(f"Reason: {reason}")