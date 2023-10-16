from random import randrange


def createMatrix(m, n):
    """Create a random M x N matrix """
    lst = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(randrange(100))
        lst.append(row)
    return lst


def printMatrix(A):
    """Print a matrix M"""
    for row in A:
        for column in row:
            print(column, end='\t')
        print()


def printRow(r, A):
    for item in A[r - 1]:
        print(item, end='\t')
    print()


def printColumn(c, A):
    for i in A:
        print(i[c - 1])


def maxValue(A):
    max = A[0][0]
    for row in A:
        for column in row:
            if max < column:
                max = column
    return max


m, n = map(int, input("Nhập giá trị m, n: ").split())
lst = createMatrix(m, n)
printMatrix(lst)
r = int(input("Nhập dòng muốn xuất: "))
printRow(r, lst)
c = int(input("Nhập cột muốn xuất: "))
printColumn(c, lst)
print("Số lớn nhất trong mảng là", maxValue(lst))
