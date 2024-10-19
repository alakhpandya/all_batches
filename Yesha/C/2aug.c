/*
1. Take 10 integers from the user & print their sum on the screen.
2. Make a C program that takes a number from user & prints sum of all the natural numbers till that number on the screen.
3. Ask a number from the user & print factorial of that number on the screen.
    Factorial of a number:
        5! = 1 x 2 x 3 x 4 x 5 = 120
        3! = 6
        4! = 24


#include<stdio.h>
int main()
{
    int n1, n2, n3, n4, n5, n6, n7, n8, n9, n10;
    printf("Enter 10 integers:\n");
    scanf("%d %d %d %d %d %d %d %d %d %d", &n1, &n2, &n3, &n4, &n5, &n6, &n7, &n8, &n9, &n10);
    printf("sum = %d", n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10);
    return 0;
}
*/
#include<stdio.h>
int main()
{
    int number, sum = 0, i;
    printf("Please enter the number: ");
    scanf("%d", &number);       // number = 5
    for (i = 1; i <= number; i++)
    {
        // printf("\n%d", i);   
        sum = sum + i;
    }
    printf("Sum = %d", sum);
    return 0;
}
/*
iteration   sum     i       new sum
1           0       1       1
2           1       2       3
3           3       3       6
4           6       4       10
5           10      5       15

HW:
Make a C program that takes a number from user & prints product of all the natural numbers till that number on the screen.


*/
