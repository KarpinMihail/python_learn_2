'''name = int(input())
print(name)
print(name + int(1))
print(name + int(2))

a = int(input())
b = int(input())
c = int(input())
print(int(a + b + c))

a = int(input())
print('Объем =', int(a*a*a))
print('Площадь полной поверхности =', int(6*(a*a)))

a = int(input())
b = int(input())
print(3 * (a + b)**3 + 275 * b**2 - 127 * a - 41)


a = int(input())
print('Следующее за числом', int(a), 'число:', int(a + 1))
print('Для числа', int(a), 'предыдущее число:', int(a - 1))

# Программа считает стоимость 3х компьютеров разной конфигурации, состоящих из монитора, системного блока, клавиатуры, мышки

# comp1
print('Введите стоимость copm1:')
a1 = int(input())
b1 = int(input())
c1 = int(input())
d1 = int(input())
sum1 = int(a1 + b1 + c1 + d1)
print('Стоимость 1 компьютера:', int(sum1))
# comp2
print('Введите стоимость copm2:')
a2 = int(input())
b2 = int(input())
c2 = int(input())
d2 = int(input())
sum2 = int(a2 + b2 + c2 + d2)
print('Стоимость 2 компьютера:', int(sum2))
# comp3
print('Введите стоимость copm3:')
a3 = int(input())
b3 = int(input())
c3 = int(input())
d3 = int(input())
sum3 = int(a3 + b3 + c3 + d3)
print('Стоимость 3 компьютера:', int(sum3))
print('Итоговая стоимость за 3 компьютера:', int(sum1 + sum2 + sum3))

# Программа считает стоимость 3х компьютеров одинаковой конфигурации, состоящих из монитора, системного блока, клавиатуры, мышки

print('Введите стоимость copm:')
a = int(input())
b = int(input())
c = int(input())
d = int(input())
sum1 = int(3*(a + b + c + d))
print('Стоимость 3х компьютера:', int(sum1))

# Арифметические операции
# Напишите программу, в которой вычисляется сумма, разность и произведение двух целых чисел, введенных с
# На вход программе подается два целых числа, каждое на отдельной строке

a = int(input())
b = int(input())
sum1 = (a + b)
dif1 = (a - b)
com1 = (a * b)
print(int(a), '+', int(b), '=', int(sum1))
print(int(a), '-', int(b), '=', int(dif1))
print(int(a), '*', int(b), '=', int(com1))

# Арифметическая прогрессия a1, a2,..., a(n)
 a(n) = a((n) - 1) + d
 a(n) = a1 + d * (n - 1)

a1 = int(input())
d = int(input())
n = int(input())
an = int(a1 + d * int(n - 1))
print(int(an))

# Разделяй и влавствуй. Напиши програму, которая считывает целое положительное число x
# и выводит на экран последовательность чисел x, 2x,3x,4x и 5x, разделенных тремя черточками.

x = int(input())
dif1 = int(x)
dif2 = int(2 * x)
dif3 = int(3 * x)
dif4 = int(4 * x)
dif5 = int(5 * x)
# print(int(dif1), '---', int(dif2), '---', int(dif3), '---', int(dif4), '---', int(dif5))
print(int(dif1), int(dif2), int(dif3), int(dif4), int(dif5), sep = '---')'''