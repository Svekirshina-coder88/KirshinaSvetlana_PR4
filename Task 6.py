#Раccтояние между двумя точками
s = float(input())
s1 = float(input())
e = float(input())
e1 = float(input())
d = ((e - s) ** 2 + (e1 - s1) ** 2) ** 0.5
print(f'Расстояние между точками равно: {d}')