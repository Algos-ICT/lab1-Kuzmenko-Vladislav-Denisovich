import time
t_start = time.perf_counter()
f = open('input3.txt')
n = int(f.read())
fib0 = 0
fib1 = 1
i = 0
if n >= 0 and n <= 10**7:
    if n != 0:
        while i < n-1:
            fib_sum = fib0 + fib1
            fib0 = fib1
            fib1 = fib_sum
            i = i + 1
    else: fib1 = 0
    f = open('output3.txt', 'w')
    f.write(str(fib1 % 10))
else: 
    f = open('output3.txt', 'w')
    f.write("Введите другое число")
print("Время работы %s секунд " % (time.perf_counter() - t_start))