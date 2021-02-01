if __name__ == '__main__':
    class Car():
        speed = input('Введите скорость')
        color = input('Введите цвет')
        name = input('Введите марку')
        is_police = False
        def go(self):
            print('Машина едет')

        def stop(self):
            print('Машина остановилась')

        def turn(self, direction):
            direction = input('Введите направление')
            print(f'Машина повернула {direction}')

        def show_speed(self,speed):
            self.speed = speed
            print(f'Скорость машины{self.speed}')

    class TownCar(Car):
        speed = Car.speed
        color = Car.color
        name = Car.name
        is_police = False
        def show_speed(self):
            if int(Car.speed) > 60:
                print('Превышение скорости')
            else:
                print(f'Скорость машины{Car.speed}')

    class SportCar(Car):
        speed = Car.speed
        color = Car.color
        name = Car.name
        is_police = False

    class WorkCar(Car):
        speed = Car.speed
        color = Car.color
        name = Car.name
        is_police = False
        def show_speed(self):
            if int(Car.speed) > 40:
                print('Превышение скорости')
            else:
                print(f'Скорость машины{Car.speed}')

    class PoliceCar(Car):
        speed = Car.speed
        color = Car.color
        name = Car.name
        is_police = True

print(WorkCar().speed)
print(WorkCar().color)
print(WorkCar().name)
WorkCar().show_speed()