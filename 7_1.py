if __name__ == '__main__':
    class Matrix:
        def __init__(self, my_list):
            self.my_list = my_list

        def __str__(self):
            return '\n'.join('\t'.join(map(str, row))
                             for row in self.my_list)

        def __add__(self, other):
            result = []
            numbers = []
            for i in range(len(self.my_list)):
                for j in range(len(self.my_list[0])):
                    summa = other.my_list[i][j] + self.my_list[i][j]
                    numbers.append(summa)
                    if len(numbers) == len(self.my_list):
                        result.append(numbers)
                        numbers = []
            return Matrix(result)

    matrix1 = Matrix([[1, 3, 4], [2, 2, 2], [3, 3, 3]])

    matrix2 = Matrix([[2, 5, 2], [2, 2, 2], [3, 3, 3]])

    print(matrix1 + matrix2)
