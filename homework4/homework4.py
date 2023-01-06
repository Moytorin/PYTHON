# Задача 22:
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа.
# n - кол-во элементов первого набора.
# m - кол-во элементов второго набора.
# Значения генерируются случайным образом.

# Input: 11 6
# (значения сгенерированы случайным образом
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18)

# Output: 11 6
# 6 12

n = int(input('Введите кол-во элементов первого набора: '))
m = int(input('Введите кол-во элементов второго набора: '))
import random
n_array = []
m_array = []
for i in range(n):
    n_array.append(random.randint(0, n))
print(n_array)
for j in range(m):
    m_array.append(random.randint(0, m))
print(m_array)
c = []
for i in n_array:
    for j in m_array:
        if i == j:
            c.append(i)
            break
c.sort()    
print(c)
list2 = []
for item in c:
    if item not in list2:
        list2.append(item)
print(list2)



