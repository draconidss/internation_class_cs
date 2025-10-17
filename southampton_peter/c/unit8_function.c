#include <stdio.h>
#include <stdarg.h>

double average(int i, ...)
{
    double total = 0;
    va_list ap;
    va_start(ap, i);
    for (int j = 1; j <= i; ++j)
    {
        total += va_arg(ap, double);
    }
    va_end(ap);
    return total / i;
}

int main()
{
    int a[5] = {22, 37, 3490, 18};
    for (int i = 0; i < 5; i++)
    {
        printf("a[%d]: %d\n", i, a[i]);
    }
    // double result_average = average(3, 1, 2, 3);
    // printf("Average of 1, 2, 3 is %f\n", result_average);
    // result_average = average(5, 10, 15, 20, 25);
    // printf("Average of 5, 10, 15, 20, 25 is %f\n", result_average);
    return 0;
}
