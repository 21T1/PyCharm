from random import randrange


def createList():
    """Create a random number list"""
    n = int(input("Nhập số phần tử, n = "))
    lst = []
    for i in range(n):
        lst.append(randrange(0, 100))
    return lst


def printList(lst):
    """Print list lst"""
    for item in lst:
        print(item, end=' ')
    print()


def delValue(lst):
    """Delete value k in list lst"""
    k = int(input("Nhập giá trị cần xóa, k = "))
    while lst.count(k) > 0:
        lst.remove(k)


def symmetric(lst):
    """Check if list lst is symmetric"""
    for i in range(0, len(lst) // 2):
        if lst[i] != lst[len(lst) - 1 - i]:
            return False
    return True


lst = createList()
print("List ngẫu nhiên:")
printList(lst)

delValue(lst)
print("List sau khi xóa:")
printList(lst)
print("List đối xứng" if symmetric(lst) else "List không đối xứng")