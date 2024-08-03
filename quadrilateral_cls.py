class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        val = [f'{side}={getattr(self,side)}' for side in vars(self)]
        return f"{self.__class__.__name__}({', '.join(val)})"

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return self.width * 2 + self.height * 2
    
    def get_diagonal(self):
        return (self.width**2 + self.height**2)**0.5
    
    def get_picture(self):
        length = ['*'*self.width+'\n' for i in range(self.height)]
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        return ''.join(length)
    
    def get_amount_inside(self, shape):
        fit_amount = self.get_area()//shape.get_area()
        if fit_amount < 0:
            return "Shape cannot fit inside"
        else:
            return fit_amount
class Square(Rectangle):
    def __init__(self, side):
        self.side = side
        super().__init__(self.side, self.side)
    
    def __repr__(self):
        return f"{self.__class__.__name__}(side={getattr(self, 'side')})"

    def set_height(self, height):
        self.__init__(height)

    def set_width(self, width):
        self.__init__(width)

    def set_side(self, side):
        self.__init__(side)
