'''
Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

**
'''
import math
cranes=float(input('Введите количество журавликов:'))
k=((cranes/3)*2)
p=(k/2)
s=(p)
print('%1s %1s %8s' % ('---','-','-----------------\n'
                                        '%1s %3s %8s' % ('Катя', math.trunc(k),'\n'
                                        '%1s %4s %8s' % ('Петя', math.trunc(p),'\n'
                                        '%1s %2s' % ('Сережа сделал', math.trunc(s))))
                                        )
)