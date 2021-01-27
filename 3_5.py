if __name__ == '__main__':
    numbers = []
    result = 0
    user_answer = 0
    while True:
        a = input('Введите числа')
        for n in a.split():
            if n == "#":
                continue
            else:
                numbers.append(int(n))
                for i in numbers:
                    result = result + i
                    numbers.clear()
        print(result)
        user_answer = input('Продолжить ввод данных? (да - нажмите Enter, нет - введите "#"): ')
        if user_answer.lower() == '#':
            break