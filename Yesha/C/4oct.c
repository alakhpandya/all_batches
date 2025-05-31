// Make a C program to find HCF of two given numbers.
/*
hcf(60, 27)
60 : 1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60 
27 : 1, 3, 9, 27
hcf = 3

*/
/*
#include<stdio.h>

int main()
{
    int a, b, r = 1, temp, c, d;
    printf("Enter two integers to find their hcf:\n");
    scanf("%d %d", &a, &b);
    c = a;
    d = b;
    if (a < b)
    {
        temp = a;
        a = b;
        b = temp;
    }
    while (r > 0)
    {
        r = a % b;
        a = b;
        b = r;
    }
    printf("hcf (%d, %d) = %d", c, d, a);
    return 0;
}
*/
// Nested loops
/*
#include<stdio.h>

int main()
{
    int i, j, count=0;
    for(i=1; i<=3; i++)
    {   //i = 1, 2, 3
        printf("i = %d\n", i);
        for(j=1; j<=5; j++)
        {
            printf("\tj = %d\n", j);    // j = 1,2,3,4,5;  j = 1,2,3,4,5;  j = 1,2,3,4,5
            count++;
        }
    }
    printf("count = %d\n", count);
    return 0;
}
*/
#include<stdio.h>

int main()
{
    int i, j, n;
    for(i=1; i<=5; i++)
    {
        for(j=1; j<=i; j++)
        {
            printf("*");
        }
        printf("\n");
    }
    return 0;
}
/*
HW:
Make use of nested for loops to produce following patterns on the output:
1.
    *****
    ****
    ***
    **
    *
2.
     *
    **
   ***
  ****
 *****
*/