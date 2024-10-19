/*
Make a C program that prints greatest of 3 numbers stored in an array.
*/
#include<stdio.h>
int main()
{
    int arr[10]; // arr[5] = {9, 15, 12, 20, 7}
    int i, max;
    printf("Enter 5 integers:\n");
    for(i=0; i<10; i++)
    {
        scanf("%d", &arr[i]);
    }
    max = arr[0];   // max = 9
    for(i=1; i<10; i++)
    {
        if (max < arr[i])   // max < 15?
        {
            max = arr[i];   // max = 15
        }
    }
/*
    if (max < arr[2])   // max < 12?
    {
        max = arr[2];
    }
    if (max < arr[3])
    {
        max = arr[3];
    }
    if (max < arr[4])
    {
        max = arr[4];
    }
*/
    printf("Largest number in the array = %d", max);
    return 0;
}