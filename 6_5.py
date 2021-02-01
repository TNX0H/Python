if __name__ == '__main__':
    class Stationery():
        title = 'Название'
        def draw(self):
            print('Запуск отрисовки')

    class Pen(Stationery):
        def draw(self):
            print('Надпись ручкой')

    class Pencil(Stationery):
        def draw(self):
            print('Надпись карандашом')

    class Handle(Stationery):
        def draw(self):
            print('Надпись маркером')
Pen().draw()
