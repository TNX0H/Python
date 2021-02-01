if __name__ == '__main__':
    a = int(input('Введите кол-во км в 1 день'))
    b = int(input('Ведите желаемое кол-во км'))
    i = 0
    while (b>a):
        i = i + 1
        a = a + (a / 10)
        print (a,i,)
    print(f'Вы достигните результата на {i+1} дне')
