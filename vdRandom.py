from random import randrange

count = 1
while True:
    x = randrange(-100, 100)
    print(count, end='.')
    print("{0:>4}".format(x))
    count += 1
    if x == 50:
        break
print("BYE!")