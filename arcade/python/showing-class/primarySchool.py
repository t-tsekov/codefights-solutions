class Rectangle(object):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def __str__(self):
        return '{} x {} = {}'.format(self.height, self.width, self.area)

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.area = self.height * self.width

def primarySchool(height, width):
    return str(Rectangle(height, width))
