'''
Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа
сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов,
чем Петя и Сережа вместе?
'''

x = int(input('Введите общее количество журавликов: '))
P = x // 6
S = x // 6
K = x - (P + S)

print('Петя - ' + str(int(P)), 'Катя - ' + str(int(K)), 'Серёжа - ' + str(int(S)))