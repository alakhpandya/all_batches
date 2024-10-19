/*
#include<stdio.h>

int main()
{
    int number, i;
    printf("Which number's table do you want to print?");
    scanf("%d", &number);
    for (i = 1; i <= 10; i++)
    {
        printf("%d x %d = %d\n", number, i, number*i);
    }
    return 0;
}
*/
#include<stdio.h>

int main()
{
    int n1, n2;
    /*
    printf("Enter number 1: ");
    scanf("%d", &n1);
    printf("Enter number 2: ");
    scanf("%d", &n2);
    */
    printf("Enter two numbers: n1 & n2:");
    scanf("%d %d", &n1, &n2);
    printf("%d + %d = %d\n", n1, n2, n1+n2);   
    printf("%d - %d = %d\n", n1, n2, n1-n2);   
    printf("%d x %d = %d\n", n1, n2, n1*n2);   
    printf("%d / %d = %d", n1, n2, n1/n2);   
    return 0;
}