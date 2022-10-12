list_data = [1, 2, 3, 4, 5]
print(list_data)
for number in list_data:
    if number == 3:
        print(number)
    elif number > 3:
        print('passed 3')
    else:
        print('not found yet')

student_data = {
    "name": 'Benedek',
    "course": 'eng130',
    "age": 22,
    "nationality": 'Hungarian'
}
for key in student_data.keys():
    print(key)
for value in student_data.values():
    print(value)
for key, value in student_data.items():
    if value == 'Benedek':
        print(key)

data = 0
while data < 10:
    print(f'it`s working -> {data}')
    if data == 5:
        break
    data += 1
