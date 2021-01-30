if __name__ == '__main__':
    text3 = open('text_3.txt','r+',encoding= 'utf - 8')
    with open('text_2.txt', encoding='utf - 8') as f_obj:
        for line in f_obj:
            for el in line.split():
                if el == 'One':
                    line = 'Один - 1\n'
                    text3.writelines(line)
                elif el == 'Two':
                    line = 'Два - 1\n'
                    text3.writelines(line)
                elif el == 'Three':
                    line = 'Три - 1\n'
                    text3.writelines(line)
                elif el == 'Four':
                    line = 'Четыре - 1\n'
                    text3.writelines(line)


