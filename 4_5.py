if __name__ == '__main__':
    from functools import reduce
    import random
    numbers = []
    while len(numbers) < 5:
        numbers.append(random.randrange(100, 1000, 2))
    def my_func(prev_el, el):
        return prev_el * el
    print(numbers)
    print(reduce(my_func, (numbers)))