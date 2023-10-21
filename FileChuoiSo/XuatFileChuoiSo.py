from FileChuoiSo import *


def printNegativeNum(lst):
    """Print all negative numbers in list lst"""
    for arr in lst:
        for x in arr:
            if int(x) < 0:
                print(x, end='\t')
        print()


arrNum = readFile("FileChuoiSo.txt")
print("Các số âm trên mỗi dòng:")
printNegativeNum(arrNum)