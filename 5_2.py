if __name__ == '__main__':
    string = 0
    word = 0
    with open('text_2.txt') as f_obj:
        for line in f_obj:
            string += 1
            word = 0
            for el in line.split():
                word += 1
            print(f'В {string} кол-во слов:{word}')