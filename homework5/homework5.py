def power(a, b):
    if (b == 1):
        return (a)
    if (b != 1):
        return a ** b

a = int(input("Введите число: "))
b = int(input("Введите степень числа: "))
print ("Результат равен: ", power(a, b))
 

