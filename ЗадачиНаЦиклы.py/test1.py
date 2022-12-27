a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
while a != b:
    if a<b:
        print(a)
        c=a**3
        print(c)
        a=a+1
    elif a>b:
        print(a)     
        c=a**3
        print(c)
        a=a-1
   
    