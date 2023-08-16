def it_is_leap_year(year):
    year = int(year)
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


user_input = input('Enter years: ')
years = user_input.split()

for year in years:
    if it_is_leap_year(year):
        print(f'{year} is a leap year')
    else:
        print(f'{year} is not a leap year')
