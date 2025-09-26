#include <stdio.h>
int main()
{
    int i = 1, j = 2;
    int result = (i > j) ? i : j;
    printf("result: %d\n", result);

    // switch
    int grade = 1;
    switch (grade)
    {
    case 1:
        printf("True\n");
    case 0:
        printf("False\n");
        break;
    default:
        printf("Illegal\n");
    }

    printf("================Switch2================");

    switch (grade) {
    case 0:
    case 1:
        printf("True\n");
        break;
    default:
        printf("Illegal\n");
    }

    int i_1 = 10;
    while (i_1 > 0)
    {
        printf("i is %d\n", i_1);
        i_1--;
    }

    // iteration 10 times
    for (int i_2 = 0; i < 10; i++){

    }

    return 0;
}