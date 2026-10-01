import math

place_for_nashe_cupe = 4

num_place = int(input("введите номер вашего места: "))
num_cupe = (num_place - 1) // place_for_nashe_cupe + 1
print("ваш вагон: ", num_cupe)