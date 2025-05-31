/*
1. Take 10 integer inputs from user and store them in an array and print them on screen.
2. Take 5 numbers from the user & print the greatest of them on the screen.
*/
#include<stdio.h>
int main()
{
    /*
    int n1, n2, n3, max;
    printf("Enter three integers:\n");
    scanf("%d %d %d", &n1, &n2, &n3);   //3,5,4;    5,5,3
    max = n1;           // max = 3                  max = 5
    if (max < n2)       // True                     False
    {   
        max = n2;       // max = 5                  ne
    }
    if (max < n3)       //  False                   False
    {
        max = n3;       // not executed             ne
    }
    printf("%d is the greatest number.", max)   //5  5  
    return 0;
    */
    int arr[5], i, max;
    printf("Enter five integers:\n");
    for(i=0; i<5; i++)
    {
        scanf("%d", &arr[i]);
    }
    max = arr[0];
    for(i=1; i<5; i++)
    {
        if (max < arr[i])
        {
            max = arr[i];
        }
    }
    printf("%d is the greatest number.", max); 
    return 0;
}