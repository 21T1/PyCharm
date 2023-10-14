s = input("Nhập chuỗi: ")
print("Chuỗi ban đầu: '{0}' [{1}]".format(s, len(s)))

s = s.strip()
arr = s.split(' ')
x = ""
for a in arr:
    if a != "":
        x += a + " "
s = x.strip()
print("Chuỗi tối ưu:", s, "[{0}]".format(len(s)))