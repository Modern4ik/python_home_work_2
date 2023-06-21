# Программа для поиска загаданных чисел Петей, использую значения суммы и произведения.

numb_sum = int(input("Введите cумму для загаданных чисел: "))
numb_prod = int(input("Введите произведение для загаданных чисел: "))

first_digit = numb_sum
second_digit = 0
flag = True

while flag:
    first_digit -= 1
    second_digit = numb_sum - first_digit
    

    if first_digit * second_digit == numb_prod or first_digit * second_digit == 0:
        flag = False


if first_digit != 0:
    print(f"Загаданные числа: {first_digit} и {second_digit}")
else:
    print(f"Так не бывает")