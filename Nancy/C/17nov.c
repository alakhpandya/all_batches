#include<stdio.h>

int main()
{
    int s[10], i, n1, membership=0;
    printf("Enter 10 integers:\n");
    for(i=0; i<10; i++)
    {
        scanf("%d", &s[i]);
    }
    printf("Enter the number you want to check: ");
    scanf("%d", &n1);   // n1 = 15
    for(i=0; i<10; i++)
    {
        if(n1 == s[i])
        {
            printf("The number is in the array.\n");
            membership=1;
            break;
        }
        // else
        // {
        //     printf("Number is not present in the array.\n");
        //     break;
        // }
    } 
    if (membership == 0)
    {
            printf("The number is NOT in the array.");
    }
    return 0;
}