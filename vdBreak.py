while True:
    n = int(input("Nhập vào 1 số: "))
    print(n, "là số chẵn" if n%2 == 0 else "là số lẻ")
    cont = input("Tiếp tục? c/k - ")
    if cont == "k":
        break
print("Bye!")

n = int(input("Nhập N: "))
s = 0
for i in range(1, n+1):
    s += i
    if s >= 15:
        break
print("S =", s)