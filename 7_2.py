if __name__ == '__main__':
    from abc import ABC


    class AbstractClothes(ABC):
        def __init__(self, size, height):
            self.size = size
            self.height = height


    class Clothes(AbstractClothes, ABC):
        def __init__(self, size, height):
            super().__init__(size, height)
            self.size = size
            self.height = height


    class Coat(Clothes, ABC):
        @property
        def expense(self):
            return self.size / 6.5 + 0.5


    class Suit(Clothes, ABC):
        @property
        def expense(self):
            return 2 * self.height + 0.3


    clot = Clothes(10, 15)
    coat = Coat(10, 15)
    suit = Suit(10, 15)
    print(coat.expense)
