'''На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
 Выведите минимальное количество монет, которые нужно перевернуть'''
import os
import random

os.system('CLS')

n = int(input('Введите количество монет на столе:'))
coinvalue=['ОРЕЛ','РЕШКА']
heads, tails=(0,0)
#coinlist = [(i,random.choice(coinvalue)) for i in range(1,n+1)]
coinlist = [random.choice(coinvalue) for i in range(1,n+1)]
print(coinlist, type(coinlist), len(coinlist), '\n',)
for i in coinlist:
    print(i)
    if i=='ОРЕЛ':
        heads+=1
    else:
        tails+=1
if heads==0 or tails==0:
    print('Переворачивать монетки не требуется')    
elif heads>tails and tails!=0:
    print(f'Необходимо перевернуть {tails} монет чтобы все монеты на столе были ГЕРБОМ/ОРЛОМ вверх')
elif heads<tails and heads!=0:
    print(f'Необходимо перевернуть {heads} монет чтобы все монеты на столе были ГЕРБОМ/ОРЛОМ) вверх')
elif heads==tails:
    print(f'Необходимо перевернуть {heads} монет чтобы все монеты на столе были ГЕРБОМ/ОРЛОМ) вверх')