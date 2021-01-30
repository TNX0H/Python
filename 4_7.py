if __name__ == '__main__':
    from math import factorial
    def my_fact(n):
        for el in range(1, n + 1):
            yield (f'!{el} = {factorial(el)}')

    n = 5
    for el in my_fact(n):
        print(el)