'''
Work through the chapter "Classes and Objects" in Think Python 2e:
http://greenteapress.com/thinkpython2/html/thinkpython2016.html and
build out the Point class example.

'''
# class Rectangle():
#     """Represents a point in 2-D space."""
#     pass
#
# class Point():
#     pass
#
# square = Rectangle()
#
# pttl = Point()
# pttl.x = 0
# pttl.y = 0
#
# pttr = Point()
# pttr.x = 10
# pttr.y = 0
#
# ptbl = Point()
# ptbl.x = 0
# ptbl.y = 10
#
# ptbr = Point()
# ptbr.x = 10
# ptbr.y = 10
#
# square.tl = pttl
# square.tr = pttr
# square.bl = ptbl
# square.br = ptbr


class Rectangle():
    """Represents a point in 2-D space."""
    def __init__(self, tl, tr, bl, br):
        self.tl = tl
        self.tr = tr
        self.bl = bl
        self.br = br

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


ptl = Point(0,0)
ptr = Point(0,10)
pbl = Point(10,0)
pbr = Point(10,10)


square = Rectangle(ptl, ptr, pbl, pbr)


