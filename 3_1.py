if __name__ == '__main__':
    def division(a, b):
        try:
            c = a / b
        except ZeroDivisionError:
            return 'Делить на ноль нельзя'
        return c
    a = int(input('Введите делимое число'))
    b = int(input('Введите делитель'))
    print(division(a, b))