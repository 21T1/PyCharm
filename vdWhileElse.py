count = sum = 0

print("Nhập 5 số >= 0 để tính trung bình")
while count < 5:
    val = float(input("Nhập giá trị: "))
    if val < 0:
        print("Sai quy tắc")
        break
    sum += val
    count += 1
else:
    print("Trung bình =", sum/count)