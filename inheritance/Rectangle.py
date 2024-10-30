from math import pi, pow


class Shape:
    def calculate_area(self) -> float:
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be positive.")
        else:
            self._radius = radius

    def __str__(self):
        return f'Circle: "radius"={self.radius}, "area"={self.calculate_area()})'

    def __repr__(self):
        return f"Circle({self.radius})"

    def __eq__(self, o):
        if isinstance(o, Circle):
            return self.radius == o.radius
        else:
            return False

    def calculate_area(self):
        return pi.real * pow(self.radius, 2)


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if width <= 0:
            raise ValueError("Width must be positive.")
        else:
            self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if height <= 0:
            raise ValueError("height must be positive.")
        else:
            self._height = height

    def __str__(self):
        return f'(Rectangle: "width"={self.width}, "height"={self.height}, "area"={self.calculate_area()}'

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __eq__(self, o):
        if isinstance(o, Rectangle):
            return self.width == o.width and self.height == o.height
        else:
            return False

    def calculate_area(self):
        return self.width * self.height


r1 = Rectangle(10, 100)
print(r1)
r1.height = 1
print(r1)

c1 = Circle(5)
print(c1)
c1.radius = 3
print(c1)
