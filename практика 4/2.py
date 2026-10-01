import math

#функция, для ввода х1 х2 у1 у2 и вывода еклидова расстояния
def rast(x1, y1, x2, y2):
    rasst = (math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2)))
    return rasst

x1, y1 = map(float, input("введите x1 y1").split())
x2, y2 = map(float, input("введите x2 y2").split())

distance = rast(x1, x2, y1, y2)

print(f"расстояние {distance:.2f}")