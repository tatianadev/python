import graphics
from graphics import Point


class Shape(object):
    def __init__(self, x: float = 0, y: float = 0, color: str = 'black'):
        self.x = x
        self.y = y
        self.color = color

    def draw(self) -> None:
        raise NotImplementedError()

    @property
    def width(self):
        raise NotImplementedError()

    @property
    def height(self):
        raise NotImplementedError()


class Rectangle(Shape):
    def __init__(self, width: float, height: float, x: float = 0, y: float = 0, color: str = 'black'):
        Shape.__init__(self, x, y, color)
        self.__width = width
        self.__height = height

    def draw(self) -> None:
        top_left = Point(self.x - self.__width / 2, self.y - self.__height / 2)
        bottom_right = Point(self.x + self.__width / 2, self.y + self.__height / 2)
        graphics.draw_rect(top_left, bottom_right, self.color)

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height


class Ellipse(Shape):
    def __init__(self, width: float, height: float, x: float = 0, y: float = 0, color: str = 'black'):
        Shape.__init__(self, x, y, color)
        self.__width = width
        self.__height = height

    def draw(self) -> None:
        top_left = Point(self.x - self.__width / 2, self.y - self.__height / 2)
        bottom_right = Point(self.x + self.__width / 2, self.y + self.__height / 2)
        graphics.draw_ellipse(top_left, bottom_right, self.color)

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height


class Triangle(Shape):
    def __init__(self, width: float, height: float, x: float = 0, y: float = 0, color: str = 'black'):
        Shape.__init__(self, x, y, color)
        self.__width = width
        self.__height = height

    def draw(self) -> None:
        first_point = Point(self.x - self.__width / 2, self.y + self.__height / 2)
        second_point = Point(self.x + self.__width / 2, self.y + self.__height / 2)
        third_point = Point(self.x, self.y - self.__height / 2)

        objects = [first_point, second_point, third_point]
        graphics.draw_polygon(objects, self.color)

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height


class Square(Rectangle):
    def __init__(self, size: float, x: float = 0, y: float = 0, color: str = 'black'):
        super().__init__(size, size, x, y, color)


class Circle(Ellipse):
    def __init__(self, size: float, x: float = 0, y: float = 0, color: str = 'black'):
        super().__init__(size, size, x, y, color)
