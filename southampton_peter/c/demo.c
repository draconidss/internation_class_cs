#include <stdio.h>
#include <math.h>
// return data type is int
// entry code
int main()
{   
    // var = 5 
    int var = 5;
    // &i is placeholder
    printf("The square of %i is %i.\n", 10, 100);
    printf("The square of %i is %i.\n", 10, 100);

    int var1, var2; 
    printf("Please enter any natural number:\n");
    // input 
    scanf("%i", &var1); 
    var2 = exp2(15); 
    printf("2 to the power of %i is %i\n", var1, var2); 

    float f1 = 123.125, f2;
    int i1, i2 = -150;
    i1 = f1;
    printf ("%f assigned to an int produces %i\n", f1, i1);
    f1 = i2;
    printf ("%i assigned to a float produces %f\n", i2, f1);
    f1 = i2 / 100;
    printf ("%i divided by 100 produces %f\n", i2, f1);
    f2 = i2 / 100.0;
    printf ("%i divided by 100.0 produces %f\n", i2, f2);

    return 0;
}