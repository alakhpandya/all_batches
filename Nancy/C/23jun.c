// Variables in C
#include<stdio.h>

int main()
{
    int num1, num2, twice, square;
    float half, division;
    printf("Enter num1 & num2: ");
    scanf("%d %d", &num1, &num2);
    // printf("Enter num1: ");
    // scanf("%d", &num1);
    // printf("Enter num2: ");
    // scanf("%d", &num2);
    twice = num1 + num1;
    printf("%d + %d = %d", num1, num1, twice);
    square = num1 * num1;
    printf("\nSquare of %d is: %d", num1, square);
    half = num1 / 2.0;
    printf("\nhalf of %d is: %0.9f", num1, half);
    printf("\n%d + %d = %d", num1, num2, num1 + num2);
    division = (float) num1 / num2;
    printf("\n%d / %d = %0.3f", num1, num2, division);
    return 0;
}
/*
#include<stdio.h>

int main()
{
    int num1 = 10, twice, square, half;
    // num1 = 8;
    twice = num1 + num1;
    printf("\n%d + %d = %d", num1, num1, twice);
    square = num1 * num1;
    printf("\nSquare of %d is: %d", num1, square);
    half = num1 / 2;
    printf("\nhalf of %d is: %d", num1, half);
    return 0;
}
*/