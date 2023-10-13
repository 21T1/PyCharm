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
        return "Béo phì cấp độ 1\n"
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


h = float(input("Chiều cao (m): "))
w = float(input("Cân nặng (kg): "))

BMI = calculateBMI(h, w)
print("BMI:", round(BMI, 2))
print("Phân loại:", result(BMI))
print("Nguy cơ phát triển bệnh:", warning(BMI))
