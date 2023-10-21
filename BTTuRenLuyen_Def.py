# Câu 1: Cho 3 hàm dưới đây:
def sum1(n):
    s = 0
    while n > 0:
        s += 1
        n -= 1
    return s

def sum2():
    global val
    s = 0
    while val > 0:
        s += 1
        val -= 1
    return s

def sum3():
    s = 0
    for i in range(val, 0, -1):
        s += 1
    return s

# Hãy cho biết kết quả sau khi gọi các lệnh trên:
# a
def main():
    global val
    val = 5
    print(sum1(5))  # 5
    print(sum2())   # sum2 = 0 and val = 0
    print(sum3())   # val = 0 -> sum3 = 0

main()

# b
def main():
    global val
    val = 5
    print(sum1(5))  # 5
    print(sum3())   # 5
    print(sum2())   # val = 5 -> sum2 = 5

main()

# c
def main():
    global val
    val = 5
    print(sum2())   # sum2 = 5 and val = 0
    print(sum1(5))  # 5
    print(sum3())   # val = 0 -> sum3 = 0

main()

# Câu 3: Cho đoạn code:
# for n in oscillate(-3, 5):
#     print(n, end=' ')
# print()
# Hãy viết hàm oscillate để khi chạy phần mềm nó ra kết quả:
# -3 3 -2 2 -1 1 0 0 1 -1 2 -2 3 -3 4 -4
def oscillate(a, b):
    if a + 1 == b:
        return "{0} {1}".format(a, -a)
    else:
        return oscillate(a, b - 1) + " {0} {1}".format(b - 1, -(b - 1))

for n in oscillate(-3, 5):
    print(n, end='')
print()

# Câu 4: Viết hàm tính tổng ước số để áp dụng chung cho 2 bài dưới đây:
def SumDivisor(n):
    s = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            s += i
    return s

# 4.1: Kiểm tra số nguyên dương n có phải là số hoàn thiện Perfect Number hay không?
# SHT là số có tổng các ước số của nó (không kể nó) bằng chính nó.
# vd: 6 có các ước số 1, 2, 3 và 1 + 2 + 3 = 6 -> 6 là SHT
def PerfectNum(n):
    if SumDivisor(n) == n:
        return "là số hoàn thiện"
    return "không là số hoàn thiện"

# 4.2: Kiểm tra số nguyên dương n có phải là số thịnh vượng Abundant Number hay không?
# STV là số có tổng các ước số của nó (không kể nó) lớn hơn nó.
# vd: 12 có các ước số 1, 2, 3, 4, 6 và 1 + 2 + 3 + 4 + 6 > 12 -> 12 là STV
def AbundantNum(n):
    if SumDivisor(n) > n:
        return "là số thịnh vượng"
    return "không là số thịnh vượng"

n = int(input("Nhập N: "))
print("Tổng ước số:", SumDivisor(n))
print(n, PerfectNum(n))
print(n, AbundantNum(n))
