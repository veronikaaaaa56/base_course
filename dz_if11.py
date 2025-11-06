a = float(input())
b = float(input())
c = float(input())

D = b**2 - 4*(a*c)

if D > 0:
    print('Уравнение имеет два корня')
    print(-b - (D) / (2 * a))
    print(-b - (D) / (2 * a))
elif D == 0:
    print('Уравнение имеет один корень')
    print(-b / (2 * a))
else:
    print('Уравнение не имеет корней')