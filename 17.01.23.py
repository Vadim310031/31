def bi(a:int):
    c = ""
    while a>1:
        
        c = str(a%2)+c
        a = a//2
    c = str(a)+c
    return c
def vos(a:int):
    k = ""
    while a>7:
        
        k = str(a%8)+k
        a = a//8
    k = str(a)+k
    return k
print(vos(17499))
