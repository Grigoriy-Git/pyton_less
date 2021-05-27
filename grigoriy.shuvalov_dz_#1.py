#1
duration = input('Введите число: ')
if duration.isdigit():
    duration = int(duration)
    print(duration // 3600, duration // 60 % 60, duration % 60)
else:
    print('Вы ввели не число!')

#2
my_list = [i ** 3 for i in range(1, 1001, 2)]
m_sum = 0
for num in my_list:
    my_sum = 0
    for my_sum in str(num):
        my_sum = int(my_sum)
        my_sum += int(my_sum)
    if my_sum % 7 == 0:
        m_sum += num
print(m_sum)

my_list = [i ** 3 for i in range(1, 1001, 2)]
m_sum = 0
for num in my_list:
    num +=17
    my_sum = 0
    for my_sum in str(num):
        my_sum = int(my_sum)
        my_sum += int(my_sum)
    if my_sum % 7 == 0:
        m_sum += num
print(m_sum)

#3

Percent = input('Введите число: ')
if Percent.isdigit():
    Percent = int(Percent)
else:
    print('Вы ввели не число!')
if Percent == 1: word = 'процент'
elif Percent <= 4: word = 'процента'
else: word = 'процентов'
print(Percent, word)


