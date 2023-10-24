from tkinter import *


def showResult():
    year = int(strSY.get())
    result = ""
    match (year - 3) % 10:
        case 0:
            result = "Quý"
        case 1:
            result = "Giáp"
        case 2:
            result = "Ất"
        case 3:
            result = "Bính"
        case 4:
            result = "Đính"
        case 5:
            result = "Mậu"
        case 6:
            result = "Kỷ"
        case 7:
            result = "Canh"
        case 8:
            result = "Tân"
        case 9:
            result = "Nhâm"
    result += " "
    match (year - 3) % 12:
        case 0:
            result += "Hợi"
        case 1:
            result += "Tý"
        case 2:
            result += "Sửu"
        case 3:
            result += "Dần"
        case 4:
            result += "Mão"
        case 5:
            result += "Thìn"
        case 6:
            result += "Tị"
        case 7:
            result += "Ngọ"
        case 8:
            result += "Mùi"
        case 9:
            result += "Thân"
        case 10:
            result += "Dậu"
        case 11:
            result += "Tuất"
    strLY.set(result)


root = Tk()
root.title("Chuyển năm Dương lịch thành Âm lịch")
root.minsize(width=450, height=70)


strSY = StringVar()
strLY = StringVar()


Label(root, width=20, text="Nhập năm Dương lịch:").grid(row=0, column=0)
Entry(root, width=10, textvariable=strSY).grid(row=0, column=1)

Label(root, width=15, text="Năm Âm lịch:").grid(row=0, column=2)
Entry(root, width=10, textvariable=strLY).grid(row=0, column=3)

Button(root, width=15, text="Chuyển đổi", command=showResult).grid(row=1, column=1, pady=10, sticky="ew")

root.mainloop()