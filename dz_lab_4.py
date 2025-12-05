def shapes(shape_type, **kwargs):
    shape_type = shape_type.lower()

    if shape_type == 'круг'    
    elif shape_type == 'прямоугольник':
        a = kwargs['a']
        b = kwargs['b']
        S = a * b
        return S

    elif shape_type == 'треугольник':
        a = kwargs['a']
        h = kwargs['h']
        S = (a * h)/2
        return S
    
print(circle(r=5))
print(f"Площадь круга: {S}")