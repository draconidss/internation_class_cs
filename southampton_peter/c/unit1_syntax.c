#include <stdio.h>
// 1123
int main()
{
    printf("%d %s %% \n", (1 + 2), "Draco");
    // format width
    printf("%12f\n", 123.45);
    printf("%-12f\n", 123.45);
    // float
    printf("%.7f\n", 123.45);

    printf("11 / -5: %+i\n", 11 / -5); // -2
    printf("11 %% -5: %+i\n", 11 % -5); // 1

    printf("-11 / -5: %+i\n", -11 / -5); // 2
    printf("-11 %% -5: %+i\n", -11 % -5); // -1

    printf("-11 / 5: %+i\n", -11 / 5); // -2
    printf("-11 %% 5: %+i\n", -11 % 5); // -1

    // bit operation
    printf("%a", 0011 & 1101); // 0001
}