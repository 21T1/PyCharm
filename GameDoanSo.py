from random import randrange

while True:
    print("*"*30)
    print("Tìm x, biết x thuộc [1; 100]")
    x = randrange(1,101)
    count = 1
    while count <= 7:
        print("Lượt đoán số", count)
        n = int(input("Nhập 1 số: "))
        count += 1
        if n < x:
            print("Số vừa đoán < Số cần tìm")
        elif n > x:
            print("Số vừa đoán > Số cần tìm")
        else:
            print("Chúc mừng bạn đã đoán đúng, x =", x)
            break
    else:
        print("GAMER OVER! Số cần tìm là:", x)
    if input("Tiếp tục? (c/k): ") == "k":
        print("END GAME")
        exit()