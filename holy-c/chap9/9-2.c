#include <stdio.h>
#include <string.h>

int main()
{
    struct Worker {
        char name[10];
        float base_wage;
        float float_wage;
        float expend;
    } worker[3];
    strcpy(worker[0].name, "zhao");
    strcpy(worker[1].name, "qian");
    strcpy(worker[2].name, "sun");
    worker[0].base_wage = 240;
    worker[1].base_wage = 360;
    worker[2].base_wage = 560;
    worker[0].float_wage = 420;
    worker[1].float_wage = 120;
    worker[2].float_wage = 0;
    worker[0].expend = 45;
    worker[1].expend = 30;
    worker[2].expend = 180;
    for (int i = 0; i <= 2; i++) {
        printf("%s:%.2f\n", worker[i].name,
                            worker[i].base_wage +
                            worker[i].float_wage -
                            worker[i].expend);
    }
    return 0;
}
