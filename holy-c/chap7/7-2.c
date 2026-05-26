#include <stdio.h>
#include <math.h>

double volume_c(double r, double h)
{
    double vol = pow(r, 2) * 3.14 * h / 3;
    return vol;
}

int main()
{
    double r, h, v;
    scanf("%lf%lf", &r, &h);
    v = volume_c(r, h);
    printf("%.2lf\n", v);
    return 0;
}
