while True:
    n = int(input("Nhập 1 số: "))
    for i in range(2,n):
        if n%i == 0:
            print(n, "không là số nguyên tố")
            break
    else:
        print(n, "là số nguyên tố")
    s = input("Tiếp tục? c/k: ")
    if s == "k":
        exit()
print("Bye!")