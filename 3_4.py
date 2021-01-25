if __name__ == "__main__":
    def my_func(x, y):
        return x**y
    print(my_func(3, 5))


    def my_func2(x,y):
        i = 0
        a = 1
        while i<y:
            a = a * x
            i = i + 1
        return a
    print(my_func2(3, 5))