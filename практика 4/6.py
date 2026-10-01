import math

rad = math.radians(int(input("введите количество градусов: ")))

print("вывод: синус числа + косинус + тангенс")
print(math.sin(rad) + math.cos(rad) + (math.tan(rad)) ** 2)
