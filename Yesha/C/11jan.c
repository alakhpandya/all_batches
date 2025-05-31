/*
Write a C program that sorts an array having 10 integers in ascending order.
*/
#include<stdio.h>
#define SIZE 10

int main()
{
    int a[SIZE], i, temp, j;
    printf("Enter %d integers:\n", SIZE);
    for(i=0; i<SIZE; i++)
    {
        scanf("%d", &a[i]);
    }
    for(j=0; j<SIZE-1; j++)
    {
        for(i=0; i<SIZE-1; i++)
        {
            if (a[i] > a[i+1]){
                // swap a[i] with a[i+1]
                temp = a[i];
                a[i] = a[i+1];
                a[i+1] = temp;
            }
        }
    }
    printf("Your array is: [\t");
    for(i=0; i<SIZE; i++)
    {
        printf("%d\t", a[i]);
    }
    printf("]\n");
    return 0;
}