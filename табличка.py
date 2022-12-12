print("Введите данные")
temp=input()
vl=input()
veter=input()
davlenie=input()
comment=input()
a="-"
b="+"
c=a*58
print(b+c+b)

t="| Температура: "
tt=(t+temp+" гр Цельсия ")
r=(60-len(tt)-1)

print(tt+" "*r+"|")

t="| Влажность: "
tt=(t+vl+" % ")
r=(60-len(tt)-1)

print(tt+" "*r+"|")

