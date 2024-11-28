#3.Напишите программу для вычисления чисел Фибоначчи,
#исходя из рекуррентного выражения F(n) = F(n-1) + F(n-2).
#Используйте рекурсию.

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
i = 0
while True:
    print(fibonacci(i), end=' ')
    i += 1