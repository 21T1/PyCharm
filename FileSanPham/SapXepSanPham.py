from FileSanPham import readFile
from XuatFileSanPham import printList


def sortProduct(lst):
    """Sort product list lst in ascending order (ASC)"""
    for i in range(len(lst) - 1):
        for j in range(i, len(lst)):
            if eval(lst[i][2]) > eval(lst[j][2]):
                t = lst[i]
                lst[i] = lst[j]
                lst[j] = t


lstP = readFile("FileSanPham.txt")
sortProduct(lstP)
printList(lstP)
