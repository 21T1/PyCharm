def FibNum(n):
    """Calculate the [n] term of Fibonancci Sequence"""
    if n <= 2:
        return 1
    else:
        return FibNum(n - 1) + FibNum(n - 2)


def FibSeq(n):
    """Find the first n terms of Fibonancci Sequence"""
    if n == 1:
        return "1"
    elif n == 2:
        return FibSeq(1) + " -> 1"
    else:
        return FibSeq(n - 1) + " -> {0}".format(FibNum(n - 1) + FibNum(n - 2))


while True:
    n = int(input("Nhập N: "))
    if n < 1:
        print("N không hợp lệ")
    else:
        print("F({0}) = {1}".format(n, FibNum(n)))
        print("Dãy", n, "phần tử đầu tiên của dãy Fibonancci:\n", FibSeq(n))
    if(input("Tiếp tục chương trình (c/k)? ")) == "k":
        break
print("Chương trình kết thúc")
