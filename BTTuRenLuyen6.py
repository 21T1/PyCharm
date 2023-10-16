# Câu 1: Cho list
# lst = [3, 0, 1, 5, 2]
# x = 2
# Hãy cho biết kết quả:
# (a) lst[0]              = 3
# (b) lst[3]              = 5
# (c) lst[x]              = 1
# (d) lst[-x]             = 5
# (e) lst[x + 1]          = 5
# (f) lst[x] + 1          = 2
# (g) lst[lst[x]]         = 0
# (h) lst[lst[list[x]]]   = 3

# Câu 2: Cho list
# lst = [20, 1, -34, 40, -8, 60, 1, 3]
# Hãy cho biết kết quả:
# (a) lst             = [20, 1, -34, 40, -8, 60, 1, 3]
# (b) lst[0:3]        = [20, 1, -34]
# (c) lst[4:8]        = [-8, 60, 1, 3]
# (d) lst[4:33]       = [-8, 60, 1, 3]
# (e) lst[-5:-3]      = [40, -8]
# (f) lst[-22:3]      = [20, 1, -34]
# (g) lst[4:]         = [-8, 60, 1, 3]
# (h) lst[:]          = [20, 1, -34, 40, -8, 60, 1, 3]
# (i) lst[:4]         = [20, 1, -34, 40]
# (j) lst[1:5]        = [1, -34, 40, -8]
# (k) -34 in lst      = True
# (l) -34 not in lst  = False
# (m) len(lst)        = 8

# Câu 3: Nhập vào 1 list có N số ngẫu nhiên không trùng nhau
from random import randrange

n = int(input("Nhập số phần tử, n: "))
lst = []
for i in range(n):
    x = randrange(n*100)
    while lst.count(x) != 0:
        x = randrange(n * 100)
    lst.append(x)
# lst.sort()
print(lst)

# Câu 4: Viết chương trình nhập vào một dãy các số theo thứ tự tăng,
# nếu nhập sai quy cách thì yêu cầu nhập lại,
# in dãy số sau khi đã nhập xong

n = int(input("Nhập số phần tử của dãy, n = "))
lst = []
for i in range(n):
    if i == 0:
        lst.append(int(input("Nhập giá trị, A[1] = ")))
    else:
        print("Nhập giá trị, A[{0}] = ".format(i + 1), end='')
        x = int(input())
        while x <= lst[i - 1]:
            print("Giá trị không hợp lệ!\nNhập lại, A[{0}] = ".format(i + 1), end='')
            x = int(input())
        lst.append(x)
print("Dãy đã nhập là: ", end='')
for item in lst:
    print(item, end=' ')
print()

# Câu 5: Viết chương trình nhập vào một dãy n số thực M[0], M[1],... M[n - 1],
# sắp xếp dãy số theo thứ tự giảm dần. Xuất ra dãy số sau khi sắp xếp
from random import randrange

n = int(input("Nhập số phần tử, n = "))
lst = []
for i in range(n):
    lst.append(randrange(1000)/100)
lst.sort(reverse=False)
for item in lst:
    print(item, end=' ')

# Câu 6: Viết chương trình nhập vào một mảng số tự nhiên. Hãy xuất ra màn hình:
# - Dòng 1: gồm các số lẻ, tổng cộng có bao nhiêu chữ số lẻ
# - Dòng 2: gồm các số chẵn, tổng cộng có bao nhiêu chữ số chẵn
# - Dòng 3: gồm các số nguyên tố
# - Dòng 4: gồm các số không phải là số nguyên tố
# M[] = {3, 6, 7, 8, 11, 17, 2, 90, 2, 5, 4, 5, 8}
# -> 3, 7, 11, 17, 5 (2) -> 6 số lẻ
def createList(n):
    """Create a list of n elements"""
    lst = []
    for i in range(n):
        print("Nhập giá trị, A[{0}] = ".format(i + 1), end='')
        x = int(input())
        lst.append(x)
    return lst


def printList(lst):
    """Print list lst"""
    for item in lst:
        print(item, end=' ')
    print()


def printOdd(lst):
    """Print and count the number of odd numbers in list lst"""
    print("->", end=' ')
    count = 0
    for item in lst:
        if item % 2 == 1:
            print(item, end=' ')
            count += 1
    print("->", count, "số lẻ")
    return count


def printEven(lst):
    """Print and count the number of even numbers in list lst"""
    print("->", end=' ')
    count = 0
    for item in lst:
        if item % 2 == 0:
            print(item, end=' ')
            count += 1
    print("->", count, "số chẵn")
    return count


def prime(x):
    """Check if x is prime number"""
    if x == 1:
        return False
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            return False
    return True


def printPrime(lst):
    """Print and count the number of prime numbers"""
    print("->", end=' ')
    count = 0
    for item in lst:
        if prime(item):
            print(item, end=' ')
            count += 1
    print("->", count, "số nguyên tố")
    return count


def printComposite(lst):
    """Print and count the number of composite numbers"""
    print("->", end=' ')
    count = 0
    for item in lst:
        if not prime(item):
            print(item, end=' ')
            count += 1
    print("->", count, "số không phải số nguyên tố")
    return count


n = int(input("Nhập số phần tử, n = "))
lst = createList(n)
printList(lst)
printOdd(lst)
printEven(lst)
printPrime(lst)
printComposite(lst)


# Câu 7:
# - Nhập 2 matrix A, B
# - Cộng 2 matrix
# - Viết hàm tính matrix hoán vị -> áp dụng để tìm matrix hoán vị của A, B
from random import randrange

def createMatrix(m, n):
    """Create a M x N matrix"""
    lst = []
    for i in range(m):
        row = []
        for j in range(n):
            # print("Nhập giá trị, A[{0}] = ".format(i + 1), end='')
            # x = int(input())
            x = randrange(100)
            row.append(x)
        lst.append(row)
    return lst


def printMatrix(lst):
    """Print list lst"""
    for row in lst:
        for column in row:
            print(column, end='\t')
        print()


def matrixAddition(A, B, m, n):
    """The addition of M x N matrix A and B """
    C = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(A[i][j] + B[i][j])
        C.append(row)
    return C


def transpose(A, m, n):
    """Return transpose of a M x N matrix A"""
    M = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(A[j][i])
        M.append(row)
    return M


m, n = map(int, input("Nhập kích thước ma trận: ").split())
A = createMatrix(m, n)
B = createMatrix(m, n)
print("Ma trận A:")
printMatrix(A)
print("Ma trận B:")
printMatrix(B)
C = matrixAddition(A, B, m, n)

print("Ma trận A + B = C:")
printMatrix(C)

print("Ma trận hoán vị/chuyển vị của A: ")
D = transpose(A, m, n)
printMatrix(D)
print("Ma trận hoán vị/chuyển vị của B: ")
D = transpose(B, m, n)
printMatrix(D)
