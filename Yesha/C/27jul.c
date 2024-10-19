// Home work:
/*
1.  Ask a number from user and display cubes of all the even natural numbers till that number on the screen.
2.  Take 10 integers from the user and print their sum on the screen.   // take a variable sum = 0
3.  Take 10 integers from the user and print their product on the screen.
4.  Take 10 integers from the user and print their average on the screen.
*/
/*
#include<stdio.h>

int main()
{
    int n, i;
    printf("Enter a number to print its multiplicative table: ");
    scanf("%d", &n);
    for(i=1; i<=10; i++)
    {
    printf("%d x %d = %d\n", n, i, n*i);
    printf("%d x %d = %d\n", n+1, i, (n+1)*i);
    }
    return 0;
}

if (25 < marks < 45)  = if (25 < marks && marks < 45)
*/
#include<stdio.h>

int main()
{
    int number, new;
    printf("Enter a number to get absolute value of it: ");
    scanf("%d", &number);
    if (number < 0)
    {
        new = number*(-1);
    }
    printf("Absolute of %d = %d", number, new);
    return 0;
}