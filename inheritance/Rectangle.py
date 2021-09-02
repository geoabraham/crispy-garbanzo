class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if width <= 0:
            raise ValueError('Width must be positive.')
        else:
            self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if height <= 0:
            raise ValueError('height must be positive.')
        else:
            self._height = height

    def __str__(self):
        return f'Rectangle: "width"={self.width}, "height"={self.height})'

    def __repr__(self):
        return f'Rectangle({self.width}, {self.height})'

    def __eq__(self, o):
        if isinstance(o, Rectangle):
            return self.width == o.width and self.height == o.height
        else:
            return False

r1 = Rectangle(10, 100)
print(r1)
r1.height = 1
print(r1)
