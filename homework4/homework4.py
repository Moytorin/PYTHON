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

# n = int(input('Введите кол-во элементов первого набора: '))
# m = int(input('Введите кол-во элементов второго набора: '))
# import random
# n_array = []
# m_array = []
# for i in range(n):
#     n_array.append(random.randint(0, n))
# print(n_array)
# for j in range(m):
#     m_array.append(random.randint(0, m))
# print(m_array)
# c = []
# for i in n_array:
#     for j in m_array:
#         if i == j:
#             c.append(i)
#             break
# c.sort()    
# print(c)
# list2 = []
# for item in c:
#     if item not in list2:
#         list2.append(item)
# print(list2)






# Задача 24
# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены 
# только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов. 
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – 
# на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего 
# модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым 
# кустом, собирает ягоды с этого куста и с двух соседних с ним.

# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий 
# модуль, находясь перед некоторым кустом заданной во входном файле грядки.

# Input: 4
# (значения сгенерированы случайным образом
# 4 2 3 1 )

# Output: 9

m = int(input('Введите кол-во кустов: '))
import random
m_array = []
for item in range(m):
    m_array.append(random.randint(1, 10))
print(m_array)

max_ = m_array[0]
for item in m_array:
    if item > max_:
         max_ = item
c = []
c.append(max_)
m_array.remove(max_)

max_ = m_array[0]
for item in m_array:
    if item > max_:
         max_ = item
c.append(max_)
m_array.remove(max_)

max_ = m_array[0]
for item in m_array:
    if item > max_:
         max_ = item
c.append(max_)
m_array.remove(max_)

print(c)

result = c[0] + c[1] + c[2]
print(result)



