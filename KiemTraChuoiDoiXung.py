def symmetric(s):
    """Check if a string (s) is symmetrical"""
    for i in range(len(s) // 2 + 1):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True


def printResult():
    s = input("Nhập chuỗi: ")
    if symmetric(s):
        print("Chuỗi", s, "đối xứng")
    else:
        print("Chuỗi", s, "không đối xứng")

while True:
    printResult()
    if input("Tiếp tục (c/k)? ") == "k":
        break
print("Kết thúc chương trình")