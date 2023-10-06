dtb = float(input("Nhập điểm trung bình: "))
# if else
if dtb >= 5:
    print("Bạn đã đậu!")
else:
    print("Chúc bạn may mắn lần sau!")
# if elif
if dtb >= 9:
    print("Xếp loại giỏi")
elif dtb >= 7:
    print("Xếp loại khá")
elif dtb >= 5:
    print("Xếp loại trung bình")
else:
    print("Bye!")
