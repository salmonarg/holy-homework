class Rectangle:
    def __init__(self, w = 1, h = 1):
        self.__width = w
        self.__height = h
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, w):
        self.__width = w
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, h):
        self.__height = h
    def compute_area(self):
        return self.__width * self.__height
    def compute_perimeter(self):
        return 2 * (self.__width + self.__height)
def main():
    w1, h1 = map(float, input("请输入第一个矩形的宽度和高度: ").split(','))
    w2, h2 = map(float, input("请输入第二个矩形的宽度和高度: ").split(','))
    rect_a = Rectangle(w1, h1)
    rect_b = Rectangle(w2, h2)
    print(f"宽为{rect_a.width:g}和高为{rect_a.height:g}的" \
          f"矩形面积:{rect_a.compute_area():.2f}, " \
          f"周长:{rect_a.compute_perimeter():.2f}")
    print(f"宽为{rect_b.width:g}和高为{rect_b.height:g}的" \
          f"矩形面积:{rect_b.compute_area():.2f}, " \
          f"周长:{rect_b.compute_perimeter():.2f}")
    rect_b.width = 12.11
    rect_b.height = 6.18
    print(f"宽为{rect_b.width:g}和高为{rect_b.height:g}的" \
          f"矩形面积:{rect_b.compute_area():.2f}, " \
          f"周长:{rect_b.compute_perimeter():.2f}")
main()
