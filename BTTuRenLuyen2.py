# Câu 1: Cho biết kết quả của Boolean Expresion, biết:
x = 3
y = 5
z = 7

# (a) x == 3              True
# (b) x < y               True
# (c) x >= y              False
# (d) x <= y              True
# (e) x != y - 2          False
# (f) x < 10              True
# (g) x >= 0 and x < 10   True
# (h) x < 0 and x < 10    False
# (i) x >= 0 and x < 2    False
# (j) x < 0 or x < 10     True
# (k) x > 0 or x < 10     True
# (l) x < 0 or x > 10     False

print(x == 3, x < y, x >= y, x <= y, x != y - 2,
      x < 10, x >= 0 and x < 10,
      x < 0 and x < 10, x >= 0 and x < 2,
      x < 0 or x < 10, x > 0 or x < 10,
      x < 0 or x > 10)

# Câu 2: Cho i. j, k là các con số và lệnh dưới đây:
i = int(input("i = "))
j = int(input("j = "))
k = int(input("k = "))
if i < j:
      if j < k:
            i = j
      else:
            j = k
else:
      if j > k:
            j = i
      else:
            i = k
print("i =", i, "j =", j, "k =", k)
#                                     i     j     k
# (a) i = 3, j = 5 and k = 7          5     5     7
# (b) i = 3, j = 7 and k = 5          3     5     5
# (c) i = 5, j = 3 and k = 7          7     3     7
# (d) i = 5, j = 7 and k = 3          5     3     3
# (e) i = 7, j = 3 and k = 5          5     3     5
# (f) i = 7, j = 5 and k = 3          7     7     3

# Câu 3: Nhập vào một số n có tối đa 2 chữ số. Hãy cho biết cách đọc ra dạng chữ
# vd: n = 35 -> Ba mươi lăm, n = 5 -> năm
def char(x):
      if x == 1:
            return "mốt"
      elif x == 2:
            return "hai"
      elif x == 3:
            return "ba"
      elif x == 4:
            return "bốn"
      elif x == 5:
            return "lăm"
      elif x == 6:
            return "sáu"
      elif x == 7:
            return "bảy"
      elif x == 8:
            return "tám"
      elif x == 9:
            return "chín"
      return ""

n = int(input("Nhập 1 số: "))
if n > 19:
      s = char(n//10) + " mươi " + char(n%10)
elif n >= 10:
      s = "mười "
      if n%10 == 1:
            s += "một"
      else:
            s += char(n%10)
else:
      if n == 1:
            s = "một"
      elif n == 5:
            s = "năm"
      else:
            s = char(n)
print(s)

# Câu 4: Nhập vào một ngày (ngày, tháng, năm). Tìm ngày kế sau ngày vừa nhập
day = int(input("Nhập ngày: "))
month = int(input("Nhập tháng: "))
year = int(input("Nhập năm: "))

if month > 12 or month < 1:
      print("Ngày tháng năm không hợp lệ!")
else:
      print("Sau ngày", day, "tháng", month, "năm", year, "là:")
      # Kiểm tra số ngày trong tháng
      if month in (1, 3, 5, 7, 8, 10, 12):
            numDay = 31
      elif month in (4, 6, 9, 11):
            numDay = 30
      else:
            if year%400 == 0 or (year%4 == 0 and year%100 != 0):
                  numDay = 29
            else:
                  numDay = 28
      if day > numDay:
            print("Ngày tháng năm không hợp lệ!")
      else:
            day += 1
            if day > numDay:
                  day = 1
                  month += 1
                  if month > 12:
                        month = 1
                        year += 1
            print("Ngày", day, "tháng", month, "năm", year)

# Câu 5: Nhập vào 2 giá trị a, b và phép toán '+', '-', '*', '/'.
# Hãy xuất ra kết quả theo đúng phép toán đã nhập
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
operator = input("Nhập phép tính( +, -, *, /): ")

if operator == "+":
      print(a, "+", b, "=", a + b)
elif operator == "-":
      print(a, "-", b, "-", a - b)
elif operator == "*":
      print(a, "*", b, "=", a*b)
elif operator == "/":
      print(a, "/", b, "=", round( a/b, 2))
else:
      print("Phép tính không hợp lệ!")

# Câu 6: Nhập vào 1 tháng, xuất ra tháng đó thuộc quý mấy trong
n = int(input("Nhập vào 1 tháng: "))
t = n//3
if n%3 != 0:
      t += 1
print("Tháng", n, "thuộc quý", t)