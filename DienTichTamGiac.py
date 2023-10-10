from math import *

print("Chương trình tính diện tích tam giác theo độ dài 3 cạnh")
a, b, c = eval(input("Nhập 3 cạnh của tam giác: "))
if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
    print("Độ dài 3 cạnh không hợp lệ")
else:
    C = a + b + c
    p = C/2
    S = sqrt(p*(p-a)*(p-b)*(p-c))
    print("Diện tích:", S)