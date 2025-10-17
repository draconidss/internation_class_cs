#include <stdio.h>

int main()
{
    int a[100] = {0};
    for (int i = 0; i < 100; i++)
    {
        printf("%d ", i, a[i]);
    }

    printf("\n\n");
    int b[15] = {[2] = 29, [9] = 7, [14] = 48};
    for (int i = 0; i < 15; i++)
    {
        printf("%d ", b[i]);
    }
    return 0;
}
