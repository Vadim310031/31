print("Введите данные")
temp=input()
vl=input()
veter=input()
davlenie=input()
comment=input()
a="-"
b="+"
c=a*58

def CreateTabl(leftpar, parametr, comment):    
    t="| " + leftpar 
    tt=(t+parametr+comment)
    r=(60-len(tt)-1)

    print(tt+" "*r+"|")
print(b+c+b)

CreateTabl("Температура  " , temp, "  Гр. Ц.")
CreateTabl("Давление  " , vl, "  %")
CreateTabl("Ветер  " , veter, "  м/с")
CreateTabl("Давление  ", davlenie, "  мм. рт. ст.")
CreateTabl(input())

print(b+c+b)