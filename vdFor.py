n = int(input("Nhập n: "))
s = 0
if n%2 == 0:
    for i in range(2, n+1, 2):
        s += i
else:
    for i in range(1, n+1, 2):
        s += i
print("S =", s)