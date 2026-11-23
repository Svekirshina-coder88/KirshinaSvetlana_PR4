#Задание 19
import math
s = int(input())
h = int(input())
V = (s ** 2) * h * math.pi
Sbok = 2 * math.pi * s * h
print(f'Объем цилиндра: {V}')
print(f'Боковая площадь поверхности: {Sbok}')
