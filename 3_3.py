if __name__ == '__main__':
    def my_func(a, b, c):
        result = 0
        if ((a >= b) or (b >= a)) and (b > c):
            result = a + b
        elif ((b >= c) or (c >= b)) and (c > a):
            result = b + c
        elif ((c >= a) or (a >= c)) and (c > b):
            result = a + c
        return result
    print(my_func(10, 10, 10))