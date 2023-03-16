#Найдите сумму цифр трехзначного числа
val=input('Введите число: ')
summa=0
for (index, num) in enumerate(val):
    if num.isdigit()==True:
        summa+=int(num)
        print(num,'[',index,']')
    elif num==',' or num =='.':
        continue
    else:
        print(f'Введенное значение {num} не является числом')
print(f'Сумма числа = {summa}')