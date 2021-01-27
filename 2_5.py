if __name__ == '__main__':
    my_list = [8,5,3,1]
    a = int(input('Введите число'))
    for n in my_list:
        i = my_list.index(n)
        if a>n:
            my_list.insert(0,a)
            print(my_list)
            break
        elif a<n:
            my_list.reverse()
            for n in my_list:
                while (a >= n):
                    k=my_list.index(n)
                    break
            my_list.insert(k + 1, a)
            my_list.reverse()
            print(my_list)
            break
        elif a==n:
            my_list.insert(i + 1, a)
            print(my_list)
            break



