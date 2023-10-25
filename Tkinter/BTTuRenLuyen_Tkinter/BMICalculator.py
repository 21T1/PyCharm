from tkinter import *


def calculateBMI(h, w):
    """Calculate BMI with h (height) and w (weight)"""
    return w / (h ** 2)


def result(BMI):
    """BMI's result"""
    if BMI >= 40.0:
        return "Béo phì cấp độ 3"
    elif BMI >= 35.0:
        return "Béo phì cấp độ 2"
    elif BMI >= 30.0:
        return "Béo phì cấp độ 1"
    elif BMI >= 25.0:
        return "Hơi béo"
    elif BMI >= 18.5:
        return "Bình thường"
    else:
        return "Gầy"


def warning(BMI):
    """Health warning"""
    if BMI >= 40.0:
        return "Nguy hiểm"
    elif BMI >= 35.0:
        return "Rất cao"
    elif BMI >= 25.0:
        return "Cao"
    elif BMI >= 18.5:
        return "Trung bình"
    else:
        return "Thấp"


def BMICalculator():
    h = float(strH.get())
    w = float(strW.get())
    BMI = calculateBMI(h, w)
    print(h, w, BMI)

    strBMI.set(str(round(BMI, 2)))
    strResult.set(result(BMI))
    strWarning.set(warning(BMI))


root = Tk()
root.title("Tính chỉ số BMI")
root.minsize(height=170, width=150)


strH = StringVar()
strW = StringVar()
strBMI = StringVar()
strResult = StringVar()
strWarning = StringVar()

Label(root, text="Nhập chiều cao: ").grid(row=0, column=0)
Entry(root, width=15, textvariable=strH).grid(row=0, column=1)
Label(root, text="(m)").grid(row=0, column=2)

Label(root, text="Nhập cân nặng: ").grid(row=1, column=0)
Entry(root, width=15, textvariable=strW).grid(row=1, column=1)
Label(root, text="(kg)").grid(row=1, column=2)

Button(root, text="Tính BMI", command=BMICalculator).grid(row=2, column=1, pady=5, sticky="we")

Label(root, text="Kết quả BMI").grid(row=3, columnspan=3)

Label(root, text="Chỉ số BMI:").grid(row=4, column=0, sticky="w")
Label(root, textvariable=strBMI).grid(row=4, column=1)

Label(root, text="Phân loại:").grid(row=5, column=0, sticky="w")
Label(root, textvariable=strResult).grid(row=5, column=1)

Label(root, text="Nguy cơ phát triển bệnh:").grid(row=6, column=0, sticky="w")
Label(root, textvariable=strWarning).grid(row=6, column=1)


root.mainloop()