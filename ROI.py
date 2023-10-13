def calculateROI(r, ivm):
    """Calculate ROI (Return On Investment) using r (return) and ivm (investment)"""
    return (r - ivm) / ivm


def hint(ROI):
    if ROI >= 0.75:
        return "Nên đầu tư"
    else:
        return "Không nên đầu tư"


r = float(input("Doanh thu: "))
ivm = float(input("Chi phí: "))

ROI = calculateROI(r, ivm)
print("ROI:", round(ROI, 2))
print("=>", hint(ROI))
