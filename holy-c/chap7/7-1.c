#include <stdio.h>

double area_t(double a, double b, double h)
{
    double area = (a + b) * h / 2;
    return area;
}

int main()
{
    double a, b, h, s;
    scanf("%lf%lf%lf", &a, &b, &h);
    s = area_t(a, b, h);
    printf("%.2lf\n", s);
    return 0;
}
