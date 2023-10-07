# Câu 1: Những giá trị có thể xuất hiện khi chạy randrange(0, 100) trong 4.5, 34, -1, 100, 0, 99
# -> 34 0 99

# Câu 2: Nhập tọa độ hai điểm A(xA,yA) và B(xB,yB). Tính và xuất độ dài đoạn AB

from math import sqrt

print("Nhập tọa độ điểm A:")
xa = float(input("xA = "))
ya = float(input("yA = "))

print("Nhập tọa độ điểm B:")
xb = float(input("xB = "))
yb = float(input("yB = "))

d = sqrt((xb - xa)**2 + (yb - ya)**2)
print("Độ dài đoạn AB =", d)

# Câu 3: Viết chương trình tính logax với a, x là các số thực nhp vào từ bàn phím, x > 0, a > 0, a != 1
from math import log

a = 0
x = 0
while a <= 0 or a == 1:
    a = float(input("Nhập a: "))
while x <= 0:
    x = float(input("Nhập x: "))
print("log{0}({1}) = {2}".format(a, x, log(x)/log(a)))

# Câu 4: Nhập n. Tính S(n) = sqrt(2 + sqrt(2 + sqrt( ... + sqrt(2)))) có n dấu căn lồng nhau
from math import sqrt

n = int(input("Nhập n: "))
s = 0
for i in range(1, n+1):
    s = sqrt(2 + s)
print("S =", s)
