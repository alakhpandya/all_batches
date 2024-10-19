// Make a C program that counts number of digits of a given integer.
#include<stdio.h>

int main()
{
    int n, temp, count = 0;
    printf("Enter the number to count its digits: ");
    scanf("%d", &n);        // n = 5782
    temp = n;
    // for(i = 0; i < n; i++)
    // {
    //     temp = temp / 10;   
    // }
    while (temp > 0)
    {
        temp = temp / 10;       // 12384 => 1238 => 123 => 12 => 1 => 0
        count++;
    }
    printf("%d has %d digits.", n, count);
    return 0;
}