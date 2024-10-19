// Make a C program that prints multiplicative table of 9
#include<stdio.h>
int main()
{
    int number = 25, i;
    for(i=1; i<=10; i++)
    {
        printf("%d x %d = %d\n", number, i, number*i);
    }
    return 0;
}
/*
Output:
9 x 1 = 9
9 x 2 = 18
9 x 3 = 9*3
9 x 4 = 9*4
number x i = number*i
*/
/*
#include<stdio.h>

int main()
{
    int i;
    for(i=-5; i<5; i++)
    {
        printf("%d. Hello Yesha!\n", i+6);
    }
    printf("Thanks for using our program!");
    return 0;
}

i = 1, 3, 5, 7, 9, 11, 13, 15, 17, 19
i = 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
i = 20, 18, 16, 14, 12, 10, 8, 6, 4, 2
i = 1, 10, 100, 1000
*/