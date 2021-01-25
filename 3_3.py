if __name__ == '__main__':
    def my_func(a, b, c):
        result = 0
        if (a >= c) and (b >= c) :
            result = a + b
        elif (b >= a) and (c >= a):
            result = b + c
        elif (c >= b) and (a >= b):
            result = a + c
        return result
    print(my_func(8, 6, 10))