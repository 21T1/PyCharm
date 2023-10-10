toan = float(input("Nhập điểm Toán: "))
li = float(input("Nhập điểm Lí: "))
hoa = float(input("Nhập điểm Hóa: "))
dtb = (toan + li + hoa)/3
print("Điểm trung bình:", dtb)
print("Làm tròn:", round(dtb, 2))

print("Chương trình tính điểm trung bình")
toan, li, hoa = eval(input("Nhập điểm toán, lý, hóa: "))
print("Điểm toán:", toan)
print("Điểm lí:", li)
print("Điểm hóa:", hoa)
dtb = (toan + li + hoa)/3
print("Điểm trung bình:", round(dtb,2))
