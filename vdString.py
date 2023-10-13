s = input("Nhập tên: ")
# Upper/Lower case
print(s.upper())
print(s.lower())
# Align right
print(s.rjust(len(s) + 5, "*"))
print(s.rjust(len(s) - 1, "*"))
# Align left
print(s.ljust(len(s) + 5, "*"))
print(s.ljust(len(s) - 1, "*"))
# Align center
print(s.center(20))
print(s.center(20, "*"))
# String length
print(len(s))
print(s.__len__())

# Removes any leading and trailing spaces
s = "      Hello      World      "
print(s.strip(), len(s))

s = "## ###Hello     World######"
print(s.strip("#"), len(s))

# startswith, endswith
s = "@hello()"
print(s.startswith("@"))
print(s.startswith("*"))
print(s.endswith("()"))
print(s.endswith(" "))

# find, count
s = "C:/folderA/folderB/folderC/vdString.py"
# find first
print(s.find("/"))
# find last
print(s.rfind("/"))
# count
print(s.count("/"))
# count from 0 to 1 / 2 * len(s)
print(s.count("/", 0, len(s) // 2))

# format, substring
s = "Hello world!"
print(s[2:])    # 2 -> end
print(s[:2])    # 0 -> (2 - 1)
print(s[-2:])   # last - (2 - 1) -> last
print(s[:-2])   # 0 -> last - (2 - 1)
print(s[2:-2])  # 2 -> last - (2 - 1)
print(s[6:11])  # 6 -> (11 - 1)

s = "C:/folderA/folderB/folderC/vdString.py"
print("File name:", s[(s.rfind("/") + 1): s.rfind(".")])

# split
s = "21T1;Hoàng Anh;1/1/1001"
arr = s.split(";")
for item in arr:
    print(item)

s = """Một con vịt
    xòe ra hai cái cánh
    nó kêu rằng
    cáp cáp cáp
    cạp cạp cạp"""
arr = s.splitlines()
for line in arr:
    print(line, "-> c:", line.count("c"))

# join
a = "Một hai ba"
b = " 123"
c = a + b
print("c =", c)

# spit and join
s = """21T1;Hoàng A;1/1/2001
21T2;Hoàng B;2/2/2002
21T3;Hoàng C;3/3/2003
21T4;Hoàng D
21T5;Hoàng E;5/5/2005
"""

arrSV = s.splitlines()
for line in arrSV:
    arrInfor = line.strip().split(";")
    if len(arrInfor) == 3:
        print(arrInfor)
        print(", ".join(arrInfor))