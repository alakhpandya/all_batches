// Conditional Statements:
//1. Take a number from user and print if it is positive or not.
#include<stdio.h>
int main()
{
    float number;
    printf("Enter any number of your choice: ");
    scanf("%f", &number);
    if (number > 0)
    {
        printf("The number is positive");
    }
    else if (number == 0)
    {
        printf("The number is neutral");
    }
    else
    {
        printf("The number is negative");
    }
    return 0;
}


// Take length & breadth of a rectangle and conclude if it's a square or not.
