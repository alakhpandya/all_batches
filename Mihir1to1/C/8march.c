//function without argument, without return
/*
#include<stdio.h>
void mihir()
{
    printf("Mihir studies B.Tech. He is in PDEU and he is a good boy. He lives in Prahlad Nagar.\n");
}
int main()
{
    int a, b;
    printf("Enter two numbers: ");
    scanf("%d %d", &a, &b);
    if (a>b)
    {
        mihir();
    }
    if (a - b > 0)
    {
        mihir();
    }
    if (a + b > 0)
    {
        mihir();
    }
    if (a * b > 0)
    {
        mihir();
    }
    return 0;
}
*/
//function with argument & with return
#include<stdio.h>
long int factorial(int num)
{
    int i;
    long int fac=1;
    for ( i = num; i > 0; i--)
    {
        fac = fac * i;
    }
    // printf("%d! = %ld", num, fac);
    return fac;
}

int main()
{
    int a, b; 
    long int n, m, sum;
    printf("Enter two numbers: ");
    scanf("%d %d", &a, &b);
    n = factorial(a);
    m = factorial(b);
    sum = n + m;
    printf("sum = %ld", sum);
    return 0;
}

a = first term
r = ratio
n = term to calculate
an = a0*r^(n-1)