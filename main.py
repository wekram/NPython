#задание 3

print(list(range(20)))
for number in range(1, 21, 1):
    if number == 1:
        print(number, 'процент')
    elif number >= 2 and number < 5:
            print(number, 'процента')
    else:
        print(number, 'процентов')

#задание 1

print('duration = 30')
duration = 30
s = 1
m = 60
h = 3600
d = 86400
print(m - duration, 'cек')

print('duration = 130')
duration = 130
print(duration // m, 'мин', 130 % m, 'сек')

print('duration = 6500')
duration = 6500
print(duration // (d // m), 'часа', 6500 // h, 'мин', 6500 % m, 'сек')

print('duration = 259200')
duration = 259200
print((duration // d), 'дня', d % m, 'часов', duration % h, 'мин', duration % m, 'сек')

#задание 2