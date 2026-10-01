import math

num = int(input("введи четырехзначное число: "))

a = num % 10
b = (num // 10) % 10
c = (num // 100) % 10
d = num // 1000

print("1 цифра: ", d)
print("2 цифра: ", c)
print("3 цифра: ", b)
print("4 цифра: ", a)