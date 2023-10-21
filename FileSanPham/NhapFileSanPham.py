from FileSanPham.FileSanPham import *


def createNewProduct():
    """Create a new product"""
    id = input("Nhập mã SP: ")
    name = input("Nhập tên SP: ")
    price = float(input("Nhập giá SP: "))
    return id + ";" + name + ";" + str(price)

# writeFile("FileSanPham.txt", createNewProduct())
