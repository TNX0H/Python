if __name__ == '__main__':
    with open('text_2.txt', encoding= 'utf - 8') as f_obj:
        for line in f_obj:
            second_name = line.split()[0]
            for el in line.split():
                try:
                    if int(el) < 20000:
                        print(f'Оклад этого сотрудника меньше 20000: {second_name}')
                except ValueError:
                    continue
