a = int(input())
b = int(input())
c = a / b

if b == 0:
    print(f'a/b')
else:
    c = a // b 
    x = a % b

if a % b == 0:
    print(f' c = {a} делится на {b} без остатка')
else:
    print(f'c = {a} делится на {b} с остатком')