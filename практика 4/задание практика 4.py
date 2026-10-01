import math

#1
num = int(input())
print(math.floor(num/2))
print(math.ceil(num/2))

#2
x1 = int(input("x1: "))
x2 = int(input("x2: "))
y1 = int(input("y1: "))
y2 = int(input("y2: "))
print(math.sqrt(((x1 - x2)**2) + ((y1 - y2)**2)))

#3
num = int(input("введи число: "))
if num // 1000 >= 10:
    print("введи четырехзначное число")
else:
    a = num % 10
    b = (num // 10) % 10
    c = (num // 100) % 10
    d = num // 1000
    print("1 цифра: ", d)
    print("2 цифра: ", c)
    print("3 цифра: ", b)
    print("4 цифра: ", a)
    
#4
n = int(input("введите целое количество школьников: "))
k = int((input("введите колво мандаринов: ")))
print(k // n)
print(k % n)

#5
min = int(input("количество минут: "))
print(min, "минут - это ", min // 60,"часов, и", min % 60, "минут")
#6
rad = math.radians(int(input()))
print(math.sin(rad) + math.cos(rad) + (math.tan(rad))**2)

#7
while True:
    place_for_nashe_cupe = 4

    num_place = int(input("введите номер вашего места: "))
    num_cupe = (num_place - 1) // place_for_nashe_cupe + 1
    print("ваш вагон: ", num_cupe)