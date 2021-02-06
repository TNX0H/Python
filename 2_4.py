if __name__ == '__main__':
    text = input('Введите строку')
    print(text.split())
    for ind, el in enumerate(text.split(), 1):
        if len(el)>10:
            print(el)
            print(ind, el[:10])
        else:
            print(ind, el)











#        if len(el)>10:
           # (text.split()[:10],1)
           # print(ind, el)