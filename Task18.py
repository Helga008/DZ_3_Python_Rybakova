# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

from random import randint
n = int(input('Введите размер массива: '))
list_1 = [randint(1,10) for _ in range(n)]
print(list_1)

x = int(input('Введите положительное число '))
diff_1 = abs(x - list_1[0])
index = 0

for i in range(1, n):
    diff_2 = abs(x - list_1[i])
    if diff_2 < diff_1:
        diff_1 = diff_2
        index = i
print(list_1[diff_1])        



