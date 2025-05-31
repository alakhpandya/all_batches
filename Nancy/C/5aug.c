/*
#include<stdio.h>
int main()
{
    int number;
    printf("Enter any number: ");
    scanf("%d", &number);
    if (number > 0)
    {
        printf("The number is positive.");
    }
    else if (number == 0)
    {
        printf("The number is neutral.");
    }
    else
    {
        printf("The number is negative.");
    }
    printf("\nThanks for using our program!");
    return 0;
}
*/
#include<stdio.h>
int main()
{
    int number;
    printf("Enter any number: ");
    scanf("%d", &number);   // number = 5
    if (number > 0)
    {
        printf("The number is positive.");
    }
    if (number > 0)
    {
        printf("The number is neutral.");
    }
    if (number < 0)
    {
        printf("The number is negative.");
    }
    printf("\nThanks for using our program!");
    return 0;
}
/*
Homework:
1. Ask length and bredth of a rectangle from user, determine and print whether it is a squre or not.
*/