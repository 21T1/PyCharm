def ptb1(a,b):
    """Giải phương trình bậc nhất ax + b = 0"""
    if a == 0:
        if b == 0:
            return "Vô số nghiệm"
        else:
            return "Vô nghiệm"
    else:
        return "x = {0}".format(-b/a)

def xuatDuLieu(data):
    print(data)

a, b = eval(input("Nhập 2 số a, b: "))
xuatDuLieu(ptb1(a,b))