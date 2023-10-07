a = int(input("Nhập số nguyên: "))
s = 0
for n in range(5, 10):
    if 4%a == 1:
        print("Ngừng vòng for")
        break
    s += n
else:
    print("S =", s)