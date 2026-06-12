import math

class Shape:
    def __init__(self, color = "black"):
        self.__color = color
    def get_color(self):
        return self.__color
    def set_color(self, color):
        self.__color = color
    def __str__(self):
        return "颜色: " + self.__color
class Triangle(Shape):
    def __init__(self, side1 = 1.0, side2 = 1.0, side3 = 1.0):
        super().__init__()
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3
    def get_area(self):
        a, b, c = self.__side1, self.__side2, self.__side3
        p = (a + b + c) / 2
        area = math.sqrt(p * (p - a) * (p - b) * (p - c))
        return area
    def __str__(self):
        return (
            f"三角形\n"
            f"{super().__str__()} 边长: "
            f"{self.__side1:g} "
            f"{self.__side2:g} "
            f"{self.__side3:g} \n"
            f"面积 {self.get_area():.2}"
        )
def main():
    a, b, c = map(float, input().split(" "))
    tri = Triangle(a, b, c)
    print(tri.__str__())
main()
