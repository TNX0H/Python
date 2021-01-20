if __name__ == '__main__':
    count = 1
    temp = []
    while True:
        name = input('Введите наименование товара: ')
        price = input('Введите цену товара: ')
        qun = input('Введите количество товара: ')
        unit = input('Введите единицу измерения товара: ')
        temp.append((count, {'название': name,
                         'цена': price,
                         'количество': qun,
                         'ед': unit}))
        user_answer = input('Добавить еще один товар? (да - нажмите Enter, нет - введите "н"): ')
        if user_answer.lower() == 'н':
            break
        count += 1

    print(temp)

