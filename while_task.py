from datetime import date
today = str(date.today())

year = 0
month = 0
day = 0

while True:
    year = input('Please enter your birth year: ')
    if year.isdigit() and 1900 <= int(year) <= 2022:
        break

while True:
    month = input('Please enter your birth month: ')
    if month.isdigit() and 1 <= int(month) <= 12:
        break

while True:
    day = input('Please enter your birth day: ')
    if day.isdigit() and 1 <= int(day) <= 31:
        break

age = int(today[:4])-int(year)
if int(month) > int(today[5:7]):
    age -= 1
elif int(month) == int(today[5:7]):
    if int(day) > int(today[8:9]):
        age -= 1
print(today)
print(age)