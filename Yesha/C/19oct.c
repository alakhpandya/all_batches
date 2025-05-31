/*
Ask 5 integers from user & print the greates of them.

#include<stdio.h>
int main()
{
    int a, b, c, d, e;
    printf("Enter three numbers:\n");
    scanf("%d %d %d %d %d", &a , &b , &c, &d, &e);
    printf("the largest number is ");
    if (a>=b && a>=c && a>=d && a>=e)
    {
        printf("%d", a);
    }
    if(b>=a && b>=c && b>=d && b>=e)
    {
        printf("%d", b);
    }
    if(c>=a && c>=b && c>=d && c>=e)
    {
        printf("%d", c);
    }
    if(d>=a && d>=b && d>=c && d>=e)
    {
        printf("%d", d);
    }
    if (e>=a && e>=b && e>=c && e>=d)
    {
        printf("%d", e);
    }
    return 0;
}
*/
/*
#include<stdio.h>

int main()
{
    int a0, a1, a2, a3, a4, max;
    printf("Enter 5 integers:\n");
    scanf("%d %d %d %d %d", &a0, &a1, &a2, &a3, &a4);
    max = a0;
    if (a1 > max)
    {
        max = a1;
    }
    if (a2 > max)
    {
        max = a2;
    }
    if (a3 > max)
    {
        max = a3;
    }
    if (a4 > max)
    {
        max = a4;
    }
    return 0;
}
*/
#include<stdio.h>

int main()
{
    int a[5], i, max;
    printf("Enter 5 integers:\n");
    for(i=0; i<5; i++)
    {
        scanf("%d", &a[i]);
    }
    max = a[0];
    for(i=1; i<5; i++)
    {
        if (a[i] > max)
        {
            max = a[i];
        }
    }
    printf("The greates number in the array is: %d", max);
    return 0;
}