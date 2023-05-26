#Задача 34: Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой 
#фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, 
#то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух 
#вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке 
#и “Пам парам”, если с ритмом все не в порядке

#**Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#    **Вывод:** Парам пам-пам 

"""
line = input()
print(line)

def mixer(character):
    vowels_set = {"а", "у", "я", "и", "ю", "ы", "о", "э", "е"}
    return character in vowels_set

a = list(map(lambda x: len(list(filter(mixer, x))), line.split(' ')))

result = "Парам пам-пам"
for i in range(len(a)-1): 
    if a[i] != a[i+1]:
        result = "Пам парам"
        break
print(result)


#Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве аргумента функцию, 
#вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны 
#быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). Примечание: бинарной операцией называется любая 
#операция, у которой ровно два аргумента, как, например, у операции умножения.

#Пример:*

#**Ввод:** `print_operation_table(lambda x, y: x * y) ` 
#**Вывод:**
"""
from itertools import repeat

num_row = int(input("Введите количество строк "))

def amount_of_num_row(num_row):
    return num_row >= 1

num_column = int(input("Введите количество столбцов "))

def amount_of_num_column(num_column):
    return num_column >= 1

def print_operation_table(operation_func, num_row, num_column):
    b = [x for x in range(1, num_row+1)]
    matrix = []
    for i in range(1, num_column+1):
        matrix.append(list(map(operation_func, repeat(i), b)))
    return matrix

result = print_operation_table(lambda x, y: x*y, num_row, num_column)
for row in result:
    print(row)
"""
