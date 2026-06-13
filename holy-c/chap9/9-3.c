#include <stdio.h>

int main()
{
    struct Student {
        int number;
        char name[20];
        char gender;
        int age;
    } student[3];
    for (int i = 0; i <= 2; i++) {
        scanf("%d", &student[i].number);
        scanf("%s", student[i].name);
        scanf(" %c", &student[i].gender);
        scanf("%d", &student[i].age);
    }
    printf("No. Name sex age\n");
    for (int i = 0; i <= 2; i++) {
        printf("%d ", student[i].number);
        printf("%s ", student[i].name);
        printf("%c", student[i].gender);
        printf(" %d\n", student[i].age);
    }
    return 0;
}
