from FileSanPham import *


def printList(dtb):
    """Print list dtb"""
    print("Mã SP\tTên SP\tGiá SP")
    print("_" * 30)
    for line in dtb:
        for info in line:
            print(info, end='\t')
        print()

# printList(readFile("FileSanPham.txt"))
