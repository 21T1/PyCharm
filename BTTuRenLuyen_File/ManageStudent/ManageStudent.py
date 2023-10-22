from SolveTextFile import *


def strData(item):
    """return string format 'item[0],item[1],...,item[n]'"""
    s = ""
    for i in range(len(item)):
        s += item[i] + ","
    return s[:len(s) - 1]


def add():
    """add new student/class to list and text file"""
    print("Thêm mới:\n1. Sinh viên\n2. Lớp\n0. Hủy")
    n = int(input("Nhập lựa chọn: "))
    match n:
        case 0:
            return 0
        case 1:
            std = [
                input("Nhập mã SV: "),
                input("Nhập tên SV: "),
                input("Nhập ngày sinh: "),
                input("Nhập mã lớp: ")
            ]
            lstStd.append(std)
            writeFile("Student.txt", strData(std))
            printList(lstStd)
        case 2:
            cls = [
                input("Nhập mã lớp: "),
                input("Nhập tên lớp: ")
            ]
            lstCls.append(cls)
            writeFile("Student.txt", strData(cls))
            printList(lstCls)
        case default:
            print("Lựa chọn không hợp lệ")
            return 0


def searchID(lst, id):
    """return index of item which id = id"""
    for i in range(len(lst)):
        if lst[i][0].upper() == id.upper():
            return i
    return -1


def search():
    """search for student/class in list"""
    print("Tìm kiếm:\n1. Sinh viên\n2. Lớp\n0. Hủy")
    n = int(input("Nhập lựa chọn: "))
    match n:
        case 0:
            return 0
        case 1:
            name = input("Nhập tên SV: ")
            for i in range(len(lstStd)):
                if name.upper() in lstStd[i][1].upper():
                    printItem(lstStd, i)
        case 2:
            name = input("Nhập tên lớp: ")
            for i in range(len(lstCls)):
                if name.upper() in lstCls[i][1].upper():
                    printItem(lstCls, i)
        case default:
            print("Lựa chọn không hợp lệ")
            return 0


def printItem(lst, index):
    """print lst[index]"""
    for i in range(len(lst[index])):
        print(lst[index][i], end='\t')
    print()


def printList(lst):
    """print list lst"""
    for i in range(len(lst)):
        printItem(lst, i)


def edit():
    """edit existing student/class's information in list"""
    print("Chỉnh sửa thông tin:\n1. Sinh viên\n2. Lớp\n0. Hủy")
    n = int(input("Nhập lựa chọn: "))
    match n:
        case 0:
            return 0
        case 1:
            id = input("Nhập mã SV: ")
            index = searchID(lstStd, id)
            if index != -1:
                printItem(lstStd, index)
                while True:
                    print("Chỉnh sửa:\n1. Mã SV\n2. Họ và tên\n3. Ngày sinh\n4. Lớp\n0. Thoát")
                    c = int(input())
                    match c:
                        case 0:
                            return 0
                        case 1:
                            lstStd[index][0] = input("Nhập mã mới: ")
                        case 2:
                            lstStd[index][1] = input("Nhập họ và tên mới: ")
                        case 3:
                            lstStd[index][2] = input("Nhập ngày sinh mới: ")
                        case 4:
                            lstStd[index][3] = input("Nhập mã lớp mới: ")
                        case default:
                            print("Lựa chọn không hợp lệ")
            else:
                print("Mã SV không tồn tại")
        case 2:
            id = input("Nhập mã lớp: ")
            index = searchID(lstCls, id)
            if index != -1:
                printItem(lstCls, index)
                while True:
                    print("Chỉnh sửa:\n1. Mã lớp\n2. Tên lớp\n0. Thoát")
                    c = int(input())
                    match c:
                        case 0:
                            return 0
                        case 1:
                            lstStd[index] = input("Nhập mã mới: ")
                        case 2:
                            lstStd[index] = input("Nhập tên mới: ")
                        case default:
                            print("Lựa chọn không hợp lệ")
            else:
                print("Mã lớp không tồn tại")
        case default:
            print("Lựa chọn không hợp lệ")
            return 0


def deleteItem():
    print("Xóa:\n1. Sinh viên\n2.Lớp\n0. Hủy")
    n = int(input("Nhập lựa chọn: "))
    match n:
        case 0:
            return 0
        case 1:
            id = input("Nhập mã SV: ")
            index = searchID(lstStd, id)
            if index != -1:
                printItem(lstStd, index)
                del lstStd[index]
                print("Xóa thông tin SV thành công")
                printList(lstStd)
            else:
                print("Mã SV không tồn tại")
        case 2:
            id = input("Nhập mã lớp: ")
            index = searchID(lstCls, id)
            if index != -1:
                printItem(lstCls, index)
                del lstStd[index]
                print("Xóa thông tin lớp thành công")
                printList(lstCls)
            else:
                print("Mã lớp không tồn tại")
        case default:
            print("Lựa chọn không hợp lệ")


def sortList(lst):
    """sort list by name"""
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if lst[i][1] > lst[j][1]:
                t = lst[i]
                lst[i] = lst[j]
                lst[j] = t
    printList(lst)


lstStd = readFile("Student.txt")
lstCls = readFile("Class.txt")
printList(lstStd)
printList(lstCls)
# add()
# edit()
search()
# deleteItem()
# sortList(lstStd)
# sortList(lstCls)