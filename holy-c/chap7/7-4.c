#include <stdio.h>
#include <math.h>

double volume_cy(float h, float r)
{
    float v = h * 3.14 * pow(r, 2);
    return v;
}

int main()
{
    float r, h, v;
    scanf("%f%f", &h, &r);
    v = volume_cy(r, h);
    printf("%f\n", v);
    return 0;
}
