f = open('input.txt')
a, b = map(int, f.read().split())
if ((a or b)>10**9) or ((a or b)< -10**9) :
    print("Введите другие числа")
else:
    f = open('output1.txt','w')
    f.write(str(a+b**2))