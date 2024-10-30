from math import pi, pow
from Shape import Shape


class Circle(Shape):
    """Circle shape class"""

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

    def calculate_area(self) -> float:
        """Calculate the area of the circle

        Returns:
            float: It is calculated using the formula A = πr^2, where 'r' is the radius of the circle.
            It is measured in square units.
        """
        return pi * pow(self.radius, 2)
