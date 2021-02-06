if __name__ == '__main__':
    def info(name, second_name, year, city, email, phone):
        print(f'Имя:{name}, Фамилия:{second_name}, год рожедния: {year},'
              f'город проживания: {city}, email: {email}, телефон: {phone}')
    name = input('Введите ваше имя')
    second_name = input('Введите вашу фамилию')
    year = input('Введите ваш год рожения')
    city = input('Введите город проживания')
    email = input('Введите ваш email')
    phone = input('Введите ваш телефон')
    info(name, second_name, year, city, email, phone)