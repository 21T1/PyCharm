#Syntax Error
a = 2
b = a + 2
b + 2 = a

#Runtime Error
try:
    x = 5
    y = 0
    z = x / y
    print(z)
except:
    print("Error!!!")
print("Thanks for using")

#Logic Error
t = 10
l = 9.5
h = 7
dtb = t + l + h/3
print(dtb)