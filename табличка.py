print("Введите данные")             # у меня не выводится print(b+c+b) в последней строке
print("Введите температуру:")
temp=input()
print("Введите влажность:")
vl=input()
print("Введите скорость ветра:")
veter=input()
print("Введите давление:")
davlenie=input()
print("Введите коментарий:")
comment=input()
a="-"
b="+"
c=a*58

temp=int(temp)

if temp<-10:
    write1="  Очень холодно"
elif temp<0:
    write1="  Холодно"
elif temp<10:
    write1="  Прохладно"
elif temp<20:
    write1="  Нормально"
elif temp<30:
    write1="  Тепло"
elif temp<10000000:
    write1="  Жарко"

temp=str(temp)

vl=int(vl)

if vl<10:
    write2="  Сухо"
elif vl<30:
    write2="  Немного влажно"
elif vl<50:
    write2="  Влажно"
elif vl<10000000000:
    write2="  ужас"

vl=str(vl)

veter=int(veter)

if veter<5:
    write3="  Слегка дует"
elif veter<15:
    write3="  Дует нормально"
elif veter<100000000:
    write3="  ОГО"

veter=str(veter)

davlenie=int(davlenie)

if davlenie<755:
    write4="  Низкое"
elif davlenie<760:
    write4="  Нормальное"
elif davlenie<100000000:
    write4="  Высокое"

davlenie=str(davlenie)

print(b+c+b)
def CreateTabl(leftpar, parametr, comment, write):    
    t="| " + leftpar 
    tt=(t+parametr+comment+write)
    r=(60-len(tt)-1)

    print(tt+" "*r+"|")

CreateTabl("Температура  " , temp, "  Гр. Ц.", write1)
CreateTabl("Влажность  " , vl, "  %", write2)
CreateTabl("Ветер  " , veter, "  м/с", write3)
CreateTabl("Давление  ", davlenie, "  мм. рт. ст.",write4)
CreateTabl(input())

print(b+c+b)