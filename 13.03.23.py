computer = int(input("kompyteroB: "))
A = int(input("A: "))
B = int(input("B: "))
C = int(input("C: "))

if B != 0:
    B = B + 1
if C != 0:
    C = C * 2 +1


count = B + C - 1
if count < 0:
    count = count *(-1)

if count < computer:
    print(count)
else:
    print(computer)