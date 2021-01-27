if __name__ == '__main__':
    import random
    from collections import Counter
    numbers = []
    c = Counter()
    while len(numbers) < 20:
        numbers.append(random.randint(0, 10))
    print(numbers)
    for el in numbers:
        c[el] += 1
    print(c.keys())

