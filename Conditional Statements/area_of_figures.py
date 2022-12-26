from math import pi,pow
figure = input()
area = 0

if figure == 'square':
    side_of_square = float(input())
    area = side_of_square * side_of_square
elif figure == 'rectangle':
    side_1 = float(input())
    side_2 = float(input())
    area = side_1 * side_2
elif figure == 'circle':
    radius = float(input())
    area = pow(radius, 2) * pi
elif figure == 'triangle':
    side = float(input())
    h = float(input())
    area = (side * h) / 2

print(f'{area:.3f}')