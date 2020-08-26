from math import floor

class Rectangle():
    def __init__(self,height,width):
        self.height = height
        self.width = width

    def set_width(self,width):
        self.width = width

    def set_height(self,height):
        self.height = height

    def get_area(self):
        return self.height * self.width

    def get_perimeter(self):
        return 2 * self.height + 2 * self.width

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return 'Too big for picture'
        picture = ''
        for line in range(0,self.height):
            picture += '*' * self.width + '\n'
        return picture

    def get_amount_inside(self,shape):
        height = shape.height
        width = shape.width
        if shape.height > self.height or shape.width > self.width:
            return 0
        return floor(self.height / shape.height) * floor(self.width / shape.width)
    
    def __str__(self):
        return f'Rectangle(height={self.height}, width={self.width})'


class Square(Rectangle):
    def __init__(self,side):
        self.height = side
        self.width = side

    def set_side(self,side):
        self.height = self.width = side

    def __str__(self):
        return f'Square(side={self.height})'

    def set_height(self,height):
        self.height = self.width = height

    def set_width(self,width):
        self.width = self.height = width

    