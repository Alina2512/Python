#Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
#*Пример:*
#A = 3; B = 5 -> 243 (3⁵)
#A = 2; B = 3 -> 8 
"""
numb_A = int(input("Введите число A "))
numb_B = int(input("Введите число B "))

def degree(numb_A, numb_B):
    if numb_B == 1:
        return numb_A
    else:
        return numb_A * degree(numb_A, numb_B - 1)

print(degree(numb_A, numb_B))
"""


#Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
#*Пример:*
#2 2   4 

numb_A = int(input("Введите число A "))
numb_B = int(input("Введите число B "))

def sum(numb_A, numb_B):
    if numb_B == 0:
        return numb_A
    else:
        return sum(numb_A, numb_B - 1) + 1

print(sum(numb_A, numb_B))

