a, b = map(int, input().split())
if ((a or b)>10**9) or ((a or b)< -10**9) :
    print("Введите другие числа")
else:
    print(a+b**2)