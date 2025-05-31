#include<stdio.h>
/*
void armstrong(int n)
{
    int temp, last_digit, cube, sum = 0;
    temp = n;
    while (n > 0)
    {
        last_digit = n % 10;
        cube = last_digit * last_digit * last_digit;
        sum = sum + cube;
        n = n / 10;
    }
    if (sum == temp)
    {
        printf("%d\n", temp);
    }
    // else
    // {
    //     printf("Not Armstrong.");
    // }
}
*/
int armstrong(int n)
{
    int temp, last_digit, cube, sum = 0;
    temp = n;
    while (n > 0)
    {
        last_digit = n % 10;
        cube = last_digit * last_digit * last_digit;
        sum = sum + cube;
        n = n / 10;
    }
    if (sum == temp)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}
int main()
{
    int n1, n2, i;
    printf("Enter n1: ");
    scanf("%d", &n1);           // 1
    printf("Enter n2: ");
    scanf("%d", &n2);           // 10
    for (i = n1; i <= n2; i++)  //  i = 1; i <= 10; i++
    {
        // armstrong(i);
        if (armstrong(i) == 1)
        {
            printf("%d\n", i);
        }
    }
    return 0;
}