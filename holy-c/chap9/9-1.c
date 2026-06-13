#include <stdio.h>

int main()
{
    struct Student {
        long int number;
        char name[10];
        int age;
        float eng_mark;
        float math_mark;
        float chi_mark;
        float po_mark;
        float phy_mark;
        float che_mark;
        float cs_mark;
        float sum;
        float avg;
    } student[10];
    int max_index = 0;
    for (int i = 0; i < 10; i++) {
        scanf("%ld", &student[i].number);
        scanf("%s", student[i].name);
        scanf("%f%f%f%f%f%f%f%f",   &student[i].age,
                                    &student[i].eng_mark,
                                    &student[i].math_mark,
                                    &student[i].chi_mark,
                                    &student[i].po_mark,
                                    &student[i].phy_mark,
                                    &student[i].che_mark,
                                    &student[i].cs_mark);
        student[i].sum =    student[i].eng_mark  + 
                            student[i].math_mark + 
                            student[i].chi_mark  +
                            student[i].po_mark   + 
                            student[i].phy_mark  + 
                            student[i].che_mark  +
                            student[i].cs_mark;
        if (i > 0) {
            if (student[i].sum > student[max_index].sum) {
                max_index = i;
            }
        }
    }
    printf("%s\n", student[max_index].name);
    return 0;
}
