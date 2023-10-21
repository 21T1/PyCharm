from SolveTextFile import readFileTxt


def sum(arr):
    s = 0
    for x in arr:
        s += int(x)
    return s


arrNum = readFileTxt("Number.txt")
for i in range(10):
    print("Tổng dòng", i + 1, ":\t", sum(arrNum[i]))
