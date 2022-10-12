# sudo coding

# if it's cold:
    # take coat
# if it's raining:
    # rain mack
# if it's sunny:
    # let's go to the beach

weather = 'time'

if weather == 'cold':
    print('wear jacket')
elif weather == 'raining':
    print('wear a rain mack')
elif weather == 'sunny':
    print('let`s go to the beach')
else:
    print('404 no weather found')

# age restriction for movie ticket
age_found = False
while age_found == False:
    age = int(input('Please enter age: '))
    if age >= 18:
        print('18 & above')
        age_found = True
    if age >= 16:
        print('16 & above')
        age_found = True
    if age >= 15:
        print('PG')
        age_found = True
    if age >= 4:
        print('Universal')
        age_found = True
    if age >= 12:
        print('12A')
        age_found = True
    if age > 117:
        age_found = False


