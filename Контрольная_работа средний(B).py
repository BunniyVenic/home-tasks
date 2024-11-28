import random
#Средний(B)
#1.  Напишите функцию для поиска суммы элементов списка больше х.
#Замените х на найденное значение. Используйте х как глобальную переменную.

random_numbers = [random.randint(1, 100) for _ in range(20)]
x = int(input('Введите число: '))
max_than_x = [num for num in random_numbers if num > x]
print(f"Числа больше чем x:", max_than_x)