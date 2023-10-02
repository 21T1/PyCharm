import math

try:
    r = float(input("Nhập bán kính hình tròn, r = "))
    print("Chu vi:", 2 * math.pi * r)
    print("Diện tích:", math.pi * r ** 2)
except:
    print("Lỗi!")
