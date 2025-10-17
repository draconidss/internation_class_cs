#include <stdio.h>

void increment(int *p)
{
    (*p)++; // increment the value pointed by p
}

void increment_by_value(int x)
{
    x++; // increment the value of x (local copy)
}

int main(void)
{
    // * 是根据地址去对应的值
    // & 是根据值去对应的地址
    // p 是变量 a 的地址
    int a = 10;
    printf("Value of *&a=%d\n", *&a);

    increment_by_value(a);                                      // copy by value
    printf("Value of a after increment_by_value(a) = %d\n", a); //

    increment(&a);                                      // pass by reference(pointer)
    printf("Value of a after increment(&a) = %d\n", a); //

    short *j;
    j = (short *)0x1234;
    j = j + 1; // 0x1236
    printf("Value of j = %p\n", j);
    return 0; // equal exit(0);
}