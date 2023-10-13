def handle(f, x):
    return f(x)


r1 = handle(lambda x: x ** 2, 9)
print("r1 =", r1)

r2 = handle(lambda x: x % 2 == 0, 4)
print("r2 =", r2)


def isOdd(x):
    return x % 2 == 0


r3 = handle(isOdd, 4)
print("r3 =", r3)

r4 = handle(isOdd, 5)
print("r4 =", r4)

r5 = handle(lambda x: isOdd(x), 5)
print("r5 =", r5)