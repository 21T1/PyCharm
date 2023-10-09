d1 = 1.11 - 1.1
d2 = 2.11 - 2.1
print("d1 =", d1)
print("d2 =", d2)

diff = d1 - d2
if diff < 0:
    diff = -diff
if diff < 0.0000001:
    print("d1 = d2")
else:
    print("d1 != d2")