#include <stdio.h>

int main()
{
    int a, b;
    int *pointer_1 = &a;
    int *pointer_2 = &b;
    scanf("%d%d", pointer_1, pointer_2);
    printf("*pointer_1=%d,*pointer_2=%d\n", *pointer_1, *pointer_2);
    return 0;
}
