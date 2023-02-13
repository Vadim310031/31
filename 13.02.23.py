print("Начало праграммы")
stroka = input("BBod clova:")
n = len(stroka)
nn = n-1
neq = ""
if n % 2 == 0:


    while nn >= 0:
        new = stroka[nn]
        nn = nn - 1
        neq = neq + new
        
    print(neq)
else:
    f = n//2
    neq = stroka[f]
    while nn >=0:
        new = stroka[nn]
        nn = nn - 1
        neq = neq + new
        if nn == f:
            nn = nn - 1
    print(neq)
