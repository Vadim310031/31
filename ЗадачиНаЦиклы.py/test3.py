#Вычислить факториал числа, которое ввел пользователь.
number = int(input("Введите число "))
c = number-1
while c >= 1:
    number=number*c
    c=c-1
else:
    number=number*c
    c=c+1
print(number)