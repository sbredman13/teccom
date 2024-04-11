# Создать класс Point, который представляет собой точку
# в двумерном пространстве. Класс должен иметь методы для
# инициализации координат точки, вычисления расстояния
# до другой точки, а также для получения и изменения координат.
class Point:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        print(
            f'Точка {self.name} '
            f'Находится на координатах: x = {self.x} y = {self.y}'
        )
    
    def shift(self, x, y):
        self.x += x
        self.y += y
        print(
            f'Точка {self.name} '
            f'Изменила координаты: '
            f'x = {self.x} y = {self.y}'
        )

    def distance(self, point):
        print(
            f'Расстояние от точки {self.name} '
            f'до точки {point.name} = '
            f'{((self.x - b.x) ** 2 + (self.y - b.y) ** 2) ** 0.5}')


if __name__ == "__main__":
    print(f'Введите название и координаты первой точки')
    a = Point(
        name = input(),
        x = int(input()),
        y = int(input())
    )
    print(f'Введите название и координаты второй точки')
    b = Point(
        name=input(),
        x=int(input()),
        y=int(input())
    )
    print(f'Передвиньте точку {a.name}')
    a.shift(
        x = int(input()),
        y = int(input())
    )
    print(f'Передвиньте точку {b.name}')
    a.shift(
        x=int(input()),
        y=int(input())
    )
    a.distance(b)
