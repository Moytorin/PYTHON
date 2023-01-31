# Уровень 1:
# 1 действие
# 2 аргумента 12 + 15

# n = "12 + 15"
# m = n.split()
# print(m)

# a = int(m[0])
# b = m[1]
# c = int(m[2])

# def calc(a, b, c):
#     if b == "+":
#         return a + c
# print("a + c =", a+c)


# Уровень 2:
# Количество действий произвольное
# 12 + 15 - 4

# n = "12 + 15 - 4"
# m = n.split()
# print(m)
# m2 = []

# a = int(m[0])
# b = m[1]
# c = int(m[2])
# d = m[3]
# e = int(m[4])

# def calc(a, b, c):
#     if b == "+" and d == "-":
#         return a + c - e
# print(a + c - e)