# Task 10 Задача с переворотом монет
# import random 
# n = 5
# m = []
# count = 0
# count1 = 0
# max = 0
# for i in range(0, n):
#     random_number = round(random.uniform(0,1))
#     m.append(random_number)
#     if m[i] == 0: count += 1
#     if m[i] == 1: count1 +=1
# if count < count1:
#     print('Необходимо перевернуть', count, 'монет')
# else:
#     count > count1
#     print('Необходимо перевернуть', count1, 'монет')

# print(m)


# Task 12 Петя и Катя. Он называет сумму этих чисел S и их произведение P.
# s = int(input('Сумма чисел равна= '))
# p = int(input('Произведение чисел равно= '))
# x = None
# y = None
# x1 = None
# x2 = None
# d = s**2 - 4*p
# print ('Discreminant =',d)
# import math
# x1 = (s - math.sqrt(d))/ 2
# x2 = (s + math.sqrt(d))/ 2
# print(x1)
# print(x2)

# Task 14 Степени числа 2 до чсила N включительно
m = int(input('В какую степень возвести = '))
n = int(input('До какой степени возводить = '))
import math
while m<=n :
    print(math.pow(2, m))
    m+=2
    










