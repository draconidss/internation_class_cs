#include <stdio.h>
#include <string.h>
#include <stdlib.h> // include malloc, free

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

    printf("\n");
    int x[12];

    printf("sizeof(x): %zu\n", sizeof(x));                             // 48
    printf("sizeof(int): %zu\n", sizeof(int));                         // 4
    printf("sizeof(x) / sizeof(int): %zu\n", sizeof(x) / sizeof(int)); // 12
    printf("(int)sizeof(x): %d\n", (int)sizeof(x));

    // a[0][0]=100, others 0
    // arr is a pointer of arr[0]
    int arr[4][2] = {100};
    printf("arr[0]: %p\n", arr[0]);
    // *arr is arr[0]
    printf("*arr: %p\n", *arr);
    // *(arr[0]) is arr[0][0]
    printf("*(arr[0]): %d\n", *(arr[0]));
    // **arr is arr[0][0]
    printf("**arr: %d\n", **arr);
    // arr[0][0]
    printf("arr[0][0]: %d\n", arr[0][0]);

    int arr1[5] = {11, 22, 33, 44, 55};

    for (int i = 0; i < 5; i++)
    {
        printf("%d\n", *(arr1 + i));
    }

    int *arr_2;
    int arr_3[] = {1, 2, 3, 4, 5};
    arr_2 = malloc(sizeof(arr_3));
    memcpy(arr_2, arr_3, sizeof(arr_3));
    for (int i = 0; i < 5; i++)
    {
        printf("arr_2[%d]: %d\n", i, *(arr_2 + i));
    }
    free(arr_2);

    char str[] = "Hello";
    printf("len of str: %zd\n", sizeof(str) / sizeof(char)); // 6
    for (int i = 0; i < sizeof(str) / sizeof(char); i++)
    {
        printf("str[%d]: %c\n", i, str[i]);
    }

    char str_2[] = "hello \
    world";
    printf("str_2: %s\n", str_2); // helloworld

    char greeting[50] = "Hello, ""how are you ""today!";
    printf("greeting: %s\n", greeting);

    return 0;
}
