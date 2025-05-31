#include<stdio.h>

int main()
{
    int a[5], i;
    printf("Enter 5 integer to store in array:\n");
    for(i=0; i<5; i++)
    {
        scanf("%d", &a[i]);
    }
    printf("\nYour array is:\n");
    for(i=0; i<4; i++)
    {
        printf("%d, ", a[i]);
    }
    printf("%d", a[4]);
    return 0;
}
/*
Make individual C programs to do each of the following array operations:
In each of the program below ask user to enter 5 integers, store them in an array & do the followings:
1. Find the greatest number from the array of 5 numbers 
    hint: take a variable "max", assign 0th element of the array into "max" and then compare max with each element of array. If any of the element is found bigger than "max", assign that element into "max".
2. Find sum of all the numbers
3. Ask user what does she want to do -to find greatest number or to find smallest number and print accordingly.
4. Calculate & print average of all the numbers in the array.
*/