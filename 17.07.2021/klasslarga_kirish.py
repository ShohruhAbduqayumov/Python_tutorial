class Son:
    x = 1
    y = 2


son1 = Son()  # son1 -> bu obyekt, Son() -> klass
print(son1.y, son1.x)
son2 = Son()
print(son2.x, son2.y)

# xulosa. Bitta klassdan hohlagancha obyekt olish mumkin

""" def __init__() funksiyasi: """


class Son:
    def __init__(self, x, y):
        self.x = x
        self.y = y


son3 = Son(4, 5)
print(son3.x, son3.y)
son4 = Son(6, 7)
print(son4.x, son4.y)
