first =int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))
fourth = int(input('Введите четвертое число: '))
def max_num():
  num1 = max(first, second)
  return num1
num3=max_num()
num2=max(third,fourth)
print(max(num3,num2))
