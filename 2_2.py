if __name__ == '__main__':
    my_list = list(input('Введите данные'))
    i = 0
    for n in my_list:
        if (my_list.index(n) + 1 != len(my_list)) and (my_list.index(n) % 2 == 0)  :
            a = my_list.index(n)
            c = n
            my_list[a] = my_list[a + 1]
            my_list[a + 1] = c
    print(my_list)
