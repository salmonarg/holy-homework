#include <stdio.h>
#include <math.h>

double volume_c(int x)
{
    double v = pow(x, 3);
    return v;
}

int main()
{
    int a;
    double v;
    scanf("%d", &a);
    v = volume_c(a);
    printf("%.2lf\n", v);
    return 0;
}
