#ax^2 + bx + c = 0
from math import sqrt

print("Chương trình giải phương trình bậc 2:")
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))

if a == 0:
    #bx + c =0
    if b == 0 and c == 0:
        print("Vô số nghiệm")
    elif b == 0 and c != 0:
        print("Vô nghiệm")
    else:
        x = -c/b
        print("Nghiệm x =", round(x, 2))
else:
    delta = b**2 - 4*a*c
    if delta < 0:
        print("Vô nghiệm")
    elif delta == 0:
        x = -b/(2*a)
        print("Nghiệm kép x1 = x2 =", round(x, 2))
    else:
        x1 = -(b + sqrt(delta))/(2*a)
        x2 = -(b - sqrt(delta))/(2*a)
        print("Nghiệm x1 =", x1)
        print("Nghiệm x2 =", x2)
