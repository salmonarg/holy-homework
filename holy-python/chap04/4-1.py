import math

def compute_area(a, b, c, d, alpha):
    p = 0.5 * (a + b + c + d)
    area = math.sqrt((p-a)*(p-b)*(p-c)*(p-d)-a*b*c*d*pow(math.cos(alpha),2))
    return area
def main():
    alpha = math.radians(145) / 2
    area = format(compute_area(3, 4, 5, 5, alpha), ".2f")
    print(f"四边形面积: {area}")
main()
