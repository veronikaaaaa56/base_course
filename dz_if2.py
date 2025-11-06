a = float(input())
b = float(input())
c = float(input())

if a + b > c and a + c > b and b + c > a:
    print('Треугольник с такими сторонами существует')
if a == b or a == c or b == c:
    print('Треугольник равнобедренный')
elif a == b and b == c:
    print('Треугольник равносторонний')
else:
    print('Треугольник разносторонний')