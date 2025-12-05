def shapes(circle, rectangle, triangle, **kwargs):
    if circle == 'круг':
        r = kwargs['r']
        S = 3.14 * r**2
        return S
    
    elif rectangle == 'прямоугольник':
        a = kwargs['a']
        b = kwargs['b']
        S = a * b
        return S
    
    elif triangle == 'треугольник':
        a = kwargs['a']
        h = kwargs['h']
        S = (a * h)/2
        return S 
    

circle = shapes('круг' , r = 3)
print(f'Площадь круга: {circle}')
