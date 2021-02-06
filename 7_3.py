if __name__ == '__main__':
    class Cell:
        def __init__(self, count_cell, cell_in_row):
            self.count_cell = count_cell
            self.cell_in_row = cell_in_row

        def __add__(self, other):
            return self.count_cell + other.count_cell

        def __sub__(self, other):
            if self.count_cell - other.count_cell > 0:
                return self.count_cell - other.count_cell
            else:
                return f'Значение меньше 0'

        def __mul__(self, other):
            return self.count_cell * other.count_cell

        def __truediv__(self, other):
            return self.count_cell / other.count_cell

        def make_order(self):
            result = ''
            count = 0
            for el in range(1, self.count_cell + 1):
                if count < self.cell_in_row:
                    result += '*'
                    count += 1
                elif count == self.cell_in_row:
                    result += '/n*'
                    count = 1
            return result


    cell1 = Cell(103, 7)
    cell2 = Cell(105, 5)
    print(cell1 - cell2)
    print(cell1.make_order())
