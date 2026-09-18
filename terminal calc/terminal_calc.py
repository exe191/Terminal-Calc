# Терминальный калькулятор
def terminal_calc():
    all_chars = ["+", "-", "*", "/"]
    print(f"Я твой терминальный калькулятор выбери что ты хочешь сделать \nПрибавить {all_chars[0]} \nОтнять {all_chars[1]} \nУмножить {all_chars[2]} \nРазделить {all_chars[3]}")
    while True:
        Chars = input("Введи символ: ")
        if len(Chars) == 1 and Chars in all_chars:
            break
        else: 
            print("Ошибка!")

    number_one = float(input(f"Введи число которое хочешь {Chars} : "))
    number_two = float(input(f"Введи второе число которое хочешь {Chars} : "))
    if Chars == "+":
        print(f"{number_one} + {number_two} = {number_one + number_two}")
    elif Chars == "-":
        print(f"{number_one} - {number_two} = {number_one - number_two}")
    elif Chars == "*":
        print(f"{number_one} * {number_two} = {number_one * number_two}")
    elif Chars == "/":
        if number_two == 0:
            print("На ноль делить нельзя!")
        else:
            print(f"{number_one} / {number_two} = {number_one / number_two}")


terminal_calc()