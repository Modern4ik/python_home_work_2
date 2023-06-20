# Программа для поиска кол-ва монеток, которые нужно перевернуть для того, чтобы все монетки были повёрнуты одной стороной,
# из общего кол-ва монеток, заданного пользователем.

from random import randint

def get_value_from_user(message):
    flag = True

    while flag:
        try:
            user_value = int(input(message))

            if user_value > 0:
                flag = False
            else:
                print("Ошибка.Число не должно быть равно или меньше 0")
                continue

        except ValueError:
            print("Ошибка.Введите число, а не буквы.")
            continue
        
    return user_value


def get_coins_status(user_value):
    coins_list = [0] * user_value

    for i in range(len(coins_list)):
        coins_list[i] = randint(0, 1)
    
    return coins_list


def get_coins_count(coins_list):
    head_coins_count = 0
    tail_coins_count = 0

    for i in range(len(coins_list)):
        if coins_list[i] == 1:
            head_coins_count += 1
        else:
            tail_coins_count += 1
    
    return head_coins_count, tail_coins_count


def print_report(head_coin_count, tail_coins_count):
    if head_coin_count > tail_coins_count and tail_coins_count != 0:
        print(f"{tail_coins_count} - монет с решкой меньше всего, значит их нужно перевернуть в данном кол-ве.")
    elif head_coin_count == tail_coins_count:
        print(f"{head_coin_count} = {tail_coins_count} - монет поровну, значит можно переворачивать любые.")
    elif head_coin_count == 0 or tail_coins_count == 0:
        print("Все монеты и так повёрнты одной стороной вверх!")
    else: 
        print(f"{head_coin_count} - монет с орлом меньше всего, значит их нужно перевернуть в данном кол-ве.")


###########################################################################################################

coins_numb = get_value_from_user("Введите кол-во монеток, большее 0: ")

head_tail_list = get_coins_status(coins_numb)
print(head_tail_list)

heads_count, tails_count = get_coins_count(head_tail_list)

print()
print_report(heads_count, tails_count)