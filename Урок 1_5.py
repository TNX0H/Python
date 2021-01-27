if __name__ == '__main__':
    revenue = int(input('Введите выручка компании'))
    costs = int(input('Введите издержки компании'))
    if revenue>costs:
        print('Компания в "плюсе"')
        profit = revenue - costs
        pAbility = profit / revenue
    else:
        print('Компания в "минусе"')
    staff = int(input('Введите кол-во сотрудников'))
    profitForStaff = profit / staff
    print(f'Прибыль {profit}, рентабельность {pAbility:.0f}, прибыль на 1 сотрудника {profitForStaff:.0f}')
