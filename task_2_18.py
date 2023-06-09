'''
Требуется найти в массиве A [1..N] самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
'''

import os
os.system('CLS')

n = str(input('Введите количество элементов в массиве [A]:> '))
x = str(input('Введите число которому нужно найти самый близкий элемент в массиве:> '))
if n.isdigit() == False:
    print(f'Введенное значение [{n}] не является цифрой')
elif x.isdigit() == False:
     print(f'Введенное значение [{x}] не является целым числом')  
elif x.isdigit() == True and n.isdigit() == True:
    from random import randint    
    list_x = [randint(1,100) for i in range(int(n))] #имитация ввода значений массива в заданой размерности
    print(f'Массив [A] для поиска {list_x}')
    close_x = [abs(list_x[i]-int(x)) for i in range(len(list_x))]
    print(f'Наиболее близкий по величине элемет числа {x} в массиве [A] = {list_x[close_x.index(min(close_x))]}')