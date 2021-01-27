if __name__ == '__main__':
    import random
    numbers = []
    result_numb = []
    while len(numbers) < 10:
        numbers.append(random.randint(0, 100))
    for n in numbers:
        i = numbers.index(n)
        if (n > numbers[i - 1]) and i > 0:
            result_numb.append(n)
    print(numbers)
    print(result_numb)