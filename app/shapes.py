class Shape:
    @staticmethod
    def about():
        print("Латыпова А., Филиппова К., Назметдинов Т.")

class Parallelepiped(Shape):
    def __init__(self, length, width, height):
        self._length = length
        self._width = width
        self._height = height

    @property
    def length(self):
        return self._length

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    def volume(self):
        return self._length * self._width * self._height

class Cube(Parallelepiped):
    def __init__(self, side):
        super().__init__(side, side, side)

    def surface_area(self):
        return 6 * self._length**2
