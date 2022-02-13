from math import hypot


class Vector:
    # __slots__ = ('_x', '_y')

    def __init__(self, x=0.0, y=0.0):
        self._x = float(x)
        self._y = float(y)

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.x == other.x and self.y == other.y
    def vectorIncrement(self, other):
        self._x += other._x;
        self._y += other._y;

    def vectorDecrement(self, other):
        self._x -= other._x;
        self._y -= other._y;

    def vectorSum(self,b,c):
        b._x += c._x;
        b._y += c._y;
        print((b._x,b._y))

    def vectorDif(self,b,c):
        b._x -= c._x;
        b._y -= c._y;
        print((b._x,b._y))

    def __ne__(self, other):
        return not a == b

    def vectorLen(self):
        return hypot(self.x, self.y)
    def vectotPrint(self):
        print((self._x,self._y))

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @x.setter
    def x(self, value):
        self._x = float(value)

    @y.setter
    def y(self, value):
        self._y = float(value)


if __name__ == '__main__':
    a = Vector(2, 2)
    b = Vector(1, 1)
    c = Vector(2, 2)


    a.vectorSum(b,c)
    a.vectorDif(b,c)
    print(f'{a.vectorLen()}')
    a.vectotPrint()
    a.vectorIncrement(b)
    a.vectotPrint()