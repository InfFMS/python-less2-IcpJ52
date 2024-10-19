num_of_month = int(input())
if num_of_month in [1, 2, 12]:
    print('Зима')
elif num_of_month in [3, 4, 5]:
    print('Весна')
elif num_of_month in [6, 7, 8]:
    print('Лето')
elif num_of_month in [9, 10, 11]:
    print('Осень')
else:
    print('Неверный номер месяца')
