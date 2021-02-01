if __name__ == '__main__':
    import random
    count = 0
    result = 0
    with open('text_2.txt','r+' ,encoding= 'utf - 8') as f_obj:
        while count < 5:
            number = random.randint(0, 50)
            f_obj.write(str(number))
            f_obj.write(' ')
            result = result + number
            count += 1
        print(result)


