if __name__ == '__main__':
    class Worker():
        name = input('Введите имя')
        surname = input('Введите фамилию')
        position = ''
        wage = input('Введите оклад')
        bonus = input('Введите премию')
        _income = {"Оклад": wage, "Премия": bonus}
    class Position(Worker):
        def get_full_name(self):
            print(f'{self.name} {self.surname}')
        def get_total_income(self):
            print(f'Доход:{self._income}')

p=Position()
p.get_full_name()
p.get_total_income()