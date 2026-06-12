import math

class Point:
    def __init__(self, x = 0, y = 0):
        self.__x = x
        self.__y = y
    def get_x(self):
        return self.__x
    def get_y(self):
        return self.__y
    def distance(self, other):
        x1 = self.get_x()
        x2 = other.get_x()
        y1 = self.get_y()
        y2 = other.get_y()
        d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        return d
def main():
    x1, y1 = map(int, input("请输入第一个点坐标: ").split(','))
    x2, y2 = map(int, input("请输入第二个点坐标: ").split(','))
    point_a = Point(x1, y1)
    point_b = Point(x2, y2)
    d = format(point_a.distance(point_b), ".2f")
    print(f"点({point_a.get_x()},{point_a.get_y()})和" \
          f"点({point_b.get_x()},{point_b.get_y()})之间的距离: {d}")
main()
