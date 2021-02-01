if __name__ == '__main__':
    from time import sleep
    class TrafficLight:
        __color = ''
        def running(self):
            count = 0
            list_col = ['Красный','Жёлтый','Зелёный']
            timer = [5, 2, 7]
            while count < 2:
                for __color in list_col:
                    i = timer.index(timer[0])
                    print(__color)
                    sleep(timer[i])
                    i += 1
                count += 1

    TL = TrafficLight()
    TL.running()