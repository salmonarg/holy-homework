#include <stdio.h>

void swap(int *pa, int *pb)
{
    int tmp;
    tmp = *pa;
    *pa = *pb;
    *pb = tmp;
}

int main()
{
    int a, b, c;
    int *p1, *p2, *p3;
    scanf("%d%d%d", &a, &b, &c);
    p1 = &a;
    p2 = &b;
    p3 = &c;
    if (*p1 > *p2) {
        swap(p1, p2);
    }
    if (*p2 > *p3) {
        swap(p2, p3);
    }
    if (*p1 > *p2) {
        swap(p1, p2);
    }
    printf("%d %d %d\n", a, b, c);
    return 0;
}
