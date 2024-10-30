from Shape import Shape


class Rectangle(Shape):
    """Rectangle shape class"""

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

    def calculate_area(self) -> float:
        """Calculate the area of the rectangle

        Returns:
            float: the result of multiplying the width by the height `self.width * self.height`
        """
        return self.width * self.height
