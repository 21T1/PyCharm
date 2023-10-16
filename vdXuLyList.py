from random import randrange


def countValue(k, lst):
    """Count the number of value k in list lst"""
    count = 0
    for item in lst:
        if item == k:
            count += 1
    return count


def prime(n):
    """Check if n is prime number"""
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


def Menu():
    """Print function list"""
    print("XỬ LÝ LIST")
    print("1. Khởi tạo list n phần tử ngẫu nhiên")
    print("2. Thêm phần tử")
    print("3. Đếm số phần tử k trong list")
    print("4. Tính tổng các số nguyên tố trong list")
    print("5. Sắp xếp list")
    print("6. Xóa list")
    print("0. Thoát chương trình")


def printList(lst):
    """Print list lst """
    for item in lst:
        print(item, end='\t')
    print()


lst = []
while True:
    Menu()
    while True:
        chs = int(input("Nhập lựa chọn: "))
        if 0 <= chs <= 6:
            break
    match chs:
        case 1:
            n = int(input("Nhập số phần tử, n = "))
            lst = []
            for i in range(n):
                lst.append(randrange(-100, 100))
            printList(lst)
        case 2:
            item = int(input("Nhập giá trị muốn thêm vào: "))
            lst.append(item)
            printList(lst)
        case 3:
            k = int(input("Nhập giá trị cần đếm, k = "))
            print("Số", k, "xuất hiện", countValue(k, lst), "lần trong list")
        case 4:
            s = 0
            for item in lst:
                if prime(item):
                    s += item
            print("Tổng các số nguyên tố trong list, s =", s)
        case 5:
            lst.sort()
            printList(lst)
        case 6:
            del lst
            print("Xóa thành công")
        case default:
            print("Kết thúc chương trình")
            break
