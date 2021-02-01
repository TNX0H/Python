if __name__ == '__main__':
    my_dict= dict(winter = [1,2,12], spring = [3,4,5], summer = [6,7,8], autumn = [9,10,11])
    month = int(input('Введите число месяца'))
    for n in my_dict:
        for i in my_dict[n]:
            if (month == i):
                print(n)
