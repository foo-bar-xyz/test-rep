class Point(object):
    '''Represents a point in two-dimensional geometric coordinates'''
    def __init__(self, x=0.0, y=0.0):
        '''Initialize the position of a new point. The x and y coordinates
        can be specified. If they are not, the point defaults to the origin'''
        self.move(x, y)

    def move(self, x, y):
        '''Move the point to a new location in two-dimensional space'''
        self.x = x
        self.y = y

    def reset(self):
        '''Reset the point back to the origin: <0, 0>'''
        self.move(0.0, 0.0)

    def calc_dist(self, other):
        '''Calculate the distance from this point to a second point passed
        as a parameter.
        This function uses the Pythagorean Theorem to calculate the distance
        between the two points. The distance is returned as float'''
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5

    def __str__(self):
        '''Prints in formated form'''
        return '<' + str(self.x) + ', ' + str(self.y) + '>'
