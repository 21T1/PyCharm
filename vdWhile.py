#Tính bình phương 1 số thuộc đoạn [1; 10]
x = -1
while x < 1 or x > 10:
    x = int(input("Nhập 1 số thuộc đoạn [1; 10]: "))
print(x, "^2 =", x**2)

#Tính tổng S = 1 + 2 + ... + N
n = int(input("Nhập N: "))
s = 0
i = 1
while i <= n:
    s += i
    i += 1
print("S =", s)