# Что будет выведено на экран в результате выполнения следующей программы?

'''num1 = 34
num2 = 81
if num1 // 9 == 0 or num2 % 9 == 0:
    print('число', num1, 'выиграло')
else:
    print('число', num2, 'выиграло')''' #число 34 выиграло

# Какое значение будет выведено на экран после выполнения следующей программы, если с клавиатуры введено число 7?

''' a = int(input())
if a >= 2 and a <= 17:
    b = 3
    p = a * a + b * b
else:
    b = 5
p = (a + b) * (a + b)
print(p)''' # 100

''' age = int(input('Сколько вам лет?: '))
grade = int(input('В каком классе вы учитесь?: '))
if age >= 12 and grade >= 7:
    print('Доступ разрешен.')
else:
    print('Доступ запрещен.')''' # Верный код

# Какое значение будет выведено на экран после выполнения следующей программы, если с клавиатуры введено число 7?
'''a = int(input())
if a >= 2 and a <= 17:
    b = 3
    p = a * a + b * b
else:
    b = 5
p = (a + b) * (a + b)
print(p)''' # Задание верно

# Задача 1. Напишите программу, которая определяет, является ли заданное натуральное число трёхзначным.
# Решение. Программа, решающая поставленную задачу, может иметь следующий вид:

'''num = int(input())
if 100 <= num <= 999:     # num >= 100 and num <= 999
    print('Число является трёхзначным')
else:
    print('Число не является трёхзначным')'''

# Задача 2. Напишите программу, которая проверяет, что все три цифры натурального трёхзначного числа различны.
# Решение. Программа, решающая поставленную задачу, может иметь следующий вид:

''' num = int(input())
d3 = num % 10
d2 = num % 100 // 10
d1 = num // 100
if d3 != d2 and d3 != d1 and d2 != d1:
    print('Цифры различны')
else:
    print('Цифры не различны')'''

# Задача 3. Напишите программу, которая по координатам точки, не лежащей на осях координат, определяет номер координатной четверти, в которой она находится.
# Решение. Программа, решающая поставленную задачу, может иметь следующий вид:

'''x = int(input())
y = int(input())

if x > 0 and y > 0:
    print('1 четверть')
if x < 0 and y > 0:
    print('2 четверть')
if x < 0 and y < 0:
    print('3 четверть')
if x > 0 and y < 0:
    print('4 четверть')'''

# Принадлежность 1
# Напишите программу, которая принимает целое число xx и определяет, принадлежит ли данное число указанному промежутку.

# Формат входных данных
# На вход программе подаётся целое число xx.

# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.
# Примечание. Если точка выколотая, то граница не включается, если точка закрашенная, то граница включается.
'''a = int(input())
if a > -1 and a < 17:
    print('Принадлежит')
else:
    print('Не принадлежит')''' # Задание верно

# Принадлежность 2
# Напишите программу, которая принимает целое число xx и определяет, принадлежит ли данное число указанным промежуткам.

# Формат входных данных
# На вход программе подаётся целое число xx.

# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.
''' x = int(input())
if x <= -3 or x >= 7:
    print('Принадлежит')
else:
    print('Не принадлежит')''' # Задание верно

'''x = int(input())
if x > -30 and x <= -2 or x > 7 and x <= 25:
    print('Принадлежит')
else:
    print('Не принадлежит')''' # 1 вариант решения задачи

#Красивое число 🌶️
#Назовем число красивым, если оно является четырехзначным и делится нацело на 7 или на 17.
#Напишите программу, определяющую, является ли введённое число красивым. Программа должна вывести «YES»,
#если число является красивым, или «NO» в противном случае.
#Формат входных данных
#На вход программе подаётся натуральное число.
#Формат выходных данных
#Программа должна вывести текст в соответствии с условием задачи.

age = int(input('Сколько вам лет?: '))
grade = int(input('В каком классе вы учитесь?: '))
city = input('В каком городе вы живете?: ')
if age >= 12 and grade >= 7 and (city == 'Москва' or city == 'Санкт-Петербург'):
    print('Доступ разрешен.')
else:
    print('Доступ запрещен.')'''

'''num = int(input())
if 999 < num <= 9999 and (num % 7 == 0 or num % 17 == 0):
    print('YES')
else:
    print('NO') # Верное решение

'''a = int(input())
b = int(input())
c = int(input())
if ((a < (b + c)) and (b < (a + c)) and (c < (a + b))) > 0:
    print('YES')
else:
    print('NO')''' # Верное решение
#Високосный год
# Напишите программу, которая определяет, является ли год с данным номером високосным.
# Если год является високосным, то выведите «YES», иначе выведите «NO».
# Год является високосным, если его номер кратен 4, но не кратен 100, или если он кратен 400.
#  Формат входных данных. На вход программе подаётся натуральное число.

'''y = int(input())
if (y // 400 and y // 4 or y % 100) > 0:
    print('YES')
else:
    print('NO')'''

'''y = int(input())
if ((y // 4 or y % 100) and (y // 400)) > 0:
    print('YES')
else:
    print('NO')'''