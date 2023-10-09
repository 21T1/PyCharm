from math import *
# log e
print(log(10))
print(log10(10))
# e
print(exp(1))
print(radians(30))
print(degrees(radians(30)))

x = 5
y = 7
print(pow(x,y))
print(x**y)

print("Nhập vào 1 góc: ")
deg = float(input())
sinx = sin(radians(deg))
cosx = cos(radians(deg))
tanx = tan(radians(deg))
cotx = 1/tanx
print("sin({0}) = {1}".format(deg, sinx))
print("cos({0}) = {1}".format(deg, cosx))
print("tan({0}) = {1}".format(deg, tanx))
print("cot({0}) = {1}".format(deg, cotx))
