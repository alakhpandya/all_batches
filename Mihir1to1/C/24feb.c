/*
1. Write a C program to add two numbers given by user with the help of pointers.
2. Call by Reference
*/
/*
#include<stdio.h>
int addition(int *ptr1, int *ptr2)
{
    int add;
    add = *ptr1 + *ptr2;
    return add;
}

int main()
{
    int number1, number2, sum;
    printf("Please enter two numbers: ");
    scanf("%d %d", &number1, &number2);
    sum = addition(&number1, &number2);
    printf("sum = %d", sum);
    return 0;
}
*/

//Predict what the following program is doing & what will be its output
#include <stdio.h>
int cL(char* ch)
{
    int ctr = 0;
    while (*ch != '\0') 
    {
        ctr++;
        ch++;
    }
    return ctr;
}
void main() 
{
    char str1[25];
    int sl;
    printf("Input a string : ");
    fgets(str1, sizeof str1, stdin);
    sl = cL(str1);
    printf("Output : %d ", sl-1);
}