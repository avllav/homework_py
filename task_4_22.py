'''Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
Затем пользователь вводит сами элементы множеств.'''

# функция для проверки, является ли строка целым числом
def is_integer(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

# ввод количества элементов первого множества
while True:
    n_input = input("Введите количество элементов первого множества: ")
    if is_integer(n_input):
        n = int(n_input)
        break
    else:
        print("Ошибка: введите целое число")

# ввод количества элементов второго множества
while True:
    m_input = input("Введите количество элементов второго множества: ")
    if is_integer(m_input):
        m = int(m_input)
        break
    else:
        print("Ошибка: введите целое число")

# ввод элементов первого множества
set1 = set()
print("Введите элементы первого множества:")
for i in range(n):
    while True:
        element_input = input(f"Элемент {i+1}: ")
        if is_integer(element_input):
            set1.add(int(element_input))
            break
        else:
            print("Ошибка: введите целое число")

# ввод элементов второго множества
set2 = set()
print("Введите элементы второго множества:")
for i in range(m):
    while True:
        element_input = input(f"Элемент {i+1}: ")
        if is_integer(element_input):
            set2.add(int(element_input))
            break
        else:
            print("Ошибка: введите целое число")

# вывод пересечения множеств
intersection = sorted(list(set1 & set2))
print("Пересечение множеств:", intersection)
