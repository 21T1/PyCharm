from random import randrange

n = int(input("Nhập số phần tử: "))
lst = [0] * n
for i in range(n):
    lst[i] = randrange(-100, 100)
print(lst)
print("Duyệt theo Collection:")
for x in lst:
    print(x, end='\t')
print("\nDuyệt theo index:")
for i in range(len(lst)):
    print(lst[i], end='\t')
print("\nDuyệt ngược:")
for i in range(len(lst) - 1, -1, -1):
    print(lst[i], end='\t')

# insert
lst = [1, 2, 3]
print(lst)
lst.insert(0, 999)
print(lst)
lst.insert(4, 777)
print(lst)
lst.insert(2, 555)
print(lst)

# append(n) = insert(len(lst), n)
lst = [1, 2, 3]
print(lst)
lst.append(999)
print(lst)
lst.append(777)
print(lst)
lst.append(([333, 555]))
print(lst)

# remove(n)
lst = [10, 20, 30, 40, 50]
lst.remove(20)
print(lst)
# del lst[i]
del lst[2:4]
print(lst)
del lst[0], lst[0]
print(lst)

# reverse
lst = [2, 0, 2, 3]
print(lst)
lst.reverse()
print(lst)
lst2 = reversed(lst)
for item in lst2:
    print(item, end=' ')
lst = ["Một", "Hai", """Ba
Bốn
Năm"""]
lst.reverse()
print(lst)

# sort
lst = [2, 0, 2, 3]
lst2 = sorted(lst)
print("lst2 = ", end='')
for item in lst2:
    print(item, end=' ')
print("\nlst =", lst)
lst.sort()
print("after sorted:", lst)
lst.sort(reverse=True)
print("reversed:", lst)

n, m = eval(input("Nhập vào số dòng và số cột (vd 3, 2): "))
arr2D = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(randrange(0, 100))
    arr2D.append(row)

print("Mảng 2 chiều", n, "x", m, "ngẫu nhiên:")
for row in arr2D:
    for column in row:
        print(column, end='\t')
    print()
