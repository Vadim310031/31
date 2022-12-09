print("Введите числа")
a=int(input())
h=int(input())
y=int(input())
d=int(input())
e=int(input())
l=int(input())
v=int(input())
j=int(input())
n=int(input())
s=int(input())
buf=a
if buf<h:
    buf=h
if buf<y:
    buf=y
if buf<d:
    buf=d
if buf<e:
    buf=e
if buf<l:
    buf=l
if buf<v:
    buf=v
if buf<j:
    buf=j
if buf<n:
    buf=n
if buf<s:
    buf=s
print("Больше всех оказалось число: ", buf)