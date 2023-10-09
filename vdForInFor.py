# draw N with for
n = int(input("Nhập chiều cao: "))
for i in range(n):
    for j in range(n):
        if j == 0 or j == i or j == n-1:
            print("*", end='')
        else:
            print(" ", end='')
    print()
print("#"*20)
# draw N with while
i = 0
while i < n:
    j = 0
    while j < n:
        if j == 0 or j == n-1 or j == i:
            print(".", end='')
        else:
            print(" ", end='')
        j += 1
    print()
    i += 1
print("#"*20)

# draw triangle
for i in range(n):
    for j in range(n):
        if j == 0 or j == i or i == n-1:
            print("*", end='')
        else:
            print(" ", end='')
    print()