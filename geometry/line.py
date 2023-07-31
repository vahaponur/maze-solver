class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, o):
        return Point(self.x + o.x , self.y + o.y)
    def __sub__(self, o):
        return Point(self.x - o.x, self.y-o.y)
    def __truediv__(self, other):
        if isinstance(other,int) or isinstance(other,float):
            try:
                return Point(self.x / other, self.y/other)
            except Exception as e:
                print(e)
        return Point(self.x/other.x,self.y/other.y)


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fillcolor):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fillcolor, width=2)
        canvas.pack()
