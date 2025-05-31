// Class work:
/*
1. Ask an integer from user & print product of all the natural numbers till that integer.
2. Write a C program to find & print all the factors of the integer given by user.
3. Write a C program to check whether the number given by user is prime or not.
HW:
4. Write a C program to print all the prime factors of the integer given by user.
*/
#include<stdio.h>

int main()
{
    int n, i, prime=1;
    printf("Enter the number you want to check: ");
    scanf("%d", &n);    //n=7
    for(i=2; i<n; i++)  // n = 25; i = 2, 3, 4, 5
    {
        if (n % i == 0)
        {
            printf("Not Prime.");
            prime = 0;
            break;
        }
    }
    if (prime == 1)
    {
        printf("Prime.");
    }
    return 0;
}