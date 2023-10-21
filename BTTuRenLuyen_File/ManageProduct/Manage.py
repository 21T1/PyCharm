from SolveTextFile import *


def printList(lst):
    for item in lst:
        for i in range(len(item)):
            print(item[i], end='\t')
        print()


def printItem(lst, i):
    for j in range(len(lst[i])):
        print(lst[i][j], end='\t')
    print()


def add():
    n = int(input("Thêm mới:\n1. Danh mục\n2. Sản phẩm\n0. Hủy\n"))
    match n:
        case 1:
            cate = []
            cate.append(input("Nhập mã DM: "))
            cate.append(input("Nhập tên DM: "))
            lstCate.append(cate)
            printList(lstCate)
            data = cate[0] + "," + cate[1]
            writeFile("Category.txt", data)
        case 2:
            prod = []
            prod.append(input("Nhập mã SP: "))
            prod.append(input("Nhập tên SP: "))
            prod.append(input("Nhập giá SP: "))
            lstProd.append(prod)
            printList(lstProd)
            data = prod[0] + "," + prod[1] + "," + prod[2]
            writeFile("Product.txt", data)
        case 0:
            return 0
        case default:
            print("Lựa chọn không tồn tại")
            return 0


def edit():
    n = int(input("Chỉnh sửa:\n1. Danh mục\n2. Sản phẩm\n0. Hủy\n"))
    data = ""
    match n:
        case 0:
            return 0
        case 1:
            id = input("Nhập mã DM cần chỉnh sửa: ")
            for cate in lstCate:
                if cate[0] == id:
                    name = input("Tên DM mới: ")
                    cate[1] = name
            printList(lstCate)
        case 2:
            id = input("Nhập mã SP cần chỉnh sửa: ")
            for prod in lstProd:
                if prod[0] == id:
                    name = input("Tên SP mới: ")
                    price = input("Giá SP mới: ")
                    prod[1] = name
                    prod[2] = price
            printList(lstProd)
        case default:
            print("Lựa chọn không tồn tại")
            return 0


def search():
    n = int(input("Tìm kiếm:\n1. Danh mục\n2. Sản phẩm\n0. Hủy\n"))
    match n:
        case 0:
            return 0
        case 1:
            name = input("Nhập tên DM cần tìm kiếm: ")
            for i in range(len(lstCate)):
                if name.upper() in lstCate[i][1].upper():
                    printItem(lstCate, i)
        case 2:
            name = input("Nhập tên SP cần tìm kiếm: ")
            for i in range(len(lstProd)):
                if name.upper() in lstProd[i][1].upper():
                    printItem(lstProd, i)
        case default:
            print("Lựa chọn không tồn tại")
            return 0


def delete():
    n = int(input("Xóa:\n1. Danh mục\n2. Sản phẩm\n0. Hủy\n"))
    match n:
        case 0:
            return 0
        case 1:
            id = input("Nhập mã DM cần xóa: ")
            for i in range(len(lstCate)):
                if lstCate[i][0] == id:
                    del lstCate[i]
            printList(lstCate)
        case 2:
            id = input("Nhập mã SP cần xóa: ")
            for i in range(len(lstProd)):
                if lstProd[i][0] == id:
                    del lstProd[i]
            printList(lstProd)
        case default:
            print("Lựa chọn không tồn tại")
            return 0


def sort(lst):
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if lst[i][1] > lst[j][1]:
                t = lst[i]
                lst[i] = lst[j]
                lst[j] = t
    printList(lst)


lstCate = readFile("Category.txt")
lstProd = readFile("Product.txt")
printList(lstProd)
printList(lstCate)
# add()
sort(lstCate)
sort(lstProd)
# search()
# delete()
# edit()