if __name__ == '__main__':

    time = int(input('Введите кол-во секунд'))
    hours = time / 3600
    minutes = time / 60
    second = time % 60
    print(f'{hours:.0f}:{minutes:.0f}:{second:.0f}')
