x = input("Enter your name: ")
print("Your name is:", x, type(x))

print("-"*20)
print("Enter your birth year: ")
n = int(input())
print("Your age is", 2023-n, type(n))

print("-"*20)
def StrToBool(s):
    return s.lower() in ("true", "yes", "t", "1")
x = input("Enter True/False: ")
x = StrToBool(x)
print(x)
