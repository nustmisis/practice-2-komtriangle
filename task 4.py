# -*- coding: utf-8 -*-
"""
Взгляните на показанный ниже
код, в котором используется цикл while и флаг found
для поиска в списке тепеней 2 занания 2, вовзевдённую в пятую степень

@author: workk
"""

L = [1, 2, 4, 8, 16, 32, 64]
X = 5
found = False
i = 0
while not found and i < len(L):
    if 2 ** X == L[i]:
        found = True
    else:
        i = i + 1

if found:
    print('at index', i)
else:
    print(X, 'not found')


'''
Код явно написан с использование альетрнативной логики.
Попоробуйте оптимизировать код c использование рекомендаций, ониявляются не обезатальными, но помогут понять основные ошибки.
а)Сначала перепишите код с конструкцией else цикла while, чтобы избавиться от флага found и финального оператора if.
б) Затем перепишите код для использования цикла for с конструкцией else,
чтобы избавиться от явной логики индексации списка. (Подсказка: для получения индекса элемента применяйте списковый метод index — L. index (X)
возвращает смещение первого элемента X в списке L.)
в) Далее полностью устраните цикл, переписав код с использованием простого
выражения с операцией членства in. (За дополнительными сведениями обращайтесь в главу 8 или наберите для тестирования 2 in [1,2,3].)
г) Наконец примените цикл for и списковый метод append для генерации списка степеней 2 (L) вместо жесткого кодирования спискового литерала.
Ниже приведены более глубокие рассуждения.
д) Как вы думаете, улучшит ли производительность перенос выражения 2 ** X
за пределы циклов? Каким образом вы представили бы это в коде?
е)  Python содержит инструмент тар (функция, список), который также способен генерировать список степеней 2:. Каким образом можно его задать ? 
    
'''

# a

L = [1, 2, 4, 8, 16, 32, 64]
X = 5
i = 0
while i < len(L):
    if 2 ** X == L[i]:
        print('at index', i)
        break
    else:
        i = i + 1
else:
    print(X, 'not found')

# б

L = [1, 2, 4, 8, 16, 32, 64]
X = 5
for l in L:
    if 2 ** X == l:
        print('at index', L.index(l))
        break
else:
    print(X, 'not found')

# в

L = [2**i for i in range(7)]
X = 5

if 2 ** X in L:
    print('at index', L.index(l))
else:
    print(X, 'not found')

#г

L = [1, 2, 4, 8, 16, 32, 64]
X = 5

if 2 ** X in L:
    print('at index', L.index(l))
else:
    print(X, 'not found')

#д
'''
Да, улучшит. когда выражение  2 ** X находится
в цикле, то оно считается на каждой итерации этого цикла.
Если разместить это выражение перед циклом, то 
оно будет расчитано единожды
'''

#e
L = list(map(lambda x: 2 ** x, range(0,7)))
X = 5

if 2 ** X in L:
    print('at index', L.index(l))
else:
    print(X, 'not found')