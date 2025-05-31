/*
Write a C program that takes 20 integers from user and stores them in an array. Now ask user to enter an integer and print whether that integer is in the array or not.
*/
#include<stdio.h>
int main()
{
    int a[10], i, n, belongs = 0;       // flag variable
    printf("Enter 10 integers:\n");
    for(i=0; i<10; i++)
    {
        scanf("%d", &a[i]);
    }
    printf("Now enter any integer: ");
    scanf("%d", &n);
    for(i=0; i<10; i++)
    {
        if (n == a[i])
        {
            printf("%d belongs to the array.", n);
            belongs = 1;
            break;
        }
    }
    if (belongs == 0)
    {
        printf("%d does not belong to the array.", n);
    }
    return 0;
}
/*
Write a C program that takes 10 integers from user and stores them in an array. Now print all the prime numbers of the array on the screen.
*/