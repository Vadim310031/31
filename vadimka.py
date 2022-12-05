print("Введите числа")
a=int(input())
print(id(a))
b=int(input())
print(id(b))
c=int(input())
print(id(c))
if a>b:
    if a>c:
        print(a, id(a))
    else:
        print(c, id(c))
else:
    if b>c:
        print(b, id(b))
    else:
        print(c, id(c))

